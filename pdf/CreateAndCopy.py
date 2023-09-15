#  انشاء و نسخ الملفات البي دي ايف
from PyPDF2 import PdfWriter as w
from pathlib import Path
import PyPDF2

pdf = w()

file = open(Path.home() / Path('D:/python cource','project','pdf','pdf_file.pdf'),'wb') # مكان حفظ الملف الجديد
# طريقة تحديد عدد الصفحات التي نريدها في الصفحة الجديدة
for i in range(5) :
    pdf.add_blank_page(219,297)     # وهذه ابعاد الورقة A4
pdf.write((file))

# عملية النسخ


pdffile = open(Path.home() / Path('D:/python cource','project','pdf','pdf_test.pdf'),'rb')
pdfreader = PyPDF2.PdfReader(pdffile)

for pagenum in range(len(pdfreader.pages)):
    pageob = pdfreader.pages[pagenum]
    pdf.add_page(pageob)

pdf.write(file)
file.close()





