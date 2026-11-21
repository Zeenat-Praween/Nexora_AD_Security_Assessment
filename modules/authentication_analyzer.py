import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "authentication_events.csv"
REPORT_FILE = BASE_DIR / "reports" / "authentication_findings.csv"


def analyze_authentication():

    print("\n" + "=" * 60)
    print("NEXORA SYSTEMS - AUTHENTICATION EVENT ANALYZER")
    print("=" * 60)

    df = pd.read_csv(DATA_FILE)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    findings = []

    # 1. Detect repeated failed login attempts
    failed_events = df[df["status"].str.lower() == "failed"]

    failed_counts = (
        failed_events.groupby(["username", "source_ip"])
        .size()
        .reset_index(name="failed_attempts")
    )

    for _, record in failed_counts.iterrows():

        if record["failed_attempts"] >= 3:

            findings.append({
                "username": record["username"],
                "source_ip": record["source_ip"],
                "finding": "Repeated failed login attempts",
                "details": f'{record["failed_attempts"]} failed attempts',
                "severity": "High",
                "recommendation": "Review authentication logs and verify account activity"
            })

    # 2. Detect failed login followed by successful login
    for username in df["username"].unique():

        user_events = df[df["username"] == username].sort_values("timestamp")

        for index in range(1, len(user_events)):

            previous = user_events.iloc[index - 1]
            current = user_events.iloc[index]

            if (
                str(previous["status"]).lower() == "failed"
                and str(current["status"]).lower() == "success"
                and previous["source_ip"] == current["source_ip"]
            ):

                findings.append({
                    "username": username,
                    "source_ip": current["source_ip"],
                    "finding": "Successful login after failed login",
                    "details": "A successful login followed a failed attempt",
                    "severity": "Medium",
                    "recommendation": "Review the sequence and confirm legitimate access"
                })

    # 3. Detect late-night login activity
    for _, record in df.iterrows():

        hour = record["timestamp"].hour

        if str(record["status"]).lower() == "success" and (
            hour >= 23 or hour < 5
        ):

            findings.append({
                "username": record["username"],
                "source_ip": record["source_ip"],
                "finding": "Late-night successful login",
                "details": record["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                "severity": "Medium",
                "recommendation": "Verify whether the login matches the user's normal schedule"
            })

    # 4. Detect disabled account login attempts
    disabled_events = df[
        df["failure_reason"].astype(str).str.lower() == "disabled account"
    ]

    for _, record in disabled_events.iterrows():

        findings.append({
            "username": record["username"],
            "source_ip": record["source_ip"],
            "finding": "Login attempt involving a disabled account",
            "details": "Authentication was rejected for a disabled account",
            "severity": "Low",
            "recommendation": "Confirm the account is intentionally disabled"
        })

    if findings:

        report = pd.DataFrame(findings)

        REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
        report.to_csv(REPORT_FILE, index=False)

        print("\nAUTHENTICATION FINDINGS")
        print("-" * 60)
        print(report.to_string(index=False))

        print("\nSUMMARY")
        print("-" * 60)
        print("Total Authentication Events:", len(df))
        print("Total Findings:", len(report))

        print("\nSeverity Distribution:")
        print(report["severity"].value_counts().to_string())

        print("\nReport saved:", REPORT_FILE)

    else:
        print("\nNo suspicious authentication patterns identified.")

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    analyze_authentication()