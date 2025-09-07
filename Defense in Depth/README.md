
# Defense in Depth Lab (DID-lab) – Azure

This project demonstrates a **defense in depth (DiD) architecture** in Microsoft Azure by deploying and securing a web application, integrating it with **Azure Front Door, Key Vault, Entra ID (Azure AD), Log Analytics, and Microsoft Sentinel**. The lab simulates real-world SOC monitoring and security enforcement.

---

## 📌 Lab Objectives
- Deploy a secure Azure Web App (Python runtime).
- Protect with **Front Door + WAF**.
- Enforce **Access Restrictions** (IP allow/deny).
- Centralize logging in **Log Analytics Workspace (LAW)**.
- Enable **Sentinel detections & dashboards**.
- Secure secrets in **Key Vault** with managed identity.
- Monitor **Entra ID sign-ins and audit logs**.

---

## 🏗️ Architecture Overview
1. **Azure Web App** (DID-lab-WEB)  
2. **Azure Front Door** (global entry, WAF rules)  
3. **Key Vault** (secrets, RBAC access)  
4. **Entra ID** (auth & SSO)  
5. **Log Analytics Workspace** (central logs)  
6. **Sentinel** (threat detection & response)  

---

## 🚀 Deployment Steps

### 1. Deploy Web App
- Provisioned via Azure Portal under **DID-lab-RG**.
- Configured with **Python 3.13** runtime.

![Web App Configuration](assets/webapp-config.jpeg)

---

### 2. Configure Networking & Access Restrictions
- Applied **allow/deny IP rules**.
- Verified 403 blocks for unauthorized IPs.

![Networking Overview](assets/networking-overview.jpeg)  
![Access Restrictions](assets/access-restrictions.jpeg)  
![403 Error](assets/403-error.jpeg)

---

### 3. Enable Diagnostics → Log Analytics
- Sent **HTTP, Console, Application logs** to LAW.
- Confirmed logs with KQL queries.

```kusto
AppServiceHTTPLogs
| summarize Hits=count() by ScStatus
| order by Hits desc
```

![Diagnostic Setting](assets/diagnostic-setting.jpeg)  
![KQL Log Query](assets/kql-query.png)

---

### 4. Deploy Key Vault
- Created **DID-Key-Vault-KV**.
- Applied **Azure RBAC** for access.
- Configured diagnostic logging to LAW.

![Key Vault Deployment](assets/keyvault-deployment.jpeg)  
![Key Vault RBAC](assets/keyvault-rbac.jpeg)  
![Key Vault Diagnostic Settings](assets/keyvault-diagnostics.jpeg)

---

### 5. Enable Entra ID Authentication
- Configured **Entra ID login** for App Service.
- Verified redirect and token-based access.

![Entra Permissions Prompt](assets/entra-permissions.jpeg)

---

### 6. Log Analytics & Sentinel Integration
- Connected **App Service + Key Vault + Entra ID logs** to LAW.
- Enabled **Sentinel detections** for failed logins and suspicious access.

![LAW Overview](assets/law-overview.jpeg)  
![Sentinel Workspace](assets/sentinel-workspace.jpeg)  
![Sentinel Query](assets/sentinel-query.jpeg)  
![Sentinel Rule](assets/sentinel-rule.jpeg)  
![Entra Logs Connector](assets/entra-logs.jpeg)

---

## 📊 Example KQL Queries

### Failed Logins (401, 404)
```kusto
AppServiceHTTPLogs
| where ScStatus in (401,404)
| summarize Count=count() by bin(TimeGenerated, 10m)
```

### Blocked IPs
```kusto
AppServiceHTTPLogs
| where ScStatus == 403
| summarize Blocked=count() by ClientIP, bin(TimeGenerated, 10m)
```

### Key Vault Access
```kusto
AzureDiagnostics
| where ResourceType == "VAULTS"
| where OperationName == "SecretGet"
| summarize Accesses=count() by CallerIPAddress, Caller, bin(TimeGenerated, 1h)
```

---

## 🛡️ Defense in Depth Achievements
- **Network Security** → IP restrictions + private endpoints.
- **Identity Security** → Entra ID authentication + audit logs.
- **Application Security** → Web App behind Front Door + WAF.
- **Secrets Management** → Key Vault with RBAC + monitoring.
- **Monitoring & Detection** → Sentinel queries, rules, dashboards.

---

## 📌 Next Improvements
- Complete **Front Door WAF policy** enforcement.
- Enable **Defender for App Service & Key Vault**.
- Build **Sentinel Workbooks** for dashboards.
- Automate response with **Logic Apps**.

---

## 📷 Screenshots
All screenshots are stored in the `/assets/` folder for GitHub compatibility.
