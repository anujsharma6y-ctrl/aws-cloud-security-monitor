import boto3
from colorama import Fore, Style

def check_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    findings = []

    print("\n=== Security Group Exposure Check ===")
    for sg in response['SecurityGroups']:
        for perm in sg['IpPermissions']:
            from_port = perm.get('FromPort')
            ip_ranges = perm.get('IpRanges', [])
            for ip_range in ip_ranges:
                cidr = ip_range.get('CidrIp')
                if cidr == "0.0.0.0/0":
                    print(f"{Fore.RED}[HIGH] SG {sg['GroupName']} open on port {from_port}{Style.RESET_ALL}")
                    findings.append({"type": "SecurityGroup", "sg": sg['GroupName'], "port": from_port, "risk": "HIGH"})
    return findings
