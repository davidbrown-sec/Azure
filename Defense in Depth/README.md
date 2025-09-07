
Defense in Depth Lab (DID-lab) – Azure

This project demonstrates a defense in depth (DiD) architecture in Microsoft Azure by deploying and securing a web application, integrating it with Azure Front Door, Key Vault, Entra ID (Azure AD), Log Analytics, and Microsoft Sentinel. The lab simulates real-world SOC monitoring and security enforcement.

⸻

📌 Lab Objectives
	•	Deploy a secure Azure Web App (Python runtime).
	•	Protect with Front Door + WAF.
	•	Enforce Access Restrictions (IP allow/deny).
	•	Centralize logging in Log Analytics Workspace (LAW).
	•	Enable Sentinel detections & dashboards.
	•	Secure secrets in Key Vault with managed identity.
	•	Monitor Entra ID sign-ins and audit logs.

⸻

🏗️ Architecture Overview
	1.	Azure Web App (DID-lab-WEB)
	2.	Azure Front Door (global entry, WAF rules)
	3.	Key Vault (secrets, RBAC access)
	4.	Entra ID (auth & SSO)
	5.	Log Analytics Workspace (central logs)
	6.	Sentinel (threat detection & response)

⸻

🚀 Deployment Steps

1. Deploy Web App
	•	Provisioned via Azure Portal under DID-lab-RG.
	•	Configured with Python 3.13 runtime.


⸻

2. Configure Networking & Access Restrictions
	•	Applied allow/deny IP rules.
	•	Verified 403 blocks for unauthorized IPs.


⸻

3. Enable Diagnostics → Log Analytics
	•	Sent HTTP, Console, Application logs to LAW.
	•	Confirmed logs with KQL queries.

AppServiceHTTPLogs
| summarize Hits=count() by ScStatus
| order by Hits desc


⸻

4. Deploy Key Vault
	•	Created DID-Key-Vault-KV.
	•	Applied Azure RBAC for access.
	•	Configured diagnostic logging to LAW.


⸻

5. Enable Entra ID Authentication
	•	Configured Entra ID login for App Service.
	•	Verified redirect and token-based access.


⸻

6. Log Analytics & Sentinel Integration
	•	Connected App Service + Key Vault + Entra ID logs to LAW.
	•	Enabled Sentinel detections for failed logins and suspicious access.


⸻

📊 Example KQL Queries

Failed Logins (401, 404)

AppServiceHTTPLogs
| where ScStatus in (401,404)
| summarize Count=count() by bin(TimeGenerated, 10m)

Blocked IPs

AppServiceHTTPLogs
| where ScStatus == 403
| summarize Blocked=count() by ClientIP, bin(TimeGenerated, 10m)

Key Vault Access

AzureDiagnostics
| where ResourceType == "VAULTS"
| where OperationName == "SecretGet"
| summarize Accesses=count() by CallerIPAddress, Caller, bin(TimeGenerated, 1h)


⸻

🛡️ Defense in Depth Achievements
	•	Network Security → IP restrictions + private endpoints.
	•	Identity Security → Entra ID authentication + audit logs.
	•	Application Security → Web App behind Front Door + WAF.
	•	Secrets Management → Key Vault with RBAC + monitoring.
	•	Monitoring & Detection → Sentinel queries, rules, dashboards.

⸻

📌 Next Improvements
	•	Complete Front Door WAF policy enforcement.
	•	Enable Defender for App Service & Key Vault.
	•	Build Sentinel Workbooks for dashboards.
	•	Automate response with Logic Apps.

⸻

📷 Screenshots

All deployment and configuration steps are documented with screenshots throughout this README.
