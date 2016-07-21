# -*- coding: UTF-8 -*-
#实现定时截图并发送到邮箱,已完成初步功能，待加上截图时间，以及改成HTML格式
import time
from PIL import Image,ImageGrab
import smtplib
import requests
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# from email.mime.multipart import MIMEMultipart

#163邮箱设置
# mail_host="smtp.163.com"  #设置服务器
# mail_user="lxyx520123@163.com"    #用户名
# mail_pass="lxyx520123"   #口令 

# #139邮箱设置
# mail_host="smtp.139.com"  #设置服务器
# mail_user="13883970320@139.com"    #用户名
# mail_pass="lxyx520123"   #口令 

# bjtu邮箱设置
mail_host="mail.bjtu.edu.cn"  #设置服务器
mail_user="08281159@bjtu.edu.cn"    #用户名
mail_pass="lxyx520123"   #口令 




sender = '08281159@bjtu.edu.cn'
receivers = ['lxyx520123@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


message = MIMEMultipart()
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("测试邮件", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText('测试发送附件测试……', 'plain', 'utf-8'))

att1 = MIMEText(open('test.jpg', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.jpg"'
message.attach(att1)

while 1:
	try:
		#定时截图
		im = ImageGrab.grab()
		im.save('test.jpg','jpeg')
	    
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)  
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException,e:
	    print "Error: 无法发送邮件",e
	time.sleep(10)
#截图并保存模块

# im = ImageGrab.grab()
# im.save('test.jpg','jpeg')
# Image.open(r"valid.jpg").show()