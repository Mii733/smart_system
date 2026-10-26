# Smart System — Dynamic Low-Code Table & Schema Builder
### نظام إدارة وبناء الجداول والنماذج الديناميكية

[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL%20%7C%20SQLite-blue.svg)](https://www.postgresql.org/)
[![Security Hardened](https://img.shields.io/badge/Security-Hardened%20%26%20Sanitized-brightgreen.svg)](#security--architecture)
[![Author](https://img.shields.io/badge/Author-Eng.%20Moatasem%20Alasi-orange.svg)](https://github.com/EngMoatasemAlasi)

---

## 📌 نبذة عن المشروع (Overview)

**Smart System (Table Builder)** هو نظام ويب متكامل ومتقدم مبني باستخدام **Django** و **PostgreSQL** يُمكّن المؤسسات والمستخدمين من إنشاء وتخصيص قواعد بيانات ونماذج ديناميكية (**Low-Code / No-Code Table Builder**) من خلال واجهة المستخدم الرسومية مباشرة دون الحاجة لكتابة كود برمجي.

النظام يتيح للمدير أو المستخدم بناء جداول مخصصة، تحديد أنواع الحقول، إنشاء العلاقات بين الجداول (Foreign Keys / Many-to-One)، وتوليد شاشات الإدخال والتقارير وتصديرها بصيغ متعددة (Excel / PDF).

---

## ✨ المميزات الرئيسية (Key Features)

* **منشئ الجداول الديناميكية (Dynamic Table Builder):** إنشاء جداول قواعد البيانات وتخصيص المخططات (Schemas) لحظياً عبر واجهة رسومية سهلة.
* **إدارة الحقول والعلاقات (Fields & Relational Modeling):**
  * دعم أنواع متعددة من الحقول (نصوص، أرقام، تواريخ، قوائم اختيار، ملفات).
  * ربط الجداول ببعضها بعلاقات أطراف إلى واحد (Foreign Keys) مع قيود التكامل المرجعي.
* **توليد النماذج التلقائي (Dynamic Forms & Formsets):** إنشاء واجهات إدخال وتعديل البيانات آلياً بناءً على هيكلية الحقول المعرفة.
* **نظام الصلاحيات والأمان (Role-Based Access Control):** إدارة المستخدمين، الأدوار، وصلاحيات الوصول لكل جدول أو نموذج.
* **محرك التقارير وتصدير البيانات (Reports & Data Export):** استعلام البيانات المخصصة، الفلترة المتقدمة، وتصدير التقارير إلى ملفات Excel عبر `pandas` و `openpyxl`.
* **الأمان والحماية المعمارية (Security Hardened):**
  * حماية استعلامات الـ DDL من هجمات حقن التعليمات البرمجية (SQL Injection Prevention).
  * عزل البيانات الحساسة عبر متغيرات البيئة (`.env`).
  * مدقق أسماء المعرفات والتطهير التلقائي (Identifier Sanitizer).

---

## 🏗️ البنية المعمارية (Architecture)

```text
smart_system/
├── table_builder/               # مجلد مشروع Django الأساسي
│   ├── table_builder/           # إعدادات المشروع (Settings, URLs, WSGI)
│   ├── dynmic_table/            # التطبيق الأساسي لإدارة وتوليد الجداول والنماذج
│   │   ├── models.py            # نماذج إدارة المخططات والجداول
│   │   ├── views.py             # المتحكمات والمنطق البرمجي
│   │   ├── forms.py             # النماذج الديناميكية ومجموعات النماذج
│   │   ├── validators.py        # محرك الفحص الأمني ومنع SQL Injection
│   │   └── tests.py             # اختبارات الوحدة الآلية والأمان
│   ├── users/                   # تطبيق إدارة المستخدمين والمصادقة
│   ├── templates/               # قوالب الواجهات الأمامية (HTML/Bootstrap)
│   ├── static/                  # ملفات الأنماط والتنسيق والجافاسكريبت
│   └── manage.py                # أداة إدارة Django
├── .env.example                 # نموذج إعدادات البيئة
├── .gitignore                   # استبعاد الملفات الثنائية والبيئات المؤقتة
├── requirements.txt             # حزم ومكتبات بايثون المطلوبة
└── README.md                    # التوثيق الرسمي
```

---

## 🚀 متطلبات التثبيت والتشغيل (Quick Start)

### 1. استنساخ المستودع (Clone the Repository)

```bash
git clone https://github.com/EngMoatasemAlasi/smart_system.git
cd smart_system
```

### 2. إنشاء وتفعيل البيئة الافتراضية (Virtual Environment)

```bash
# إنشاء البيئة الافتراضية
python -m venv .venv

# تفعيل البيئة (Windows)
.venv\Scripts\activate

# تفعيل البيئة (Linux / macOS)
source .venv/bin/activate
```

### 3. تثبيت الاعتماديات (Install Dependencies)

```bash
pip install -r requirements.txt
```

### 4. ضبط إعدادات البيئة (Environment Setup)

قم بنسخ ملف الإعدادات التجريبي `.env.example` إلى `.env`:

```bash
copy .env.example table_builder\.env
```

ثم قم بتعديل ملف `.env` وفقاً لبيانات قاعدة البيانات الخاصة بك:

```env
SECRET_KEY=your-secure-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# قاعدة البيانات (PostgreSQL)
USE_SQLITE=False
DB_ENGINE=django.db.backends.postgresql
DB_NAME=s19
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

> **ملاحظة:** يمكنك تفعيل `USE_SQLITE=True` لتجربة النظام محلياً بسرعة دون الحاجة لخادم PostgreSQL.

### 5. تطبيق الترحيلات وتشغيل الخادم (Migrate & Run)

```bash
cd table_builder
python manage.py migrate
python manage.py runserver
```

افتح المتصفح على: `http://127.0.0.1:8000/`

---

## 🧪 الاختبارات وضمان الجودة (Tests & Security Verification)

لتشغيل حزمة اختبارات الأمان ومدققات المعرفات:

```bash
cd table_builder
python manage.py test dynmic_table
```

أو تشغيلها مباشرة عبر Python:

```bash
python -c "import sys; sys.path.insert(0, 'table_builder'); import unittest; suite = unittest.defaultTestLoader.loadTestsFromName('dynmic_table.tests'); runner = unittest.TextTestRunner(); res = runner.run(suite); sys.exit(0 if res.wasSuccessful() else 1)"
```

---

## 🛡️ الأمان وضبط الإنتاج (Security Guidelines)

* **SECRET_KEY:** لا تقم بتضمين المفتاح الحقيقي في Git أبداً. يتم تحميله دائماً من `.env`.
* **DEBUG:** يجب ضبط `DJANGO_DEBUG=False` عند الرفع لخادم الإنتاج.
* **SQL Identifiers:** يتم فحص وتطهير أسماء الجداول والحقول لمنع أي محاولات لحقن SQL في أوامر DDL.

---

## 👨‍💻 المطور (Author)

* **المهندس معتصم العاصي (Eng. Moatasem Alasi)**
* GitHub: [@EngMoatasemAlasi](https://github.com/EngMoatasemAlasi)

---

## 📄 الترخيص (License)

هذا المشروع متاح للاستخدام وفقاً لرخصة الاستخدام الخاص بمطوره.
