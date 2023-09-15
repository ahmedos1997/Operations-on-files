# join
# حيث يقوم هذا التابع بجمع الجملة التي يكتبها المستخدم ثم تحويل القائمة الى سلسلة

list = ['hello', 'world']
print (list)
print(' '.join(list))
print('-'.join(list))
print('ABC'.join(list))

print('________________________________')

# split
# يقوم هذا التابع بعكس ما يفعله المثال السابق
# حيث يقوم بفصل القائمة بالجملة التي يكتبها المستخدم ثم تحويل السلسة الى قائمة كالمثال التالي

test = 'hello world'
print(test)
print(test.split(' '))

test = 'my abc name abcis abcahmed '
print(test)
print(test.split('abc'))

test = ''' hello
how are you?
thanks, iam fine'''
print(test)

print(test.split('\n'))



print('----------------------')
# splitline
# يقوم تقريبا بنفس الامثلة السابقة

test = ''' hello
how are you?
thanks, iam fine'''
print(test)

print(test.splitlines())

# الفرق بين المثالين اعلاه بين split و splitlines  اننا لم نحتاج ان نكتب \n لفصل الكلمات





