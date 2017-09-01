#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys   
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#构造消息
try:
    mail_smg = sys.argv[1]
    print('*' * 20)
    #print ('\033[1;31;40m')
    print 'mail_smg:' + mail_smg
    #print ('\033[0m')
except BaseException:
    #print ('\033[1;31;40m')
    print "error! need smg"
    #print ('\033[0m')
    exit(0)

#第三方 SMTP 服务
mail_host="smtp.mxhichina.com"			#设置服务器
mail_user="your@mail"			#用户名
mail_pass="yourpwd"				#口令 
 
sender = 'your@mail'			#发送邮箱
receivers = ['your@mail2']		#接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 html 设置网页格式，第三个 utf-8 设置编码
message = MIMEText("<html>" + mail_smg + "</html>", 'html', 'utf-8')
message['From'] = Header("From", 'utf-8')	    #发件人
message['To'] =  Header("To, 'utf-8')		      #收件人
subject = '服务不可达报告'					            #邮件主题
message['Subject'] = Header(subject, 'utf-8') #邮件正文

#发送邮件
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)					#25为SMTP端口号
    smtpObj.ehlo()
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()  
    #print ('\033[1;31;40m')
    print "邮件发送成功"
    #print ('\033[0m')
    print('*' * 20)
except smtplib.SMTPException:
    #print ('\033[1;31;40m')
    print "Error: 无法发送邮件"
    #print ('\033[0m')
    print('!' * 20)
