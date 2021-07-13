# coding=UTF-8
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import from_email, password, html
import pandas as pd

people= pd.read_excel('test.xlsx')
count = 0
for human in people.values:
    print(human[0], human[1])
    msg = MIMEMultipart()
    msg['Subject']='Информация для абитуриентов ЦиТХИн'
    msg.attach(MIMEText(html.format(human[0]), 'html', 'utf-8'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, human[1], msg.as_string())
    server.quit()
    count +=1
    print('{}/{}'.format(count, len(people.values)))
    time.sleep(10)

