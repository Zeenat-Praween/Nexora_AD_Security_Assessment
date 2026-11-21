import streamlit as st
import pandas as pd
from pathlib import Path
import base64
from modules.user_security_audit import audit_users
from modules.service_account_audit import audit_service_accounts
from modules.permissions_audit import audit_permissions
from modules.authentication_analyzer import analyze_authentication


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="NEXORA SYSTEMS | Security Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "reports"

BACKGROUND_IMAGE = BASE_DIR / "assets" / "nexora_background.jpg"

encoded_image = base64.b64encode(
    BACKGROUND_IMAGE.read_bytes()
).decode("utf-8")

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image:
            linear-gradient(
                rgba(5, 13, 30, 0.25),
                rgba(5, 13, 30, 0.35)
            ),
            url("data:image/jpeg;base64,{encoded_image}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)




# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        linear-gradient(
            rgba(5, 13, 30, 0.82),
            rgba(5, 13, 30, 0.88)
        ),
        url("assets/nexora_background.jpg");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;

    color: #ffffff;
}
/* Hide Streamlit branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main Heading */

.hero {
    text-align: center;
    padding: 45px 15px 30px 15px;
}

.hero h1 {
    font-size: 65px;
    font-weight: 1000;
    letter-spacing: 8px;
    color: #F0D58C;
    margin-bottom: 5px;
    text-shadow: 0px 0px 22px rgba(66, 232, 245, 0.4);
}

.hero h3 {
    font-size: 31px;
    font-weight: 900;
    color: #F5F0E6;
    letter-spacing: 4px;
}

.hero p {
    color: #FFFFFF;
    font-size: 26px;
}

/* Section Heading */

.section-heading {
    color: #42e8f5;
    font-size: 25px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 20px;
}

/* Cards */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(66,232,245,0.25);
    border-radius: 16px;
    padding: 18px;
}

/* Buttons */

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #087fbd, #12c6d6);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-weight: 800;
    font-size: 15px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #12c6d6, #087fbd);
    color: white;
    border: 1px solid #42e8f5;
    transform: scale(1.02);
}

/* Report Tables */

div[data-testid="stDataFrame"] {
    border: 1px solid #42e8f5;
    border-radius: 10px;
}

/* Download Buttons */

.stDownloadButton > button {
    background: #172b49;
    color: #42e8f5;
    border: 1px solid #42e8f5;
    border-radius: 8px;
    font-weight: 700;
}

/* Footer */

.footer {
    text-align: center;
    color: #8fa8c8;
    padding: 30px 10px;
    font-size: 30px;
}

/* Generated Reports - Expander Styling */

div[data-testid="stExpander"] {
    background-color: #142944 !important;
    border: 1px solid #42e8f5 !important;
    border-radius: 12px !important;
}

div[data-testid="stExpander"] details summary {
    color: #42e8f5 !important;
    font-weight: 800 !important;
    background-color: #142944 !important;
}

div[data-testid="stExpander"] details summary p {
    color: #42e8f5 !important;
    font-weight: 800 !important;
}

div[data-testid="stExpander"] details summary:hover {
    background-color: #203d5e !important;
}

div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {
    background-color: #142944 !important;
    color: #ffffff !important;
}



</style>
""", unsafe_allow_html=True)


# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="hero">
    <h1>🛡️ NEXORA SYSTEMS</h1>
    <h3>SECURE. ASSESS. DETECT. DEFEND.</h3>
    <p>
        Active Directory Security Assessment
        &amp; Threat Detection Platform
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- PROJECT INFORMATION ----------------

st.markdown("""
<div style="
    background:rgba(66,232,245,0.08);
    border-left:7px solid #42e8f5;
    padding:20px;
    border-radius:15px;
    margin-bottom:28px;
">

<b style="color:#42e8f5;">ABOUT NEXORA</b>

<p style="color:#F5F0E6; margin-bottom:0;
 font-size:18px;">
