import smtplib
from email.mime.text import MIMEText
pw='cbxseuhhetyndhnm'

body="This is the first python email sent"

msg = MIMEText(body)

msg['From'] = 'mayankr.shakalya@infobeans.com'
msg['To'] = 'mayankr.shakalya@infobeans.com'
msg['Subject'] = 'Python Email'

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('mayankr.shakalya@gmail.com', pw)

server.send_message(msg)

print('Mail sent...')

server.close()