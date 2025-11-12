# 💻 AWS Command Line Interface (CLI) Lab: Enhanced Guide

---

## 🎯 Objective: Mastering S3 Operations with AWS CLI

This comprehensive lab is designed to guide you through the essential steps of configuring the **AWS Command Line Interface (CLI)** and using it to perform fundamental operations on **Amazon Simple Storage Service (S3)**. Upon completion, you will be proficient in:
1.  Securely configuring the AWS CLI with an IAM user's credentials.
2.  Creating a globally unique S3 bucket.
3.  Uploading a local file to the newly created S3 bucket.
4.  Verifying the successful upload using CLI commands.

---

## 🧰 Prerequisites and Security Best Practices

Before proceeding, ensure you have the following in place. **Security Note:** It is a best practice to use an **IAM User** with the principle of least privilege for CLI access, rather than using the root account credentials.

| Prerequisite | Status | Details |
| :--- | :--- | :--- |
| **AWS CLI v2** | Installed | Download and install the latest version from the official AWS documentation [1]. |
| **IAM Credentials** | Available | You must have an **Access Key ID** and **Secret Access Key** for an IAM user with the necessary S3 permissions (e.g., `AmazonS3FullAccess` for this lab). |
| **AWS Account** | Active | Ensure your account is active and you are aware of the Free Tier limits to avoid unexpected charges. |
| **Target File** | Ready | A file (e.g., `Ahmed_Hossam_CV.pdf`) to be uploaded to S3. |

---

## 🪪 Step 1 – Securely Configuring the AWS CLI

The `aws configure` command is the standard method for setting up your credentials and default settings, which are stored in the `~/.aws/credentials` and `~/.aws/config` files.

### 1.1 Execution Command

Open your terminal or command prompt and execute the following command:

```bash
aws configure
```

### 1.2 Input Prompts and Explanation

The CLI will prompt you for four key pieces of information. Enter the values carefully.

| Prompt | Required Input | Professional Explanation |
| :--- | :--- | :--- |
| `AWS Access Key ID [None]:` | Your IAM User's Access Key ID. | This key identifies the user making the request. It is the public part of your credential pair. |
| `AWS Secret Access Key [None]:` | Your IAM User's Secret Access Key. | This key is used to cryptographically sign the request. **Treat this like a password**; it should never be shared or committed to source control. |
| `Default region name [None]:` | Your preferred AWS Region (e.g., `us-east-1`). | This sets the default region for all subsequent commands, meaning you won't have to specify the `--region` flag every time. |
| `Default output format [None]:` | `json` (Recommended). | This defines how the command output is structured. `json` is ideal for scripting and automation, while `text` or `table` are better for human readability. |

### 1.3 Visual Confirmation

The following screenshot illustrates the expected interactive session. **(Note: In a final document, this image should be annotated to highlight where each credential is entered.)**

![AWS CLI Configure Command Output](images/cli-configure.png)

---

## 📦 Step 2 – Creating a Globally Unique S3 Bucket

S3 bucket names are part of a single, global namespace, meaning the name you choose must be unique across all AWS accounts worldwide.

### 2.1 Execution Command

We use the `aws s3 mb` (make bucket) command. You **must** replace `your-unique-bucket-name` with a name that is guaranteed to be unique (e.g., combining your name and a date).

```bash
aws s3 mb s3://your-unique-bucket-name
```

### 2.2 Command Output

A successful creation will confirm the bucket location. If the name is already taken, the CLI will return an error, and you must choose a different name.

![AWS CLI Make Bucket Command Output](images/cli-create-bucket.png)

---

## ⬆️ Step 3 – Uploading a File to S3

The `aws s3 cp` (copy) command is the workhorse for transferring files. It is highly optimized and supports multipart uploads for large files.

### 3.1 Execution Command

The syntax is `aws s3 cp <source> <destination>`. We are copying a local file to the S3 bucket.

```bash
aws s3 cp Ahmed_Hossam_CV.pdf s3://your-unique-bucket-name/
```

### 3.2 Command Explanation

*   `Ahmed_Hossam_CV.pdf`: The local path to the file. (Ensure you are in the directory containing this file, or use the full path).
*   `s3://your-unique-bucket-name/`: The destination S3 URI. The trailing slash indicates that the file should be placed inside the bucket, maintaining its original filename.

### 3.3 Visual Confirmation

The output will display the upload progress and a final confirmation of the file transfer.

![AWS CLI Copy Command Output](images/cli-upload-cv.png)

---

## 🔍 Step 4 – Verifying the Upload and Listing Contents

It is crucial to verify the operation. The `aws s3 ls` (list) command allows you to inspect the contents of your bucket.

### 4.1 Execution Command

```bash
aws s3 ls s3://your-unique-bucket-name/
```

### 4.2 Command Output

The output will list all objects in the bucket, including the date/time of upload, size, and the object key (filename).

![AWS CLI List Bucket Command Output](images/cli-list-bucket-after-upload.png)

---

## ✅ Conclusion and Next Steps

You have successfully executed a complete AWS CLI workflow for S3, from configuration to verification.

### Key Takeaways:
*   The `aws configure` command is essential for initial setup.
*   S3 bucket names are globally unique.
*   The `aws s3 cp` command is used for file transfers.
*   The `aws s3 ls` command is used for verification.

### Further Exploration:
*   **Cleanup:** Use `aws s3 rm s3://your-unique-bucket-name/Ahmed_Hossam_CV.pdf` to delete the file, and `aws s3 rb s3://your-unique-bucket-name` to remove the bucket.
*   **Sync:** Explore `aws s3 sync` for synchronizing entire directories between your local machine and S3.

***

### References
[1] AWS Documentation. *Installing, updating, and uninstalling the AWS CLI version 2*. [https://docs.aws.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