Nexora Systems is a simulation-based security assessment
platform designed to identify potential Active Directory
security weaknesses, analyze authentication patterns,
review account permissions, and generate security reports.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    """
    <div style="
        font-size: 19px;
        font-weight: 400;
        color: #C0C0C0;
        margin: 0;
    ">
        <strong>Simulation Environment:</strong>
        This platform uses synthetic security records and does not
        connect to a live Active Directory domain.
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- SECURITY ASSESSMENT MODULES ----------------

def display_findings(filename):

    file_path = REPORT_DIR / filename

    if file_path.exists():

        findings = pd.read_csv(file_path)

        st.markdown("#### 📋 Audit Findings")

        st.metric("Total Findings", len(findings))

        if findings.empty:

            st.success("No security findings detected.")

        else:

            styled_findings = (
                findings.style
                .set_properties(**{
                    "background-color": "#101F35",
                    "color": "#D5E3F5",
                    "border": "1px solid #8C6A35",
                    "font-size": "14px",
                    "padding": "10px"
                })
                .set_table_styles([
                    {
                        "selector": "th",
                        "props": [
                            ("background-color", "#F0D58C"),
                            ("color", "#081225"),
                            ("font-weight", "bold"),
                            ("border", "1px solid #8C6A35"),
                            ("text-align", "center"),
                            ("padding", "12px")
                        ]
                    },
                    {
                        "selector": "td",
                        "props": [
                            ("border", "1px solid #8C6A35"),
                            ("text-align", "left")
                        ]
                    }
                ])
            )

            st.markdown(
                styled_findings.to_html(),
                unsafe_allow_html=True
            )

    else:

        st.warning(
            "Report file was not generated. "
            "Please check the audit module."
        )
        

st.markdown(
    '<div class="section-heading">⚡ SECURITY ASSESSMENT MODULES</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    with st.container(border=True):

        st.markdown("### 👤 User Security Audit")

        st.write(
            "Identifies weak account configurations, "
            "missing MFA, and password policy concerns."
        )

        if st.button("▶ RUN USER AUDIT", key="user"):

            with st.spinner("Analyzing user security..."):
                audit_users()

            st.success("User security audit completed!")


    with st.container(border=True):

        st.markdown("### ⚙️ Service Account Audit")

        st.write(
            "Reviews service account configurations, "
            "password age, ownership, and privileges."
        )

        if st.button("▶ RUN SERVICE ACCOUNT AUDIT", key="service"):

            with st.spinner("Analyzing service accounts..."):
                audit_service_accounts()

            st.success("Service account audit completed!")


with col2:

    with st.container(border=True):

        st.markdown("### 🔐 Permissions Audit")

        st.write(
            "Identifies potentially excessive permissions "
            "and reviews access control assignments."
        )

        if st.button("▶ RUN PERMISSIONS AUDIT", key="permissions"):

            with st.spinner("Reviewing permissions..."):
                audit_permissions()

            st.success("Permissions audit completed!")


    with st.container(border=True):

        st.markdown("### 📊 Authentication Analysis")

        st.write(
            "Detects repeated failed logins, unusual login "
            "times, and suspicious authentication patterns."
        )

        if st.button("▶ ANALYZE AUTHENTICATION", key="authentication"):

            with st.spinner("Analyzing authentication events..."):
                analyze_authentication()

            st.success("Authentication analysis completed!")
            

# ---------------- SECURITY REPORTS ----------------

st.divider()

st.markdown(
    '<div class="section-heading">📁 GENERATED SECURITY REPORTS</div>',
    unsafe_allow_html=True
)

report_files = {
    "👤 User Security Findings": "user_security_findings.csv",
    "⚙️ Service Account Findings": "service_account_findings.csv",
    "🔐 Permissions Findings": "permissions_findings.csv",
    "📊 Authentication Findings": "authentication_findings.csv"
}

for title, filename in report_files.items():

    file_path = REPORT_DIR / filename

    if file_path.exists():

        report_df = pd.read_csv(file_path)

        with st.expander(title, expanded=False):

            st.write("Total Findings:", len(report_df))

            styled_report = (
    report_df.style
    .set_properties(**{
        "background-color": "#142944",
        "color": "#FFFFFF",
        "font-weight": "bold",
        "font-size": "14px",
        "border": "1px solid #315574",
        "text-align": "left"
    })
    .set_table_styles([
        {
            "selector": "th.col_heading",
            "props": [
                ("background-color", "#42E8F5"),
                ("color", "#000000"),
                ("font-weight", "900"),
                ("font-size", "15px"),
                ("border", "1px solid #315574"),
                ("text-align", "center")
            ]
        }
    ])
    .hide(axis="index")
)

            st.markdown(
    styled_report.to_html(),
    unsafe_allow_html=True
)

            st.download_button(
                label="⬇ DOWNLOAD REPORT",
                data=file_path.read_bytes(),
                file_name=filename,
                mime="text/csv",
                key=filename
            )

    else:

        st.warning(
            f"{title}: Run the corresponding audit to generate this report."
        )

#------------FOOTER---------------------#        

st.markdown(
    "<div style='text-align:center; color:#D4AF37; font-size:24px;'>"
    "Active Directory Security Assessment &amp; Threat Detection"
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='text-align:center; color:Hex Code	Colour:#C0C0C0; font-size:18px;'>"
    "Developed for Cybersecurity Research and Educational Simulation"
    "<br>© 2026 | All Rights Reserved"
    "</div>",
    unsafe_allow_html=True
)