import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "service_accounts.csv"
REPORT_FILE = BASE_DIR / "reports" / "service_account_findings.csv"


def to_bool(value):
    return str(value).strip().lower() in ("true", "1", "yes")


def audit_service_accounts():

    print("\n" + "=" * 55)
    print("NEXORA SYSTEMS - SERVICE ACCOUNT AUDITOR")
    print("=" * 55)

    df = pd.read_csv(DATA_FILE)
    findings = []

    for _, account in df.iterrows():

        username = account["username"]

        spn = to_bool(account["spn_configured"])
        managed = to_bool(account["managed_service_account"])
        privileged = to_bool(account["privileged"])
        owner_defined = to_bool(account["owner_defined"])
        password_age = int(account["password_age_days"])

        if spn and not managed:
            findings.append({
                "username": username,
                "finding": "SPN configured on a non-managed service account",
                "severity": "High",
                "recommendation": "Review the account and consider a managed service account"
            })

        if password_age > 180:
            findings.append({
                "username": username,
                "finding": "Service account password is older than 180 days",
                "severity": "Medium",
                "recommendation": "Review and update the service account password policy"
            })

        if privileged and not owner_defined:
            findings.append({
                "username": username,
                "finding": "Privileged service account has no defined owner",
                "severity": "High",
                "recommendation": "Assign an accountable owner and review privileges"
            })

        if not owner_defined:
            findings.append({
                "username": username,
                "finding": "Service account has no defined owner",
                "severity": "Medium",
                "recommendation": "Assign a responsible account owner"
            })

    if findings:

        report = pd.DataFrame(findings)
        REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
        report.to_csv(REPORT_FILE, index=False)

        print("\nSERVICE ACCOUNT FINDINGS")
        print("-" * 55)
        print(report.to_string(index=False))

        print("\nSUMMARY")
        print("-" * 55)
        print("Total Service Accounts:", len(df))
        print("Total Findings:", len(report))
        print("\nSeverity Distribution:")
        print(report["severity"].value_counts().to_string())

        print("\nReport saved:", REPORT_FILE)

    else:
        print("\nNo security findings identified.")

    print("\nAudit completed successfully.")


if __name__ == "__main__":
    audit_service_accounts()