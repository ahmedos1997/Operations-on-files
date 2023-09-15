import smtplib


sender_emal = 'ahmedelmadani1997@gmail.com'
rec_email = 'ahmedelmadani1997@gmail.com'

password = input('enter you password ')

message = 'hi ahmed my name is ahmed'
# connect to server
server = smtplib.SMTP('smtp.gmail.com', 587)  # port 578
server.starttls() # تشفير الاتصال

server.login(sender_emal, password)
print('login is good')
server.sendmail(sender_emal, rec_email, message)
print('you have send message to ', rec_email)













