# العمليات على المفات المضغوطة
import os
import zipfile
from pathlib import Path



# تم ايقاف المثال لاستكمال الدرس
'''
compzip = zipfile.ZipFile(Path.home() / Path('Desktop','New folder.zip'))
# لطباعة اسماء الملفات داخل المجلد المضغوط
print(compzip.namelist())

# لمعرفة بيانات ملف معين داخل المجلد المضغوط

fileinfo = compzip.getinfo('New folder/new file.txt')
print(fileinfo.file_size)   # حجم الملف قبل الضغط
print(fileinfo.compress_size) # عرض حجم الملف بعد الضغط

print('------------------------------------------------------------------------------')
# extract
# تستخدم لفك الملفات المضغوظة
os.chdir(Path.home() / Path('Desktop')) #  قمنا بتحديد مكان فك الضغط
compzip.extractall()                    # فك الضغط
print('______________________________________________________________________________')
# يمكن تحديد ملف معين لاستخراجه من المجلد المضغوط
compzip.extract(('New folder/new file.txt'),Path.home() / Path('Desktop','khkh'))
print('______________________________________________________________________________')
'''
# compress file
# سنتعلم عملية ضغط الملفات

#newzip = zipfile.ZipFile('new.zip', 'w')
#newzip.write('New folder/new file.txt')

# compress folder
# ضغط المجلدات
zipp = zipfile.ZipFile('newnew.zip', 'w')
zipp.write(Path.home() / Path('Desktop','New folder'))
# الرجاء اكمال التمرين لانه لا يعمل بطريقة جيدة





