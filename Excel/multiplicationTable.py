# في البداية يذهب المستخدم الى terminal ثم يقوم بكتابة كلمة بايثون مع اسم الملف اعلاه وهو الوسيط الاول  ثم رقم الذي يريد ضربه وهو الوسيط الثاني
# في هذا المثال سنستخدم جدول الضرب 5

import openpyxl , sys
from pathlib import Path
from openpyxl.styles import Font   # تستخدم لشكل ايطار الصفحة
# سنستخدم الدالة try
if len(sys.argv) ==2:               # نتاكد من ان المستخدم ادخل الوسيطين ونتاكد من ذلك عن طريق الدالة sys.argv

    try:
        number = int(sys.argv[1])                 # ادخلنا الرقم او الوسيط الثاني داخل متغير وهولناه الى int لانه ياتي string

    except Exception as e:                         # في حالة فشل ادخال الجملة اعلاه افعل الاكسبشن كذا
        print(e)

    exfile = openpyxl.Workbook()                  # انشانا ملف اكسل
    sheet = exfile.active                         # سمينا الملف الاول sheet في المتغير sheet
    # سنقوم بعمل حلقتين فور واحرة للصفوف و الاخري للاعمدة


    for y in range(number + 1):            # y  تشير الى الصفوف
        for x in range(number + 1):        # x تشير الى الاعمدة


            isheader = False                 # عندما يكون العنصر موجود في الصف الاول او العامود الاول سيتغير الى tru
            if x == 0 and y == 0:
                isheader = True
                n = ''                     # لجعل اول سطر و اول عامود فارغ
            elif x==0 :
                isheader = True
                n = y

            elif y==0 :
                isheader = True
                n = x

            else:
                n = x * y

                # يجب تحديد الصف و العامود الذي سنكتب فيهم
                cell = sheet.cell(row=y +1 , column=x + 1) # بدانا بارقم واحد لانه في الاعلى بدانا بالرقم صفر

                if isheader:
                    cell.font = Font(blood=True)
                cell.value = n



    savefile = str(Path.home() / Path('D:/python cource/project/Excel') / 'multiplacation') + str(number) + '.xlsx'

    exfile.save(savefile)

    print('file is save in ' + savefile)
else:
    print('please enter tow arg')
# يوجد خطا بسيط الرجاء مراجعة الدرس مرة اخري


