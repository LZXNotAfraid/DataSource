# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/24 22:49

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from sec import *

class EmailInformer:
    msg = MIMEMultipart

    def __init__(self, text, to, subject, attach=None):
        self.msg = MIMEMultipart()
        self.msg["From"] = SENDER
        self.msg["To"] = to
        self.msg["Subject"] = subject
        self.msg.attach(MIMEText(text, "plain", "utf-8"))
        if attach is not None:
            for x in attach:
                part = MIMEApplication(open(x, 'rb').read())
                part.add_header('Content-Disposition', 'attachment', filename=x)
                self.msg.attach(part)

    def send(self):
        server = smtplib.SMTP("smtp.163.com", 25)
        server.login(SENDER, PASS)
        server.sendmail(SENDER, self.msg["To"], self.msg.as_string())
        server.quit()

if __name__ == "__main__":
    print("Test emailing")
    '''
    msg = MIMEText("send by python smtplib", "plain", "utf-8")
    sender = SENDER
    password = PASS
    receiver = "632814252@qq.com"
    smtp_server = "smtp.163.com"
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = 'from Bot'
    server = smtplib.SMTP(smtp_server, 25)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    '''
    e = EmailInformer("带附件的测试邮件",
                      "632814252@qq.com",
                      "测试邮件",
                      ['F:\\Photos\\tupian.jpg', 'F:\\Photos\\mirrorofthesky.jpg'])
    e.send()