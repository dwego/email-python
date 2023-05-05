import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# alt = random 5-digit verification number
alt = random.randint(10000,100000)
alt = str(alt)

mail = input('Enter your email for verification: ')

host = "smtp.gmail.com"
port = "587"

# Email and password
login = ""
password = ""

# Connecting to server
server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()

server.login(login,password)

# Building email
body = f"Your verification code is <b>{alt}</b>"
email_msg = MIMEMultipart()

# Sending email
email_msg['From'] = login
email_msg['To'] = mail
email_msg['Subject'] = "Verification Code"
email_msg.attach(MIMEText(body,'html'))

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()

# Verifying code
print('Enter the verification code sent to {}'.format(mail))
code = input('')
code = code.strip()

if code == alt:
    print('Correct')
else:
    print('Incorrect')
