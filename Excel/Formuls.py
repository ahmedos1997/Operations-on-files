# الدوال الرياضية (جمع - طرح - الخ
import openpyxl
from pathlib import Path
exfile = openpyxl.load_workbook(Path.home() / Path('D:/python cource','project','Excel','example.xlsx'))
sheet = exfile['Sheet1']

sheet['B7'] = '=sum( B1:B6)'
sheet['B8'] = '=average( B1:B6)'          # متوسط المرتبات
sheet['B9'] = '=countif( B1:B6,">750")'   # عدد الموظفين الراتبهم اكبر من 750




exfile.save(filename= Path.home() / Path('D:/python cource','project','Excel','example.xlsx')) # وهكذا تم حفظ الملف







