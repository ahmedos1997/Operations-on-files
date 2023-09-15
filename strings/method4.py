# rjust, ljust, center
# يقوم التابع اعلاه بازاحلة السلسة النصية من اليمين او اليسار او من المنتصف تابع المثال التالي

test = 'hello'
print(test)
print(test.rjust(10))
print(test.ljust(10))
print(test.center(10))
# مثال اخر ونقوم بكتابة علامة للازاحات

print(test.rjust(10, '#'))
print(test.ljust(10, '#'))
print(test.center(10, '#'))
print(test.center(11, '#'))

print('--------------------------------------')
# expandtabs
# يقوم هذا التابع بعمل فواصل او مسافات بين الجمل
#  \t المستخدم في هذا المثال يستخدم لعمل الفواصل
test = 'heloo \t how are you \t iam fine \t thankyou'
print(test)
print(test.expandtabs(1))
print(test.expandtabs(10))


