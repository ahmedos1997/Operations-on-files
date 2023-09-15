#startswith , endswith
# يستعلم هذا التابع اذا كنت السلسة تبدء او تنتهي بالحرف كذا و الجواب يكون true , faluse مثال الاتي
test = 'hello, world'
print(test.startswith('h'))
print(test.startswith('f'))
print(test.endswith('d'))
print(test.endswith('t'))
# حددنا اذا كانت الجملة بين 7 و 11 تبدأ ب w
print(test.startswith('w', 7 , 11))


print('--------------------------------------')

# strip , lstrip , rstrip
# يقوم هذا التابع بحذف الفراغات او الكتابات داخل السلسلة strip
# lstrip , rstrip تقوم بحذف الفراغات اذا كانت باليمين او بالشمال

test = '   heloo, world   '
print(test)
print(test.strip())
print(test.lstrip())
print(test.rstrip())
# ناخذ مثال اخر مع وجود كلمات في الجوانب

test = '@@@heloo,world@@@'
print(test)
print(test.strip('@'))
print(test.lstrip('@'))
print(test.rstrip('@'))

# مثال ثالث مع وجود اكثر من رمز

test = '@#@#@#@heloo,world@#@#@#@'
print(test)
print(test.strip('@#'))
print(test.lstrip('@#'))
print(test.rstrip('@#'))


print('-------------------------------------------')

#zfill
# ويستخدم هذا التابع لاضافة 0 او زيرو للسلسلة تابع المثال التالي عن الساعة

hours = '1'
min = '9'
sec = '5'

print(f'{hours}:{min}:{sec}')
print(f'{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}')
print(f'{hours.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}')
# مثال اخر

hours = '1'
min = '19'
sec = '25'

print(f'{hours.zfill(2)}:{min.zfill(2)}:{sec.zfill(2)}')
print(f'{hours.zfill(3)}:{min.zfill(3)}:{sec.zfill(3)}')




