# regular expressions
# هي التعابير النمطية التي نكتبها في سطر واحد لعمل شي معين يمكن ان نكتبه بطريقة كبيرة دون استخدامها
# مثال للتاكد من رقم الهاتف بدون استخدام التعبير النمطي
# لاستخدام المثال التالي بالطريقة الصحصحة راجع اول درس في التعابير النمطية

# 453-368-1234
def itsphonenum(text):
    if len(text) !=12 :
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-' :
            return False


    for i in range(4,7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-' :
            return False

    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('is 458-587-1547 a phone number')
itsphonenum('458-587-1547')
print('-------------------------------------')
print('is 458-587-154 a phone number')
itsphonenum('458-587-154')
# في استخدام التعبير النمطي يمكن اختصار هذه الكودات في سطر واحد
# الرجاء مراجعة الفديو الاول في الدرس





