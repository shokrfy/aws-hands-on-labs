# 🖥️ AWS Management Console Lab / تجربة واجهة AWS

## الهدف / Objective
إنشاء S3 bucket ورفع ملف واختبار الإعدادات عبر واجهة الويب (Console).

## الخطوات (Step-by-step)
1. سجل دخولك في https://aws.amazon.com/console/  
2. افتح خدمة **S3**.  
3. اضغط **Create bucket**.
   - **Bucket name:** `ahmed-demo-bucket`
   - **Region:** `eu-central-1` (Frankfurt) — مثال
   - الإعدادات الافتراضية جيدة للبدء (تأكد من إعدادات الـ public access حسب الحاجة).
4. افتح الـ bucket و]اضغط Upload > Add files] ثم اختر `test.txt` ثم Upload.
5. تحقق من وجود الملف في قائمة الـ Objects.

## Screenshots / لقطات شاشة
ضع لقطاتك هنا داخل مجلد `images/`، ثم اربطها هنا بالشكل التالي:
```markdown
![Console - Create bucket](../images/console-create-bucket-1.png)
![Console - Upload file](../images/console-upload-1.png)
```

## Verification / التحقق
- افتح الملف من الـ Console وتأكد من المحتوى أو الخصائص (مثلاً Last modified).
- ضع لقطات شاشة للخطوات (Create, Upload, Object listing).

## AWS Docs reference
https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
