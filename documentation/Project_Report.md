# Nexora Systems
## Active Directory Security Assessment & Threat Detection Platform

**Project Report**

---

## 1. Abstract

Nexora Systems – Active Directory Security Assessment & Threat Detection Platform is a Python-based, simulation-oriented cybersecurity project designed to identify common security weaknesses in Active Directory environments.

The platform evaluates synthetic Active Directory-related records to identify potentially risky account configurations, service account weaknesses, excessive permissions, and unusual authentication patterns.

The system consists of four independent security assessment modules: User Security Audit, Service Account Audit, Permissions Audit, and Authentication Analysis. Each module applies predefined security rules to synthetic CSV datasets and generates findings that can be reviewed through an interactive Streamlit dashboard.

The primary objective of this project is to demonstrate fundamental Active Directory security assessment concepts in a controlled educational environment. It does not connect to a live Active Directory domain or perform real-world security testing.

---

## 2. Introduction

Active Directory (AD) is a directory service commonly used by organizations to manage users, computers, authentication, and access permissions within a network.

Improper account configurations, weak service account management, excessive permissions, and unusual authentication activity can create security risks.

Regular security assessments help organizations identify configuration weaknesses and improve their security posture.

Nexora Systems is developed as an educational platform to demonstrate how selected Active Directory security-related indicators can be reviewed using Python-based analysis and a dashboard interface.

The project uses synthetic data rather than information collected from an actual organization or domain.

---

## 3. Problem Statement

Organizations need to monitor account configurations, service accounts, access permissions, and authentication activities to identify potential security weaknesses.

Manual review of these areas can be time-consuming and may make it difficult to organize findings in a consistent format.

This project addresses the problem by providing a simulation-based platform that:

- Reviews user account configurations.
- Identifies selected service account weaknesses.
- Highlights potentially excessive permissions.
- Detects predefined unusual authentication patterns.
- Presents assessment findings through a centralized dashboard.

---

## 4. Aim of the Project

The aim of Nexora Systems is to develop a Python-based simulation platform that assesses selected Active Directory security indicators and presents potential configuration weaknesses through an interactive dashboard.

---

## 5. Objectives

The main objectives are:

1. To understand fundamental Active Directory security concepts.
2. To assess user account configurations using predefined security rules.
3. To review service account configurations and ownership information.
4. To identify potentially excessive access permissions.
5. To analyze synthetic authentication records for unusual patterns.
6. To classify findings according to project-defined severity levels.
7. To generate structured CSV reports.
8. To display assessment results through a Streamlit dashboard.

---

## 6. Scope of the Project

The project focuses on four major areas:

- User Account Security
- Service Account Security
- Permissions and Access Control
- Authentication Activity Analysis

The platform is intended for educational demonstration and controlled testing using fictional records.

### Project Boundaries

- No live Active Directory connection is implemented.
- No actual Windows Event Logs are collected.
- No real organizational user accounts are accessed.
- No real-world attacks or exploitation are performed.
- All assessment results are generated from synthetic CSV records and predefined rules.

---

## 7. Existing System

Traditional security reviews may involve manually checking account settings, service account configurations, permissions, and authentication records.

This approach can require considerable effort, especially when information is distributed across multiple sources.

A structured assessment tool can make these reviews easier to organize and understand.

---

## 8. Proposed System

Nexora Systems provides a centralized dashboard for reviewing simulated Active Directory security information.

The proposed system uses Python modules to analyze synthetic CSV files. Each module performs specific checks and generates a separate findings report.

The dashboard allows users to execute individual assessments and view the generated results.

### Key Features

- Interactive Streamlit dashboard.
- Four independent assessment modules.
- Synthetic CSV-based input data.
- Rule-based security checks.
- High, Medium, and Low severity classification.
- CSV-based findings reports.
- Centralized presentation of assessment results.

---

## 9. System Architecture

The platform follows a modular architecture.

### Architecture Workflow

1. The user opens the Streamlit dashboard.
2. The user selects a security assessment module.
3. The selected Python module reads its corresponding synthetic CSV file.
4. Predefined security rules evaluate the available records.
5. Potential security findings are identified.
6. Findings are saved as CSV reports.
7. The dashboard reads and displays the generated reports.

### Architecture Diagram

```text
             USER
               |
               v
       STREAMLIT DASHBOARD
               |
       ---------------------
       |         |         |
       v         v         v
   User       Service   Permissions
  Security    Account     Audit
   Audit       Audit
       |         |         |
       ---------------------
               |
               v
      Authentication Analysis
               |
               v
       SYNTHETIC CSV DATA
               |
               v
        SECURITY RULES
               |
               v
       FINDINGS GENERATION
               |
               v
          CSV REPORTS
               |
               v
       DASHBOARD DISPLAY
```

---

## 10. Methodology

The project follows a rule-based assessment methodology.

### Step 1: Data Preparation

Synthetic CSV datasets were created to represent different Active Directory-related records.

These datasets contain fictional users, service accounts, permissions, and authentication events.

### Step 2: Data Processing

Python and Pandas are used to read and process the CSV records.

### Step 3: Security Assessment

Each module evaluates the records using predefined conditions.

### Step 4: Finding Classification

Identified issues are assigned severity levels according to the rules implemented in the project.

The severity levels are:

- **High:** A finding indicating a potentially significant security concern.
- **Medium:** A finding indicating a configuration weakness that should be reviewed.
- **Low:** A finding indicating a lower-priority issue or review requirement.

These classifications are project-defined and are not presented as a universal industry severity standard.

### Step 5: Report Generation

The assessment modules generate structured CSV files containing identified findings.

### Step 6: Dashboard Presentation

The Streamlit dashboard displays the findings in a readable table format.

---

## 11. Project Modules

