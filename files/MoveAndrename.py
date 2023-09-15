# الدالة ةخرث لنقل الملفات

import os
import shutil
from pathlib import Path

#shutil.move(Path.home() / Path('Desktop','New folder','new_folder.txt'), Path.home() / Path('Desktop', 'dreamwaver','yes.txt'))

shutil.move(Path.home() / Path('Desktop','New folder','myfile.txt'), Path.home() / Path('Desktop', 'new folder','yes.txt'))



