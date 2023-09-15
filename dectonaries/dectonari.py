# decronaris
# هي قاموس تستخدم في كتابة السجيل و داخل كل سجل عدد من المعلومات
# في المثال التالي سنوضح مشكلة عدم استخدام القاموس حيث لايوجد طريقة لتحديد السجل و معلوماته و شاهد الفرق
'''
emp = ['ahmed','mohammed', 'sara', 'maha']
salary = ['50000'.'70000','100000']
phone = ['05545454','544545454','0245545445']
# هنا لايمكن معرفة مثال احمد كم راتبه او كم رقم هاتف
# هنا سوف نستخدم الدكشناري او القاموس لحل هذه المشكلة
'''
ahmed = {
    'name' : 'ahmed',
    'salary': '100000',
    'phone': '0999968099',
    'skills': ['html', 'odoo','pythone','c++']
}
print(ahmed)
print(ahmed['phone'])
print(ahmed['salary'])

# في الدكشنري اذا كانت قائمتين تحمل نفس القيم حتى لو لم تكن بنفس الترتيب يعتبر القائمتين متساويتين عكس عن المصفوفة
# تابع المثال التالي

list = ['ahmed','mohammed', 'sara']
mylist = ['sara','ahmed','mohammed']
print(list==mylist)
print(list[0])
print(mylist[0])
print('----------------------------------------------------------')
# هنا الناتج سوف ياتي خطا
# فلنجرب نفس المثال عن طريق الدكشنري

emp = {'name': 'ahmed', 'age': '25', 'salary': '5000'}
oemp = {'age': '25', 'salary': '5000', 'name': 'ahmed'}
print(emp==oemp)
# النتيجة صحيحة

print(emp['age'])
print(oemp['age'])

print(emp['name'])
print(oemp['name'])
print('-----------------------------')
# تمرين
'''
birth = {'ahmed':'may 97', 'mohammed':'dec 94', 'wdzain':'agu 95'}
while True:
    name = input('enter the name ')
    if name == '':
        break
    else:
        if name in birth:
            print(birth[name] + ' the birth of ' + name)
        else:
            print('we can not found it')
            print('what the birth of ' + name)
            newbirth= input()
            birth[name] = newbirth
            print('new name was add to database')
'''
print('---------------------------------------------------------------')
# تكملة الدرس

ahmed = {
    'name' : 'ahmed',
    'salary': '100000',
    'phone': '0999968099',
    'skills': ['html', 'odoo','pythone','c++']
}
# لطباعة العنوان فقط
print(ahmed.keys())
# لطباعة القيمة
print(ahmed.values())
# لطباعة كل البيانات داخل اقواس
print(ahmed.items())
print('-----------------------------------------------------')

# مثال لعمل اكثر من قاموس داخل قاموس رئيسي
# get
test = {
    'test1' : {
                1:'html',
                2:'css',
                3:'bootstrap'
     },
    'test2' : {
                1:'php',
                2:'node.js'

}
}

print(test)
print(test['test1'])
print(test['test2'])
print(test['test1'][2])


