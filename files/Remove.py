# unlink()
# تتخدم هذه الدالة لمسح النلف او المجلد


import os
import shutil
from pathlib import Path
import Send2Trash



#os.unlink(Path.home() / Path('Desktop','New folder','hahahahahah.txt'))
# الدالة rmdir تسمح المجلدات الفارغة فقط

#os.rmdir(Path.home() / Path('Desktop','New folder','empty'))

# لحذف مجلد وداخله بيانات نستخدم الدالة shutil.rmtree

#shutil.rmtree(Path.home() / Path('Desktop','New folder','hahahahahah'))
# في الامثلة السابقة تم مسح جميع البيانات نهائياً
# في المثال التالي سنتعلم كيف نحذ الملفات و تكون موجودة في سلة المهملات

Send2Trash.Send2Trash(Path.home() / Path('Desktop','New folder','new file'))
