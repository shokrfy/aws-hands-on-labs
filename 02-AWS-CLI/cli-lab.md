# 💻 AWS Command Line Interface (CLI) Lab

---

## 🎯 Objective
This lab demonstrates how to use the **AWS Command Line Interface (CLI)** to interact with **Amazon S3**.  
By the end of this lab, you will have successfully configured the AWS CLI, created a new S3 bucket, uploaded a file, and verified the upload using CLI commands.

---

## 🧰 Prerequisites

Before running any commands, ensure that:
- AWS CLI v2 is installed ✅  
- You have your **Access Key ID** and **Secret Access Key** for an IAM user with S3 permissions ✅  
- Your AWS account is active and within the Free Tier limits ✅  

If not installed, download the CLI from: [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

---

## 🪪 Step 1 – Configure AWS CLI

### 🧩 Description
To allow the CLI to connect to your AWS account, you must configure it with your credentials. This process securely stores your Access Key ID and Secret Access Key.

### ⚙️ Command
```bash
aws configure
```

### 📸 Screenshot
After running the command, you will be prompted to enter four pieces of information.

![AWS CLI Configure Command Output](images/cli-configure.png)

| Prompt | Input |
| :--- | :--- |
| `AWS Access Key ID [None]:` | Paste your Access Key ID |
| `AWS Secret Access Key [None]:` | Paste your Secret Access Key |
| `Default region name [None]:` | Enter your preferred AWS region (e.g., `us-east-1`) |
| `Default output format [None]:` | Enter `json` (recommended) |

---

## 📦 Step 2 – Create an S3 Bucket

### 🧩 Description
Amazon S3 bucket names must be globally unique. We will use the `aws s3 mb` (make bucket) command to create a new bucket.

### ⚙️ Command
Replace `your-unique-bucket-name` with a globally unique name.

```bash
aws s3 mb s3://your-unique-bucket-name
```

### 📸 Screenshot
A successful operation will return a confirmation message.

![AWS CLI Make Bucket Command Output](images/cli-create-bucket.png)

---

## ⬆️ Step 3 – Upload a File to the S3 Bucket

### 🧩 Description
The `aws s3 cp` (copy) command is used to upload files from your local machine to an S3 bucket. Ensure you have a file named `Ahmed_Hossam_CV.pdf` in the root of your repository or update the command path.

### ⚙️ Command
```bash
aws s3 cp Ahmed_Hossam_CV.pdf s3://your-unique-bucket-name/
```

### 📸 Screenshot
The output will show the progress and confirmation of the file transfer.

![AWS CLI Copy Command Output](images/cli-upload-cv.png)

---

## 🔍 Step 4 – Verify the Upload

### 🧩 Description
To confirm the file was successfully uploaded, use the `aws s3 ls` (list) command on the bucket.

### ⚙️ Command
```bash
aws s3 ls s3://your-unique-bucket-name/
```

### 📸 Screenshot
The output will list the contents of the bucket, including the uploaded file.

![AWS CLI List Bucket Command Output](images/cli-list-bucket-after-upload.png)

---

## ✅ Conclusion
You have successfully configured the AWS CLI and used it to perform fundamental S3 operations: creating a bucket, uploading a file, and listing the bucket contents. This demonstrates the power and efficiency of managing AWS resources directly from your command line.
