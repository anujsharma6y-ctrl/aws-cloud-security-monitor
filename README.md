# AWS Cloud Security Monitor

Early-stage startups often overlook basic AWS misconfigurations.  
This CLI tool detects public S3 buckets and Security Groups open to all IPs.

## Features
- Detect public S3 buckets
- Detect open Security Groups (0.0.0.0/0)
- Risk scoring
- Colored CLI output
- Export JSON audit report

## Requirements
- Python 3
- boto3
- colorama
- AWS CLI credentials configured

## Usage
```bash
pip install -r requirements.txt
python main.py
python main.py --export
