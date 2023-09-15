# توجد مشكلة في ملف الورد الرجاء ايجاد حل للمشكلة
import docx
from pathlib import Path
doc = docx.document(Path.home()/ Path('G:/python cource','project','word','academy_1.docx'))
print(len(docx.paragraph()))