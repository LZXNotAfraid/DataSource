# -*- coding: utf-8 -*-
# author:RicardoLiu
# date:2019/5/24 22:49

import smtplib
from email.mime.text import MIMEText
from . import sec




if __name__ == "__main__":
    print("Test emailing")
    msg = MIMEText("send by python smtplib", "plain", "utf-8")
    sender = sec.SENDER
    password = sec.PASS
    receiver = "632814252@qq.com"
    smtp_server = "smtp.163.com"
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = 'from Bot'
    server = smtplib.SMTP(smtp_server, 25)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()