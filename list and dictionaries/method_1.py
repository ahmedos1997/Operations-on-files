# append and insert
# تستخدم append لاضافة سجل داخل المصفوفة
# تستخدم insert لاضافة سجل و تحديد مكانه داخل المصفوفة تابع المثال التالي

emp = ['ahmed', 'mohammed', 'rawan', 'faisal','ibrahim']
emp.append('ali')
print(emp)

emp.insert(1, 'alaa')
print(emp)
#  والان سندمج قائمة جديدة داخل القائمة القديمة
oldemp = ['samah','awad']
emp.append(oldemp)
print(emp)
# لطباعة القائمة عناصر مصفوفة oldemp من داخل emp
print(emp[7])
# لطباعة عنصر من مصفوفة oldemp من داخل emp ولكن عنصر معين سنقوم بتحديد رقم المصفوفة oldemp داخل emp ثم كتابة رقم السجل المطلوب

print(emp[7][0])
print(emp[7][1])
print('----------------------------------------------------------')
# extend
# يقوم هذا التابع بدمج السجلات الجديدة مع القديمة مباشرة بدون دمجها كقائمة

emp = ['ahmed', 'mohammed', 'rawan', 'faisal','ibrahim']
oldemp = ['samah','awad']

emp.extend(oldemp)
print(emp)

print('----------------------------------------------------------------')
# remove
#  وهي تستخدم لمسح سجل داخل المصفوفة

emp.remove('awad')
print(emp)
# سوف اقوم بتجربة في المثال التالي من عندي
'''
print('enter the name')
name = input()

if name not in emp:
    print('can not found' + name)
else:
    emp.remove(name)
    print('the name was delete')
    print(emp)
'''
# في هذا المثال سنقوم بكتابة قائمة فيها اسماء متشابهة

emp = ['ahmed', 'mohammed', 'ibrahim', 'faisal','ibrahim']
emp.remove('ibrahim')
print(emp)

# نلاحظ في المثال السابق حذف اول كلمة متشابهة فقط
# باستخدام الاستيتمين del يمكن حذف السجل المتشابهة اذا كنا نعرف index الخاص به
# وستكون عملية الحذف عن طريق index  فقط
del emp[0]
print(emp)

# sort
# حيث يقوم هذا التابع بترتيب القائمة كالمثال التالي
num = [1,0.2,2,6,-7]
num.sort()
print(num)
# نلاحظ انه في المثال السابق رتب من الاصغر الى الاكبر ماذا لو اردنا العكس
# اذا تركنا الاقواس () فسيعتبر البرنامج ان قيمة reverse = faluse
# لنتابع المثال التالي

num.sort(reverse=True)
print(num)
# مثال اخر ولكن كسلسلة وليس رقم
# في المثال التالي سيقوم البرنامج بترتيب الكلمات حسب الاحرف

emp = ['ahmed', 'mohammed', 'ibrahim', 'faisal','ibrahim']
emp.sort()
print(emp)
# والترتيب العكسي
emp.sort(reverse=True)
print(emp)
print('--------------------------------------------------------')
# reserve
# توجد تابع reverse مستقل في لغة بايثون حيث يقوم بالترتيب العكسي للمصفوفة

emp = ['ahmed', 'mohammed', 'ibrahim', 'faisal','ibrahim']
emp.reverse()
print(emp)
