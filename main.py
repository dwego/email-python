import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
# alt = numero aleatorio de 5 digitos para verificação

alt = random.randint(10000,100000)
alt = str(alt)

mail = input('Digite o seu email para verificarmos: ')

host = "smtp.gmail.com"
port = "587"
# Email e senha
login = ""
senha = ""

# Conectando ao servidor
server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()

server.login(login,senha)
# Montando email

body = f"Seu codigo de verificação é <b>{alt}</b>"
email_msg = MIMEMultipart()
# Enviando email

email_msg['From'] = login
email_msg['To'] = mail
email_msg['Subject'] = "Codigo de verificação"
email_msg.attach(MIMEText(body,'html'))

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
# Verificando codigo

print('Digite o cogido de verificação enviado para {}'.format(mail))
codigo = input('')
codigo = codigo.strip()

if codigo == alt:
    print('Correto')
else:
    print('Incorreto')