### 11.1 User Security Audit

**File:** `modules/user_security_audit.py`

This module evaluates synthetic user account records to identify selected account security weaknesses.

It checks for:

- Privileged accounts without MFA.
- Accounts configured so that passwords never expire.
- Passwords that have not been changed for more than the configured threshold.
- Enabled standard accounts without MFA.
- Disabled accounts requiring review.

**Output:** `reports/user_security_findings.csv`

### 11.2 Service Account Audit

**File:** `modules/service_account_audit.py`

This module evaluates service account configurations.

It checks for:

- Service accounts with SPN configuration that do not use the managed service account configuration represented in the dataset.
- Old service account passwords.
- Privileged service accounts without a defined owner.
- Service accounts with missing ownership information.

**Output:** `reports/service_account_findings.csv`

### 11.3 Permissions Audit

**File:** `modules/permissions_audit.py`

This module reviews synthetic permission assignments to identify potentially excessive access.

It checks for:

- Admin-equivalent permissions.
- Full Control permissions with missing or undocumented business justification.
- Modify permissions with missing or undocumented business justification.
- Access assignments that require further review.

**Output:** `reports/permissions_findings.csv`

### 11.4 Authentication Analysis

**File:** `modules/authentication_analyzer.py`

This module analyzes synthetic authentication event records to identify predefined unusual patterns.

It checks for:

- Multiple failed login attempts from the same source.
- Failed login attempts followed by a successful login from the same source.
- Successful logins during configured late-night hours.
- Login attempts involving disabled accounts.

**Output:** `reports/authentication_findings.csv`

---

## 12. Technology Stack

The project uses the following technologies:

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard development |
| Pandas | CSV reading and data processing |
| CSV | Input datasets and assessment reports |
| HTML | Dashboard content rendering |
| CSS | Dashboard styling |
| Visual Studio Code | Development environment |

---

## 13. Dataset Description

The project uses four synthetic datasets.

| Dataset | Records | Purpose |
|---|---:|---|
| `ad_users.csv` | 10 | User account assessment |
| `service_accounts.csv` | 5 | Service account assessment |
| `permissions.csv` | 8 | Permission assessment |
| `authentication_events.csv` | 12 | Authentication analysis |

### Dataset Characteristics

- All records are fictional.
- The datasets contain no real organizational account information.
- Authentication IP addresses use the documentation-only address range `192.0.2.0/24`.
- The datasets are designed to demonstrate the project's predefined assessment rules.

---

## 14. Risk Classification

The platform uses three project-defined severity levels.

| Severity | Description |
|---|---|
| High | Potentially significant security weakness requiring priority review |
| Medium | Configuration issue requiring investigation or corrective review |
| Low | Lower-priority issue or account requiring review |

The severity assigned to a finding depends on the conditions implemented in the respective Python module.

---

## 15. Dashboard Implementation

The dashboard is developed using Streamlit.

It provides a centralized interface for running the four assessment modules and viewing their results.

### Dashboard Capabilities

- Displays the project title and overview.
- Provides access to individual assessment modules.
- Executes the selected assessment.
- Displays the total number of generated findings.
- Presents findings in formatted tables.
- Shows a message when no findings are detected or a report is unavailable.

The interface uses a dark background with champagne-gold headings and light-colored text to maintain a consistent visual design.

---

## 16. Testing and Results

The project modules were executed using the prepared synthetic datasets.

Testing focused on verifying whether the predefined assessment conditions were correctly applied and whether the corresponding findings reports were generated.

### Testing Summary

| Module | Testing Focus | Result |
| User Security Audit | Account configuration and MFA checks | Executed successfully |
| Service Account Audit | Password age, ownership, and configuration checks | Executed successfully |
| Permissions Audit | Admin-equivalent permissions and justification checks | Executed successfully |
| Authentication Analysis | Failed logins, late-night activity, and disabled account attempts | Executed successfully |

### User Security Audit Results

The tested user security dataset produced the following findings:

| Severity | Findings |
|---|---:|
| High | 2 |
| Medium | 10 |
| Low | 1 |
| **Total** | **13** |

The results were checked against the expected conditions in the User Security Audit module.

The remaining modules were also executed and their findings were reviewed through the dashboard. Their exact finding totals are not included here because they may depend on the implemented rules and input records.

---

## 17. Limitations

The current implementation has the following limitations:

1. The platform uses synthetic CSV data.
2. It does not connect to a live Active Directory domain.
3. It does not collect real Windows authentication logs.
4. Its detection capabilities are limited to predefined rules.
5. It does not perform real-time monitoring.
6. Its findings require human review and validation.
7. The results should not be treated as a complete security audit of an actual organization.

---

## 18. Future Enhancements

The project can be extended with the following features in future versions:

- Authorized integration with a controlled Active Directory test environment.
- Importing authorized Windows authentication event records.
- More comprehensive account and permission assessment rules.
- Advanced filtering and search functionality.
- Exporting reports in PDF format.
- Historical assessment comparison.
- Role-based dashboard access.
- Additional visual analytics and assessment summaries.
- Configurable risk thresholds.

Any future integration with real systems would require appropriate authorization and security controls.

---

## 19. Conclusion

Nexora Systems demonstrates how Python-based automation and a Streamlit dashboard can be used to assess selected Active Directory security indicators in a controlled simulation environment.

The project brings together four assessment areas: user account security, service account configuration, permissions review, and authentication activity analysis.

By processing synthetic CSV records and applying predefined security rules, the platform identifies potential configuration weaknesses and presents them in structured reports.

The project provides practical exposure to cybersecurity concepts, Python programming, data processing, modular application development, and dashboard design.

Although the current implementation is simulation-based, it establishes a foundation for further learning and future development of authorized security assessment solutions.
