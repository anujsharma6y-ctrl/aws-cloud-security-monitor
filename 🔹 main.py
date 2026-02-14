import argparse
from s3_checker import check_s3
from sg_checker import check_security_groups
from report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="AWS Cloud Security Monitor")
    parser.add_argument("--export", action="store_true", help="Export audit report to JSON")
    args = parser.parse_args()

    findings = []
    findings += check_s3()
    findings += check_security_groups()

    if args.export:
        generate_report(findings)

if __name__ == "__main__":
    main()
