خلاصهٔ کاری که باید انجام شود: محتوای فایل main.py را کامل با عبارت زیر جایگزین کنم:
a+b+c

محتوای نهایی main.py
--------------------
a+b+c

نحوهٔ اعمال تغییر (در دستگاه شما یا روی سرور CI/CD):
1) کلون کردن مخزن (اگر هنوز کلون نکردید):
   git clone https://github.com/mitrapahlevanzade-lab/mitra-github.git
   cd mitra-github

2) جایگزینی محتوای main.py:
   echo 'a+b+c' > main.py

3) ثبت تغییر و ارسال به گیت‌هاب:
   git add main.py
   git commit -m "Replace main.py content with 'a+b+c'"
   git push origin main

(اگر می‌خواهید این را در یک شاخهٔ جدید و از طریق pull request اعمال کنید، به‌جای مرحلهٔ push:
   git checkout -b update/main-py-to-a-plus-b-plus-c
   git push -u origin update/main-py-to-a-plus-b-plus-c
و سپس یک Pull Request از این شاخه باز کنید.)

اگر مایلید من مستقلاً این تغییر را روی مخزن شما در گیت‌هاب اعمال کنم، توکن دسترسی (Personal Access Token) با مجوز repo یا اجازهٔ دسترسی از طرف شما لازم است — یا می‌توانید دسترسی لازم را از طریق GitHub App/Integration فراهم کنید. بفرمایید که کدام گزینه را ترجیح می‌دهید تا ادامه دهم.