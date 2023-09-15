import ezgmail

print(ezgmail.EMAIL_ADDRESS)  # to know what is gmail running
# send email
#ezgmail.send('ahmedelmadani1997@gmail.com','test line','the body of email',['test.png','test2.png'])

# get unread message in my email

# unread here give 25 just last 25 unread message
#unreadmsg = ezgmail.unread()
#print(ezgmail.summary(unreadmsg))
#print(len(unreadmsg))
#print(unreadmsg[0])
#print(unreadmsg[0].messages[0].subject) # subject to give title of ,message
#print(unreadmsg[0].messages[0].body)    # to give body of message
#print(unreadmsg[0].messages[0].timestamp) # the time when send message
#print(unreadmsg[0].messages[0].sender)   # how send the message
#print(unreadmsg[0].messages[0].recipient) # how recive the message

# recent last 25 message read and not

recentmsg = ezgmail.recent()
print((len(recentmsg)))

recentmsg = ezgmail.recent(maxResults=100) # to give me last 100 message
print(len(recentmsg))

# search
search = ezgmail.search('Morrison ')
print(len(search))



