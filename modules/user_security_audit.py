import pandas as pd
from pathlib import Path


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "ad_users.csv"
REPORT_FILE = BASE_DIR / "reports" / "user_security_findings.csv"


def to_bool(value):
    return str(value).strip().lower() in ("true", "1", "yes")


def audit_users():

    print("\n" + "=" * 55)
    print("NEXORA SYSTEMS - USER SECURITY AUDITOR")
    print("=" * 55)

    # Load dataset
    df = pd.read_csv(DATA_FILE)

    findings = []

    for _, user in df.iterrows():

        username = user["username"]

        enabled = to_bool(user["enabled"])
        privileged = to_bool(user["privileged"])
        password_never_expires = to_bool(
            user["password_never_expires"]
        )
        mfa_enabled = to_bool(user["mfa_enabled"])

        password_age = int(user["last_password_change_days"])

        # Check 1: Privileged account without MFA
        if privileged and not mfa_enabled:

            findings.append({
                "username": username,
                "finding": "Privileged account without MFA",
                "severity": "High",
                "recommendation": "Review privileged account and enforce MFA"
            })

        # Check 2: Password never expires
        if password_never_expires:

            findings.append({
                "username": username,
                "finding": "Password never expires policy enabled",
                "severity": "Medium",
                "recommendation": "Review password expiration policy"
            })

        # Check 3: Old password
        if password_age > 90:

            findings.append({
                "username": username,
                "finding": "Password age exceeds 90 days",
                "severity": "Medium",
                "recommendation": "Review password security policy"
            })

        # Check 4: Standard account without MFA
        if enabled and not privileged and not mfa_enabled:

            findings.append({
                "username": username,
                "finding": "Standard account without MFA",
                "severity": "Medium",
                "recommendation": "Evaluate MFA deployment"
            })

        # Check 5: Disabled account review
        if not enabled:

            findings.append({
                "username": username,
                "finding": "Disabled account requires review",
                "severity": "Low",
                "recommendation": "Verify account deactivation and retention"
            })

    # Generate report
    if findings:

        report = pd.DataFrame(findings)

        REPORT_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        report.to_csv(REPORT_FILE, index=False)

        print("\nUSER SECURITY FINDINGS")
        print("-" * 55)

        print(report.to_string(index=False))

        print("\nSUMMARY")
        print("-" * 55)

        print("Total Users:", len(df))
        print("Total Findings:", len(report))

        print("\nSeverity Distribution:")

        print(
            report["severity"]
            .value_counts()
            .to_string()
        )

        print("\nReport saved successfully:")
        print(REPORT_FILE)

    else:

        print("\nNo security findings identified.")

    print("\nAudit completed successfully.")


if __name__ == "__main__":
    audit_users()