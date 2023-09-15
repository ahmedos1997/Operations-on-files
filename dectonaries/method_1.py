# get
# وهو يحل رسالة مثلا لا يوجد اذا لم نجد السجل المطلوب
# في المثال التالي سنحذف ال salary لمعرفة الدرس
ahmed = {
    'name' : 'ahmed',
    'phone': '0999968099',
    'skills': ['html', 'odoo','pythone','c++']
}
#print(ahmed['name'] + ' his salary is ' + str(ahmed['salary']))
print(ahmed['name'] + ' his salary is ' + str(ahmed.get('salary','no salary')))
print('----------------------------------------------------------------------------')
#setdefault
# يقوم هذا التابع باضافة سجل غير موجود
# اما في حالة السجل موجود اصلا يعيد القيمة القديمة حتى لو ادخلنا فيه قيمة جديدة
# ونكتبه بدلا عن عملية if لاضافة سجل جديد
# تابع المثال التالي

print(ahmed)
print(ahmed.setdefault('name', 'sara'))
print(ahmed.setdefault('salary','50000'))
print(ahmed)
# هنا نجد انه اضاف القيمة سالاري
# يمكن عمل نفس الطريقة ولكن بحلقة if و هي اكثر كتابة
if 'langa' not in ahmed:
    ahmed['langa']= ['pdf']
    print(ahmed)

print('------------------------------------------------------')
# update
# يقوم هذا التابع باضافة بيانات جديدة او تعديل بيانات موجود اصلا
num = {1:'one', 2: 'three'}
print(num)
print(num.update({2:'tow'}))
print(num)
print(num.update({3:'three'}))
print(num)

print('---------------------------------------------------------')
# clear
# يقوم هذا التابع بحذف بيانات القاموس مع ابقاء القاموس فارغاً
print(num)
num.clear()
print(num)






