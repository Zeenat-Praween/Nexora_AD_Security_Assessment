# 🛡️ NEXORA SYSTEMS
## Active Directory Security Assessment & Threat Detection Platform

### 1. Project Overview

Nexora Systems is a simulation-based cybersecurity assessment platform designed to identify potential security weaknesses in Active Directory environments using synthetic security records.

The platform evaluates user account configurations, service account security, permission assignments, and authentication activity patterns. It generates security findings and presents them through an interactive dashboard.

**Note:** This project uses synthetic datasets and does not connect to a live Active Directory domain.

### 2. Problem Statement

Active Directory environments manage user identities, service accounts, permissions, and authentication processes. Misconfigurations in these areas may introduce security risks.

Nexora Systems provides a simulation-based approach to reviewing these security areas, identifying potential weaknesses, and presenting findings in an understandable format.

### 3. Project Objectives

- Identify weak user account configurations.
- Review missing Multi-Factor Authentication (MFA).
- Evaluate service account configurations.
- Identify potentially excessive permissions.
- Analyze suspicious authentication patterns.
- Generate structured security reports.
- Present findings through an interactive dashboard.

### 4. Key Features

- User Security Audit
- Service Account Audit
- Permissions Audit
- Authentication Analysis
- Security Findings Dashboard
- Risk-based findings classification
- CSV Report Generation
- Interactive Streamlit Interface

### 5. Security Assessment Modules

#### 5.1 User Security Audit

Reviews user account configurations and identifies:
- Missing MFA.
- Passwords that never expire.
- Older password change records.
- Privileged accounts without MFA.
- Disabled accounts requiring review.

#### 5.2 Service Account Audit

Evaluates service account configurations, including:
- Service Principal Name (SPN) configuration.
- Password age.
- Managed service account configuration.
- Account ownership.
- Privileged service accounts.

#### 5.3 Permissions Audit

Reviews access control assignments and identifies:
- Potentially excessive permissions.
- Administrative-equivalent permissions.
- Full Control and Modify assignments.
- Missing or undocumented business justifications.

#### 5.4 Authentication Analysis

Analyzes synthetic authentication records to identify:
- Repeated failed login attempts.
- Failed login attempts followed by successful authentication.
- Unusual login times.
- Login attempts involving disabled accounts.

### 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard |
| Pandas | Data processing and analysis |
| NumPy | Numerical operations |
| Plotly | Data visualization |
| CSV | Synthetic datasets and security reports |
| CSS | Dashboard customization |

### 7. Project Structure

```text
Nexora_AD_Security_Assessment/
│
├── assets/
│   └── nexora_background.jpg
│
├── data/
│   ├── ad_users.csv
│   ├── service_accounts.csv
│   ├── permissions.csv
│   └── authentication_events.csv
│
├── modules/
│   ├── __init__.py
│   ├── user_security_audit.py
│   ├── service_account_audit.py
│   ├── permissions_audit.py
│   └── authentication_analyzer.py
│
├── reports/
│
├── documentation/
│
├── mitre_mapping/
│
├── app.py
├── README.md
└── requirements.txt
```

### 8. Installation and Setup

**Step 1: Clone or download the project**

Download the project folder to your local system.

**Step 2: Create a virtual environment**

```bash
python -m venv venv
```

**Step 3: Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**Step 4: Install dependencies**

```bash
pip install -r requirements.txt
```

### 9. How to Run

Run the following command from the project directory:

```bash
streamlit run app.py
```

The application will open in your default web browser.

### 10. Output and Reports

The platform generates structured CSV reports for:

- User Security Findings
- Service Account Findings
- Permissions Findings
- Authentication Findings

The dashboard displays the detected findings and provides report download functionality.

### 11. Limitations

- The platform uses synthetic security records.
- It does not connect to a live Active Directory domain.
- It does not collect real Windows Security Event Logs.
- Findings depend on the predefined audit rules and available input records.
- Results represent simulated security assessment outcomes, not a production security certification.

### 12. Future Scope

Potential future enhancements include:

- Integration with authorized Active Directory test environments.
- Support for Windows Security Event Log analysis.
- Advanced security analytics.
- Enhanced visualization and reporting.
- Expanded detection rules.
- Integration with MITRE ATT&CK knowledge bases.

### 13. Conclusion

Nexora Systems demonstrates how Python-based data processing and interactive visualization can support a structured review of Active Directory security configurations.

By combining multiple audit modules with centralized findings and report generation, the platform provides an educational demonstration of security assessment and threat detection concepts.
