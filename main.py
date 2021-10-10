# coding=UTF-8
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import from_email, password, html, name, contacts
import pandas as pd


def check_mail(mail, psw):
    if "gmail.com" in from_email:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
    elif "yandex.ru" in from_email:
        server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    elif "mail.ru" in from_email:
        server = smtplib.SMTP_SSL('smtp.mail.ru:465')
    elif "muctr.ru" in from_email:
        server = smtplib.SMTP_SSL('smtp.muctr.ru:465')
    else:
        return False
    try:
        server.login(mail, psw)
    except:
        return False
    return True


def send_mail(in_file, mail, psw, header, html_text):
    people = pd.read_excel('test.xlsx')
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
    elif "muctr.ru" in from_email:
        server = smtplib.SMTP_SSL('smtp.muctr.ru:465')
    else:
        print("Неопознанный домен")
        exit(0)
    server.login(mail, psw)
    for human in people.values:
        print(human[0], human[1])
        msg = MIMEMultipart()
        msg['Subject'] = header
        msg['From'] = from_email
        msg['To'] = human[1]
        dict_const = {}
        for key in in_file.keys():
            dict_const[key] = human[in_file[key] - 1]
        msg.attach(MIMEText(html_text.format(**dict_const), 'html', 'utf-8'))
        server.sendmail(from_email, human[1], msg.as_string())
        count +=1
        print('{}/{}'.format(count, len(people.values)))
        time.sleep(10)
    server.quit()
