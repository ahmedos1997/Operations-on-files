from pathlib import Path

# توجد مشكلة في هذا المثال الرجاء مراجعة المحاضرة
myfile = open('new_file.txt', 'w')
#myfile = open(Path.home() / Path('D:كورس بايثون','project','files','new_file.txt'),'w')
#myfile.write = ('11. hello, how are you')
#myfile.write = ('12. hello, how are you')
#myfile.write = ('13. hello, how are you')
# نكمل باقي الامثلة
mylist = ['16. hello, how are you\n 17.hello, how are you\n']
myfile.writelines(mylist)