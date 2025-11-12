# 🐍 AWS SDK (Python - Boto3) Lab / تجربة بايثون Boto3

## الهدف / Objective
استخدام Boto3 للتعامل برمجياً مع S3: استعراض البكتس، رفع ملف، وتحميل ملف.

## الإعداد (Setup)
```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .\.venv\Scripts\activate
pip install boto3
```

تأكد أن بيانات الاعتماد معرفة في `~/.aws/credentials` أو استخدم boto3 session.

## مثال كود (Code example)
```python
import boto3

s3 = boto3.client('s3')
# List buckets
response = s3.list_buckets()
print('Buckets:')
for b in response['Buckets']:
    print(' -', b['Name'])

# Upload file
s3.upload_file('test.txt', 'ahmed-sdk-bucket', 'test.txt')
print('Uploaded test.txt to ahmed-sdk-bucket')
```

## Screenshots / لقطات شاشة
ضع صورة لمخرج الكود في الترمينال `images/sdk-list-buckets.png`

## AWS Docs reference
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
