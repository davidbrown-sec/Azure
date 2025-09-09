# Defense-in-Depth (DID) Lab – Azure Web App Security

This project demonstrates a **Defense-in-Depth (DID)** approach using Azure services.  
I deployed a basic web application and applied multiple security layers: **Identity**, **Perimeter**, **Secrets/Data**, and **Monitoring/Detection**.

---


## 🔹 Layers Implemented

### 1. Identity
- Integrated the web app with **Microsoft Entra ID (Azure AD)** for authentication.  
- Configured **App Service Authentication** to enforce logins.  
- Enabled **Microsoft Entra ID Connector** in Sentinel to ingest:
  - Sign-in Logs (tracks user logons)  
  - Audit Logs (tracks admin changes)

📷 *Example: Sentinel data connector for Entra ID*  
![Entra Connector](<https://drive.google.com/file/d/1LYhzJODA6M4YVa1cOTkby-MviJP5InHo/view?usp=sharing>)  
📸 *File: Screenshot 2025-09-06 at 4.51.15 PM (2).jpeg*

📷 *Entra Connector settings page*  
![Entra Settings](<https://github.com/davidbrown-sec/Azure/blob/8f035345462c427b9eb11817b41216fe26af1d5b/Defense%20in%20Depth/Screenshot%202025-09-06%20at%204.54.43%20PM%20(2).png>)  
📸 *File: Screenshot 2025-09-06 at 4.54.43 PM (2).jpeg*

---

### 2. Perimeter
- Configured **App Service Access Restrictions** to only allow traffic from my trusted IP.  
- Verified **403 Forbidden blocks** when accessing from untrusted sources (VPN).  
- Created an **Analytics Rule** in Sentinel to detect repeated unauthorized or suspicious access attempts.

📷 *Blocked access page (403)*  
![403 Block](<link-to-403-block-screenshot>)  
📸 *File: Screenshot 2025-09-06 at 2.19.23 PM (2).jpeg*

📷 *Sentinel Analytics Rule in Defender portal*  
![Sentinel Rule](<link-to-sentinel-rule-screenshot>)  
📸 *File: Screenshot 2025-09-06 at 4.32.34 PM (2).jpeg*

---

### 3. Data / Secrets
- Created an **Azure Key Vault** to store sensitive values instead of hardcoding secrets.  
- Granted my Web App’s **Managed Identity** the `Key Vault Secrets User` role.  
- Configured **Application Settings** in App Service to reference Key Vault secrets.  
- Enabled **Key Vault diagnostic logs** to monitor access attempts.

📷 *Key Vault RBAC role assignment*  
![Key Vault RBAC](<link-to-keyvault-rbac-screenshot>)  
📸 *File: Screenshot 2025-09-06 at 8.22.57 AM (2).jpeg*

📷 *Key Vault access configuration page*  
![Key Vault Config](<link-to-keyvault-access-config-screenshot>)  
📸 *File: Screenshot 2025-09-06 at 8.20.25 AM.png*

---

### 4. Monitoring / Detection
- Connected the Web App and Key Vault diagnostic logs to my **Log Analytics Workspace (LAW)**.  
- Integrated **Azure Sentinel** to centralize monitoring and generate incidents.  
- Built detection rules to alert on:
  - Repeated failed web requests  
  - Excessive failed Entra ID sign-ins  
  - Unauthorized Key Vault access attempts  

📷 *Sentinel Logs showing suspicious requests*  
![Sentinel Logs](<link-to-sentinel-logs-screenshot>)  
📸 *File: Screenshot 2025-09-06 at 4.24.35 PM (2).jpeg*

📷 *Log Analytics Workspace overview*  
![LAW Overview](<link-to-law-overview-screenshot>)  
📸 *File: Screenshot 2025-09-06 at 1.57.17 PM.jpeg*

---

## 🔹 Lab Highlights
- ✅ **Defense in Depth applied:** Identity, Perimeter, Data, and Monitoring layers.  
- ✅ **Real-world detections:** Access restriction bypass attempts, failed logins, and secret access monitoring.  
- ✅ **Azure native tools:** App Service, Entra ID, Key Vault, Log Analytics, Sentinel.  
- ✅ **Actionable alerts:** Automatic Sentinel incidents tied to suspicious activity.  


---

## 🔹 Next Steps
- Add **Azure Front Door with WAF** for advanced perimeter defense.  
- Expand Sentinel rules with MITRE ATT&CK mapping.  
- Automate deployments using **Bicep/ARM templates** or **Terraform**.

---
