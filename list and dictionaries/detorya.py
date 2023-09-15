
# سنقوم بعمل برنامج تخمين
# حيث ان البرنامج يختار اسم من المصفوفة ثم يقوم المستخدم بتخمين احرف هذا الاسم
# اذا كتب حرف صحيح تتحول _ الى الحرف و اذا كان خاطأ تنقص المحاولات وعددها 12 وهكذا


import random
name = input('what is your name? ')
print('goodluck! ' + name)

emp = ['ahmed', 'mohammed','sara', 'maha', 'omer', 'aziza']
word = random.choice(emp)
print('the name is:')


guesses = ''
turn = 12
while turn > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char)


        else:
            print("-")
            failed += 1


    if failed == 0:
            print('you win')
            print('the name is: ', word)
            break

    gess = input("gess your charactor:")
    guesses += gess
    if gess not in word:
        turn -= 1
        print('wronge guess')
        print('you have', + turn, 'more gessus')

    if turn == 0:
        print('you loose' + name)





