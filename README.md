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
📂 Project Structure
Each project is organized into its own directory for modularity:

aws-cloud-security-monitor/
│
├── main.py
├── s3_checker.py
├── sg_checker.py
├── report_generator.py
├── requirements.txt
└── README.md
🛠️ Tech Stack
Language: Python 3.8+
## ⚖️ License & Legal Information

This project is primarily licensed under the **MIT License**, with specific modules covered under **Apache 2.0** and **GPL v3**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-red.svg)](./LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

### Key Permissions:
- ✅ **Commercial Use:** You can use this code for business purposes.
- ✅ **Modification:** You can change the code however you like.
- ✅ **Distribution:** You can share the code with others.
- ✅ **Private Use:** You can use it privately.

### Conditions:
- ⚠️ **Notice:** You must include the original copyright and license notice in any copy of the software/source code.

### Warranty:
- 🛡️ **No Warranty:** The software is provided "as is", without any warranty of any kind. The author is not liable for any claims or damages.

**For more details, view the [Full LICENSE File](./LICENSE)**
👨‍💻 Author
Anuj Sharma Cloud Security Automation Enthusiast | IT Automation Specialist | Python for SecOps
