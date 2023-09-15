# طريقة التعامل مع ملفات جوجل



import gspread
from oauth2client.service_account import ServiceAccountCredentials

# انشءنا روابط وهي روابط تتيح فتح و قرائة و الكتابة على ملف جوجل


scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


# المفاتيح التي نحتاجها
credential = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)         #   تعيد الدالة ()from_json_keyfile_name كائن بيانات اعتماديات تم إنشاؤه من ملف المفتاح keyfile.


# سنكتب بعد ذلك اذن الوصول

file = gspread.authorize(credential)         #تستخدم الدالة ()authorize لتسجيل الدخول إلى Google API باستخدام بيانات اعتماد OAuth2.


# الان لنفتح الملف
sheet = file.open("test").sheet1


sheet.update_cell(2,1, 'heloo world')        # تستخدم الدالة ()update_cell لتحديث قيم خلايا جدول البيانات.




