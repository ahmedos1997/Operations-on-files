# طريقة التعامل مع ملفات جوجل

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


credential = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
file = gspread.authorize(credential)         #تستخدم الدالة ()authorize لتسجيل الدخول إلى Google API باستخدام بيانات اعتماد OAuth2.
# الان لنفتح الملف
sheet = file.open("example")
# هناك طريقة اخرى لفتح الملف عن طريق اليو ار ال

#sheet = file.open_by_url("https://docs.google.com/spreadsheets/d/1pKpbd-AhWfq6XtSp1Umvj5a0N8Kw1NZI4YqCtGILWIg/edit?usp=share_link").sheet1

# طرق تحديد الورق التي نريد القراءة منها وتوجد عدة طرق
# الطريقة الاولى عن طريق تحديد index

#worksheet = sheet.get_worksheet(0)
# الطريقة الثانية عن طريق اسم الورقة
worksheet = sheet.worksheet('sheet1')

# طباعة جميع اسماء الاوراق في الملف
worksheet_list = sheet.worksheets()
print(worksheet_list)

# القراءة من الملف

val = worksheet.acell('B1').value

print(val)

val = worksheet.acell('A5').value
print(val)

# نقرا من الملف بالستخدام الدالة cell لتحديد الصفوف و الاعمدة


val = worksheet.cell(5,1).value
print(val)

# الان سنطبع بالعامود كامل او الصف كامل

val_list = worksheet.row_values(2)
print(val_list)

val_list = worksheet.col_values(1)
print(val_list)

#  لطباعة جميع البيانات التي داخل الورقة وتطبعه على شكل مجموعات
listoflists = worksheet.get_all_values()
print(listoflists)

#  لطباعة جميع البيانات التي داخل الورقة وتطبعه على شكل سجلات


listofdic = worksheet.get_all_records()
print(listofdic)



