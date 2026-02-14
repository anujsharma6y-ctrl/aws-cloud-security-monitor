import json

def generate_report(findings):
    with open("cloud_audit_report.json", "w") as f:
        json.dump(findings, f, indent=4)
    print("\nReport exported as cloud_audit_report.json")
