# توجد مشكلة في الكود تحتاج للمراجعة
import webbrowser
import sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    print('enter you address')

webbrowser.open('https://www.google.com/maps/place/'+ address)
