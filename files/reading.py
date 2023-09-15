# سنتعلم كيفية فتح الملف
# نكتب المسار ثم نحدد لماذا نريد فتح الملف و هنالك اربعة انواع
# الحرف a اختصار ل apped ويستخدم للاضافة على الملف
#الحرف r للقرائة من الملف
#  الحرف w اختصار ل write للكتابة على الملف
# الحرف x ويستخدم لإنشاء ملف
# في الدالة open لو لم نحدد الغرض م فتح الملف فسيكون الملف في وضع القراءة

from pathlib import Path
import os
#openf = (r'D:\كورس بايثون\project\files')
print(Path.home())

#my_file = open(Path.home() / Path('D:','كورس بايثون','project','files','read.txt'), 'r')

#print(str(Path.home() / Path('D:','كورس بايثون','project','files','read.txt')))

op = open('D:/كورس بايثون/project/files/new file.txt','r')
print(op)


print(op.name)
print(op.mode)
print('-------------------------------------------------------------------------------------')

# الان نستخدم القراءة
# ظللنا الامثلة لاكمال المثال
#print(op.read())
# لطباعة سطر و احد نستخدم الدالة read line
#print(op.readline())
#print(op.readlines())

# توجد طريقتين فقط لتحديد اي سطر تريد طباعته لان الدالة السابقة تعيد اول سطر  فقط
# الاول وظعها في مصفوفة
lines = op.readlines()
print(lines[0:5])

print('-------------------------------------------------------------------------')
# الطريقة الثانية حلقة فور
i = 0
for line in lines:
    print(line)
    i += 1
    if i == 5:
        break

op.close


