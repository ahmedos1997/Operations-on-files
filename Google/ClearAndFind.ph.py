# سنتعلم هنا طريفة مسح و بحث داخل الورقة
import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


credential = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
file = gspread.authorize(credential)

sheet = file.open('example').sheet1

#تعيد الدالة ()find الخلية الأولى التي تطابق الاستعلام.

cell = sheet.find('Hadi')
print(cell)
#print(f'your search name is in row {cell.row}, and column in {cell.col} ')
#تعيد الدالة ()findall كل الخلايا التي تطابق الاستعلام.
print('-'*100)
cell = sheet.findall('Hadi')
print(cell)
print('-'*100)

# عملية بحث باستخدام التعابير النمطية
emp = re.compile(r'(Anas|Sara)')
cell= sheet.findall(emp)
print(cell)

# مسح البيانات
sheet.batch_clear((['A8:C8']))
# مسح الملف بالكامل

sheet.clear()



