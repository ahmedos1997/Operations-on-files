# تجميع مجموعة من ملفات pdf في ملف pdf واحد
import fileinput

import PyPDF2, os
from pathlib import Path

pdffile = [] # قمنا بعمل مجموعة فارغة و سنخزن فيها اسماء الملفات التي نريد دمجها
# سنقوم بعمل حلقة فور للمرور على الملفات التي نريد دمها والتي تحمل الصيغة بي دي اف فقط
for filename in os.listdir(Path.home() / Path('G:\python cource','project','pdf','article')) : # هنا نقوم باحضار جميع الملفات الموجودة داخل الملف
    if filename.endswith('.pdf'):                            # هنا حددنا فقط الملفات التي تحمل الصيفة بي دي اف
        pdffile.append(filename)                              # هنا قمنا باضافة جميع الملفات الى المتغير filename
pdffile.sort(key= str.lower)                                  #  قمنا بترتيب الملفات بالاحرف الهجائية لتكون مرتلة بعد الدمج
pdfwriter = PyPDF2.PdfWriter()

for filename in pdffile:                                      # عملنا حلقة للمرور على الملفات المخزنة في pdffile
    pdffileob = open(Path.home() / Path('G:\python cource','project','pdf','article',filename),'rb')       # نقوم بفتح الملف الاول ثم الثاني وهكذا
    pdfreader = PyPDF2.PdfReader(pdffileob)     # انشاناه لقراءة المف

    for numpage in range(1, len(pdfreader.pages)) :   # هنا حددنا له ان يحدد ارقام الصفحات من الرقم الثاني
        pageob = pdfreader.pages[numpage]             # استخدمناها لجلب الصفحات
        pdfwriter.add_page(pageob)                   # استخدمنا الدالة add لجلب الصفحات

pdfoutput = open(Path.home() / Path('G:\python cource','project','pdf','article','article.pdf'),'wb')   # حددنا المكان الجديد للملف
pdfwriter.write(pdfoutput)                          # حددنا اننا نريد الكتابة
pdfoutput.close()                                   # اغلقنا الملف

