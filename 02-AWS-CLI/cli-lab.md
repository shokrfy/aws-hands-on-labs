# 💻 AWS CLI Lab / تجربة سطر أوامر AWS

## الهدف / Objective
إعداد AWS CLI، إنشاء S3 bucket، رفع ملف، وعرض محتويات الـ bucket باستخدام أوامر CLI.

## الإعداد (Setup)
1. نزّل وثبّت AWS CLI v2: https://aws.amazon.com/cli/
2. اعدد الـ credentials:
   ```bash
   aws configure
   # أدخل Access Key ID و Secret Access Key (من IAM user)
   # Region: eu-central-1
   # Output: json
   ```

## أوامر أساسية (Commands)
```bash
# قائمة البكتس
aws s3 ls

# انشاء bucket
aws s3 mb s3://ahmed-cli-bucket

# رفع ملف
aws s3 cp test.txt s3://ahmed-cli-bucket/

# عرض الملفات داخل البكت
aws s3 ls s3://ahmed-cli-bucket/
```

## Screenshots / لقطات شاشة
نافذة التيرمنال: احفظ لقطات للشاشة بعد كل أمر مهم و ضعها داخل `images/` مثل:
- `images/cli-aws-config.png`
- `images/cli-upload-output.png`

## AWS Docs reference
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
