import re
# سنقوم بعملية التحقق من البريد الالكتروني باستخدام التعبير النمطي
def isemail (email):

    is_email = re.search(r'^ [A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$', email)
    if is_email:
        print(f'your email {email} is correct email')
    else:
        print(f'your email {email} is not correct email')

print('is ahmed-elmadani@gmail.com is correct email')
isemail('ahmed-elmadani@gmail.com')
print('is ahmed-elmadani is correct email')
isemail('ahmed-elmadani')