# index[substring, start , end]
# يقوم هذا التابع بعملية بحث داخل السلسلة و إعادة رقمها داخل السلسلة كالمثال التالي

test = 'hello world'
print(test.index('world'))



# نستخدم البداية و النهاية
#print(test.index('world',0 ,5))
# في عملية الطباعة السابقة سوف يرسل لنا رسالة خطأ ولكن لا تكون جميلة
try:
    print(test.index('world', 0 , 5))
except:
    print('we can not find your search')

# هو نفس عمل المثال السابق و الفرق فقط في حالة لم يجد الناتج في عملية البحث يرجع القيمة -1 find
# find [substring, start , end]
print(test.find('world'))
print(test.find('world', 0, 5))

print('--------------------------------------------')


# replace(old value then new value then count
# في هذا التابع نقوم باستبدال الكلمات و طباعة كلمات جديدة تابع المثال التالي
# في حالة لم نحدد قيمة الكاونت سيقوم بتغير كل الكلمات المشابهة داخل السلسلة

test = ('one pluse one equal tow')
print(test.replace('one', '1'))
# في المثال التاي سوف نستخدم كاونت و هي عدد المرات التي يختار فيها الكلمات المشابهة

print(test.replace('one', '1',1))
print(test.replace('tow', '2'))



