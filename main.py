# coding=UTF-8
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import from_email, password, html, name, contacts
import pandas as pd

people= pd.read_excel('test.xlsx')
count = 0
yandex =False
if "gmail.com" in from_email:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
elif "yandex.ru" in from_email:
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    yandex = True
elif "mail.ru" in from_email:
    server = smtplib.SMTP_SSL('smtp.mail.ru:465')
else:
    print("Неопознанный домен")
    exit(0)
server.login(from_email, password)
for human in people.values:
    print(human[0], human[1])
    msg = MIMEMultipart()
    msg['Subject'] = 'Информация для абитуриентов ЦиТХИн'
    if yandex:
        msg['From'] = from_email
    contacts_string = ""
    for key in contacts.keys():
        contacts_string += '– {}: {}<br>'.format(key, contacts[key])
    msg.attach(MIMEText(html.format(human[0], name, contacts_string), 'html', 'utf-8'))
    server.sendmail(from_email, human[1], msg.as_string())
    count +=1
    print('{}/{}'.format(count, len(people.values)))
    time.sleep(10)
server.quit()
