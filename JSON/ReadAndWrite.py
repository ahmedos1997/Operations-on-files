# التعامل مع ملفات جيسون الرجاء كراعات الفاصل داخل المتغيير
stringjsonfile = '{"name" : "zophi", "iscat" : true , "nicecuate" : 0 ,"feliniq" : null}'
import json
# قرائة الملف
stringvalue = json.loads(stringjsonfile)
print(stringvalue)

# الكتابة داخل الملف


pythonvalue = {"is cat" : True , 'nicecaut' : 0, 'name' : 'zophi', 'feliniqi' : None}

stringdata = json.dumps(pythonvalue)
print(stringdata)
