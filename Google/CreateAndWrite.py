import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


credential = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
file = gspread.authorize(credential)
# انشاء ملف جديد
# يجب عمل مشاركة للملف عن طريق الدالة شير الى البريد الالكتروني المسجل
# ينقسم كود المشاركة الى ثلاثة 1- اسم الملف 2- perm_type وهي نوع البريد الالكتروني 3- role هي الصلاحية التي سنعطيها لصاحب هذا البريد الالكتروني
# و تتقم هذه الصلاحيات الى الاتي:1-owner - writer - reader
#new_file = file.create('new test')
# نعمل مشاركة
#new_file.share('ahmedelmadani1997@gmail.com', perm_type='user', role='writer')
# تم  غلق المثالين لانه سيقوم بانشاء ملف في كل مرة
# فتح الملف

new_file = file.open('new test')

# انشاء شيت جديد
#worksheet = new_file.add_worksheet(title='sheet2', rows='100', cols='20')

# اغلقنا المثال السابق لتكملة التمثال
worksheet = new_file.worksheet('Sheet1')
# يمكن الاضافة للخلية عن طريقتين الاولى و هي مكان الخلية بالاحرف
worksheet.update('B1','heloo ahmed')
# والثانية مكان الخلية بتحديد الصفوف و الاعمدة

worksheet.update_cell(2,4 , 'hello mohamed')
#يمكن ضبط قيمة خلية أو عدة خلايا من خلال الدالة ()update.
worksheet.update('A1:C2', [['ahmed',100,'21/5/1997'],['mohammed',250,'15/1/1997']])

# في المثال اعلاه ادخلنا البيانات علي شكل مجموعات

