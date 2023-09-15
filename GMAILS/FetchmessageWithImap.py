# read the message with smtp
import imapclient
# connect to server   # ssl = التشفير

impob = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# login to email

rec_email = 'ahmedelmadani1997@gmail.com'
password = input('enter you password ')
impob.login(rec_email, password)


# print all folder

import pprint


pprint.pprint(impob.list_folders())

# select folder
#impob.select_folder(('INBOX', readonly=True))

# search
uid = impob.search(['ALL'])
print(uid)

# توجد مشكلة الرجاء اعادة الدرس

import pyzmail
