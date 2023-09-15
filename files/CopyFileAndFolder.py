# سنتعلم هنا طريقة عمل نسخ للملفات عن طريق الدالة shutil.copy
# عند كتابة الدالة نقوم بكتب مسار الملف الذي نريد نسخه ثم فاصلة ثم كتابة مسار الملف الجديد و اسمه واذا لمن نكتب اسمه سيقوم بنسخ نفس الاسم القديم
import  os
import shutil
from pathlib import Path
shutil.copy(Path.home() / Path('Desktop','new folder','new_folder.txt'), Path.home() / Path('Desktop', 'dreamwaver', 'ahmed.txt'))
#shutil.copy('New Folder','new_folder.txt'),('dreamwaver','ahmed.txt')

# لنسخ المجلدات نسنخدم الدالة shutil.copytree

shutil.copytree(Path.home() / Path('Desktop','dreamwaver'), Path.home() / Path('Desktop', 'new folder','hahahahahah'))

