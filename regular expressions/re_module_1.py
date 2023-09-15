# search
# لاستخدام التعابير النمطية يجب استيراد العنصر re
# عملية البحث هي عملية لايجاد نمط تعبيري معين داخل الجملة تابع المثال التالي

import  re
txt = 'My name is Ahmed'
search = re.search('[A-Z]',txt)
print(search)
# لمعرفة الانديكس داخل الجملة نفعل الاتي
print(search.span())
# لمعرفة جميع خصائص search k;jf hghjd
print(dir(search))

# امثلة اخري
print('--------------------------------------------------------------------')
test = 'is 458-587-1547. tomorrow. 458-145-1234 is my office'
search = re.search(r'\d{3}-\d{3}-\d{4}',test)
print(search)
print(search.group())
print(search.string)
print('----------------------------------------------------------------------------')
# findall
# تعمل هذه الدالة مثل الدالة سيرش ولكنها في حالة وجدت تطابق تعيد لنا قائمة بجميع العناصر المتطابقة واذا لم تجد تعيد قائمة فارغة

string= 'hello my number is 458-789-1234 and my freind phone is 145-748-4567'
test_search = re.findall(r'\d{3}-\d{3}-\d{4}',string)
print(test_search)
test_search = re.findall(r'[A]', string)
print(test_search)
print('-------------------------------------------------------------------------')
#practic
# تمرين
phone = input('please enter your number ')
check_phone = re.findall(r'\d{3}-\d{3}-\d{4}',phone)
if check_phone:
    print('your phone {phone} is correct')
else:
    print(f'your phone {phone} is not correct')

