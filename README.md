# ☁️ AWS Hands-on Labs Documentation / توثيق تجارب AWS العملية

هذا المستودع يحتوي توثيق عملي لتجارب التفاعل مع AWS بثلاث طرق: **Console (واجهة الويب)**، **CLI (سطر الأوامر)**، و**SDK (بايثون - Boto3)**.
This repository contains documentation and hands-on labs demonstrating the three main methods of interacting with AWS.

---

## 🧭 الهدف / Objective
- تجربة وممارسة الطرق الثلاث للتعامل مع AWS (Console, CLI, SDK).  
- توثيق الخطوات والأوامر والكود ولقطات الشاشة لكل تجربة.  
- بناء Portfolio عملي على GitHub.

## 📂 هيكل المجلدات / Repository structure
```text
aws-hands-on-labs/
│
├── README.md
├── .gitignore
├── images/                    # ضع لقطات الشاشة هنا (مثلاً: console-1.png)
├── 01-AWS-Console/
│   └── console-lab.md
├── 02-AWS-CLI/
│   └── cli-lab.md
└── 03-AWS-SDK/
    └── sdk-lab.md
```

## ✅ نصائح للمظهر الاحترافي / Pro tips
- استخدم **صور (screenshots)** لكل خطوة داخل مجلد `images/` وادمجها داخل ملفات الـ Markdown.  
- استخدم جداول، أقسام `Code blocks`، وعناوين واضحة.  
- اربط كل تجربة بروابط رسمية من AWS Docs.  
- حدث README بعد كل تجربة مع قسم تغيير التحديثات (CHANGELOG).

---

## 🧩 Labs Overview (حالة العمل)
| Lab | Description | Status |
|-----|-------------|--------|
| 01-AWS-Console | Create and manage S3 buckets via Console | ✅ Ready (add screenshots) |
| 02-AWS-CLI | Configure CLI, create/upload/list S3 objects | ✅ Ready (add commands output screenshots) |
| 03-AWS-SDK | Boto3 examples to list/upload S3 objects | ✅ Ready (add script output screenshots) |

---

## 🛠️ How to use (كيفية الاستخدام)
1. فك الضغط أو استنساخ الريبو محليًا.  
   ```bash
   git clone https://github.com/<username>/aws-hands-on-labs.git
   cd aws-hands-on-labs
   ```
2. افتح ملف الـ Markdown الخاص بكل تجربة وأضف لقطات الشاشة داخل `images/` ثم أضف روابط الصور داخل الملفات.  
3. أضف commit وادفع التحديثات إلى GitHub:
   ```bash
   git add .
   git commit -m "Add lab documentation and screenshots"
   git push origin main
   ```

---

## 📌 Author / المؤلف
**Ahmed Hossam** — AWS learning & hands-on documentation.

---

## 🔗 Useful Links / روابط مفيدة
- AWS CLI docs: https://docs.aws.amazon.com/cli/
- Boto3 docs: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- AWS Free Tier: https://aws.amazon.com/free
