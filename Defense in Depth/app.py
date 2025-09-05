import logging, os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change")

# Hard-coded demo user (use Entra ID auth in Azure; this is for local dev only)
DEMO_USER = os.environ.get("DEMO_USER", "analyst@example.com")
DEMO_PASS_HASH = os.environ.get("DEMO_PASS_HASH") or generate_password_hash(
    os.environ.get("DEMO_PASS", "ChangeMe!123")
)

# Logging to stdout (picked up by App Service + App Insights)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")
log = logging.getLogger("did-app")

@app.after_request
def set_security_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["X-XSS-Protection"] = "0"
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    return resp

@app.route("/")
def home():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        if email.lower() == DEMO_USER.lower() and check_password_hash(DEMO_PASS_HASH, password):
            session["user"] = email
            log.info({
                "event": "login_success",
                "user": email,
                "ip": request.remote_addr,
                "ua": request.headers.get("User-Agent")
            })
            return redirect(url_for("home"))
        log.warning({
            "event": "login_failed",
            "user": email,
            "ip": request.remote_addr
        })
    return render_template("login.html")

@app.route("/logout")
def logout():
    user = session.pop("user", None)
    if user:
        log.info({"event": "logout", "user": user})
    return redirect(url_for("login"))

@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
