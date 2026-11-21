import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "permissions.csv"
REPORT_FILE = BASE_DIR / "reports" / "permissions_findings.csv"


def to_bool(value):
    return str(value).strip().lower() in ("true", "1", "yes")


def audit_permissions():

    print("\n" + "=" * 55)
    print("NEXORA SYSTEMS - PERMISSIONS AUDITOR")
    print("=" * 55)

    df = pd.read_csv(DATA_FILE)
    findings = []

    for _, record in df.iterrows():

        principal = record["principal"]
        resource = record["resource"]
        permission = str(record["permission"]).strip()
        admin_equivalent = to_bool(record["is_admin_equivalent"])
        justification = str(record["business_justification"]).strip()

        if admin_equivalent and not justification:
            findings.append({
                "principal": principal,
                "resource": resource,
                "finding": "Admin-equivalent permission has no business justification",
                "severity": "High",
                "recommendation": "Review the permission and document its business need"
            })

        if permission.lower() == "fullcontrol" and admin_equivalent:
            findings.append({
                "principal": principal,
                "resource": resource,
                "finding": "Admin-equivalent FullControl permission detected",
                "severity": "High",
                "recommendation": "Apply least-privilege access and review the assignment"
            })

        if permission.lower() == "modify" and admin_equivalent:
            findings.append({
                "principal": principal,
                "resource": resource,
                "finding": "Admin-equivalent Modify permission detected",
                "severity": "Medium",
                "recommendation": "Validate whether elevated modification access is required"
            })

    if findings:

        report = pd.DataFrame(findings)
        REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
        report.to_csv(REPORT_FILE, index=False)

        print("\nPERMISSION FINDINGS")
        print("-" * 55)
        print(report.to_string(index=False))

        print("\nSUMMARY")
        print("-" * 55)
        print("Total Permission Records:", len(df))
        print("Total Findings:", len(report))
        print("\nSeverity Distribution:")
        print(report["severity"].value_counts().to_string())

        print("\nReport saved:", REPORT_FILE)

    else:
        print("\nNo security findings identified.")

    print("\nAudit completed successfully.")


if __name__ == "__main__":
    audit_permissions()