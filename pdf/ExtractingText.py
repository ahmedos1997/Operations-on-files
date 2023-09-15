import PyPDF2
from pathlib import Path

# rb اختصار الى read binary لان البي دي اف يعد ثنائي
pdf_file = open(Path.home() / Path('D:/python cource','project','pdf','pdf_test.pdf'),'rb')
# هذا قارئ ملفات بي دي ايف
pdfreader = PyPDF2.PdfReader(pdf_file)

# لمعرفة عدد صفحات الملف
print(len(pdfreader.pages))
# لقراءة الملف الرقم 0 يعني الصفحة الاولى وهكذا
pagepdf = pdfreader.pages[0]
print(pagepdf.extract_text())

pdf_file.close()















