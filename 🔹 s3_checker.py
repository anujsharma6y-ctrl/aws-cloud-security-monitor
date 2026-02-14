import boto3
from colorama import Fore, Style

def check_s3():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    findings = []

    print("\n=== S3 Public Bucket Check ===")
    for bucket in buckets:
        name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            public = any("AllUsers" in str(grant) for grant in acl['Grants'])
            if public:
                print(f"{Fore.RED}[HIGH] Public bucket: {name}{Style.RESET_ALL}")
                findings.append({"type": "S3", "bucket": name, "risk": "HIGH"})
            else:
                print(f"{Fore.GREEN}[LOW] {name} safe{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}Error checking bucket {name}: {e}{Style.RESET_ALL}")
    return findings
