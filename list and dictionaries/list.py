emp = ['ahmed','ali','samar','khalid']
print(emp)
print(emp[0])
print(emp[:3])
print(emp[-1])
print(emp[-3])
# مثال لعرض الستة بين عددين و التحرك بمقدار 1

print(emp[:3:1])
print(emp[::2])
print(emp[0:4:1])
# تغيير عناصر القائمة بعناصر جديدة
emp[1] = 'hassan'
print(emp)

emp[-1] = 'haroon'
print(emp)
# تغيير اكثر من عنصر في القائمة

emp[0:2] = 'samih','yarra'
print(emp)


emp[0:2] = ''
print(emp)

print('--------------------------------------------------------------')

# for loop with list
# الان سوف نستخدم الحلفة فور
emp = ['ahmed','ali','samar','khalid']
for i in range(4):
    print(emp[i])
# هنا لن نحدد القائنة و سوف نكتفي ب المتغيير داخل الحلقة
for i in range(4):
    print(i)
    print('-----------------------------------------------------------------')
# اذا لم نكن نعلم طول المصفوفة فسوف نستخدم الدالة len داخل حلقة فور كالمثال التالي

emp = ['ahmed','ali','samar','khalid']
for i in range(len(emp)):
    print(emp[i])

print('-----------------------------------------------------')
# في المثال التالي سوف نقوم بطباعة المصفوفة و امام كل عنصر في المصفوفة سوف يطبع رقم العنصر في المصفوفة
for i in range(len(emp)):

    print(f'index {i} in emp is:{emp[i]} ')
print('----------------------------------------------------------')
# enumerate
# تقوم هذه الدالة بنفس تفاصيل المثال السابق ولكن بطريقة افضل و اسهل كالمثال التالي
# المتغير index يعبر عن الرقم داخل المصفوفة
# المتغير item يعبر عن الكلمة في المصفوفة

for index , item in enumerate(emp):
    print(f'index {index} in emp is : {item}')
    print('_____________________________')

# in and not in
# تستخدم هذه الدالة لمعرفة اذا كان اسم معين موجود في المصفوفة ام لا
# الناتج يكون true or faluse

print('ahmed'in emp)
print('ahmed' not in emp)
'''
# تمرين بسيط حيث يدخل المستخدم اسم لمعرفته اذا كان موجود يطبع بياناته اما اذا لا يطبع الاسم غير موجود
# هنا من عندي ادخلت الدالة LOWER التي تبدل الحروف
print('ادخل اسم الموظف')
name = input()

if name.lower() not in emp:
   print('لا يوجد موظف اسمه' + name)
else:
    print(f'هو موظف داخل الشركة   {name}')
'''
# سنقوم بجعل المثال السابق موقوف لاكمال الدرس

print('_______________________________________________')
# random.choice() and random.shuffle
# تقوم الدالة random.choice باختيار عنصر عشوائي من القائمة
# اما الدالة random.shuffle تقوم بترتيب القائمة بشكل عشوائي
# لعمل الدالة random يجب استدعائها في العى القائمة import random
# ولكن لان هذا مثال سنقوم باستدعائها هنا

import random

emp = ['ahmed','ali','samar','khalid']

print(random.choice(emp))
print(random.choice(emp))

random.shuffle(emp)
print(emp)


