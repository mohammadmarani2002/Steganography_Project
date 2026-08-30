# 🖼️ Steganography Project (LSB)

## 📌 معرفی
این پروژه با استفاده از روش **LSB (Least Significant Bit)**، قابلیت مخفی‌سازی **متن و تصویر** درون تصاویر رو فراهم می‌کنه.  
رابط کاربری با **Streamlit** ساخته شده و کاربر می‌تونه به‌راحتی داده‌های مخفی رو در تصویر ذخیره یا استخراج کنه.

## 🛠️ تکنولوژی‌های استفاده‌شده
- Python 3.10+
- Streamlit
- Stegano (کتابخونه‌ی LSB)
- Pillow (PIL)
- NumPy

## 📂 ساختار پروژه


steganography_project/
│
├── app_01.py                 # مخفی‌سازی و استخراج متن
├── app_02.py                 # مخفی‌سازی و استخراج تصویر در تصویر
├── app_hide_json.py          # مخفی‌سازی فایل JSON در تصویر
├── encode_decode_example.py  # مثال‌های کدگذاری
├── requirements.txt          # لیست کتابخونه‌ها
└── final_secret.png          # تصویر نهایی (تولیدشده)



## 🚀 نصب و اجرا


bash
# ۱. کلون کردن پروژه
git clone https://github.com/mohammadmarani2002/steganography_project.git
cd steganography_project

# ۲. ایجاد محیط مجازی
python -m venv venv
source venv/bin/activate  # برای لینوکس/مک
.\venv\Scripts\activate   # برای ویندوز

# ۳. نصب کتابخونه‌ها
pip install -r requirements.txt

# ۴. اجرا (مثال)
streamlit run app_01.py


📸 نمونه خروجی

(اسکرین‌شات به‌زودی اضافه می‌شود)

👨‍💻 نویسنده

محمد مرانی
                                                                                                      https://github.com/mohammadmarani2002

📝 نکات

· تصاویر خروجی با فرمت PNG ذخیره می‌شوند تا کیفیت حفظ شود.
· برای مخفی‌سازی تصویر در تصویر، از کدگذاری latin-1 استفاده شده است.
· فرمت‌های پشتیبانی‌شده: PNG, JPG, JPEG.
· امکان بررسی کیفیت تصویر بعد از مخفی‌سازی (گام ۶ تمرین) فراهم است.
