name = 'hadi'
age = 29
# print('hello , my name is ' + name +'i am ' + age+ 'years old' )
print('hello , my name is ' + name +' i am ' + str(age) + ' years old ' )

print('heloo , my name is %s. iam %d years old' %(name,age))

rank = 9.0

print('heloo , my name is %s. iam %d years old my rank is %.2f' %(name,age,rank))

print('heloo , my name is {}. iam {} years old my rank is {}'.format(name,age,rank))



print('heloo , my name is {:s}. iam {:d} years old my rank is {:.3f}'.format(name,age,rank))

# هنا اجرينا تغيير لمكان المتغيرات ثم حددنا المدخل حسب الترتيب وكتبناه داخل الاقواس

print('heloo , my name is {1}. iam {0} years old my rank is {2}'.format(age,name,rank))


# في هذه الطريقة استخدمنا متغير لتعريفة داخل دالة الطباعة


print('heloo , my name is {name}. iam {age} years old my rank is {rank}'.format(name = name,age = age,rank = rank))


# الطريقة f-string
# وهي هذه افضل طريقة لكتابة السلاسل النصية وطباعتها

print('__________if-string_____________')

print(f'my name is {name}. iam {age} years old my rank is {rank}.')

print(f'my name is {name}. in nex yaers i will be  {age+1} an i want my rank will be {rank}.')

