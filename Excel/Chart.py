import openpyxl
from pathlib import Path
exfile = openpyxl.load_workbook(Path.home() / Path('D:/python cource','project','Excel','example.xlsx'))
sheet = exfile['Sheet1']

#charts
# الرسم البياني

# نستخدم الباني ()Reference لإنشاء مرجع للبيانات المطلوب رسمها وإضافتها للرسم البياني.



titel = openpyxl.chart.Reference(sheet, min_col=1, max_col=1 , min_row=1, max_row=6)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=2 , min_row=1, max_row=6)
chart = openpyxl.chart.BarChart()  # حددنا الشكل البياني و توجد انواع كثيرة منه
# اشكال اخرى للرم لبياني يمكن تفعيلها
#chart = openpyxl.chart.LineChart()
#chart = openpyxl.chart.PieChart()


chart.title = 'my new titel'                          # حددنا عنوان للشكل البياني
chart.add_data(data=data)
chart.set_categories(titel)

sheet.add_chart(chart, 'E8')


exfile.save(filename= Path.home() / Path('D:/python cource','project','Excel','example.xlsx')) # وهكذا تم حفظ الملف






