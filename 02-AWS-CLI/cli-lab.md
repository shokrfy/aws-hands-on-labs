# 💻 AWS Command Line Interface (CLI) Lab

---

## 🎯 Objective
This lab demonstrates how to use the **AWS Command Line Interface (CLI)** to interact with **Amazon S3**.  
By the end of this lab, I successfully configured the AWS CLI, created a new S3 bucket, uploaded a resume PDF file, and verified the upload using CLI commands.

---

## 🧰 Prerequisites

Before running any commands, ensure that:
- AWS CLI v2 is installed ✅  
- You have your **Access Key ID** and **Secret Access Key** ✅  
- Your AWS account is active and within the Free Tier limits ✅  

If not installed, download the CLI from: [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

---

## 🪪 Step 1 – Configure AWS CLI

### 🧩 Description
To allow the CLI to connect to my AWS account, I configured it using the command below:

```bash
aws configure
