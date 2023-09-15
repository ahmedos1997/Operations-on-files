import re
def isphonenum (text):
    is_phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
    if is_phone:
        print(f'the {text} is correct')
    else:
        print(f'the {text} is not correct number')

print('is 458-587-1547 a phone number? ')
isphonenum('458-587-1547')
print('-------------------------------------')
print('is 458-587-154 a phone number')
isphonenum('458-587-154')