import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
import os.path

# smtpserver='smtp.163.com'
def send_mail(file_new):
	f=open(file_new, 'rb')
	mail_body=f.read()
	f.close
	file_name=os.path.basename(file_new)

	user="zhqg23@163.com"
	password="zhuqiuge23"
	reciver="zhqg23@163.com"
	subject="自动化测试报告"

	msg=MIMEMultipart()
	msg.attach(MIMEText(mail_body,'html','utf-8'))
	att=MIMEText(open(file_new, 'rb').read(),'html','utf-8')
	att["Content-Type"]='application/octet-stream'
	att["Content-Disposition"]='attachment;filename=%s'%file_name
	#msg=MIMEMultipart('related')

	msg['Subject']=subject
	msg['From']=user
	msg["To"]=reciver
	msg.attach(att)

	smtp=smtplib.SMTP_SSL('smtp.163.com',465)
	smtp.login(user, password)
	smtp.sendmail(user, reciver, msg.as_string())
	smtp.quit()
	print("email has been sent out")

#===查找测试报告目录，找到最新的测试报告文件====
def new_report(testreport_dir):
	lists=os.listdir(testreport_dir)
	lists.sort()
	file_new=os.path.join(testreport_dir, lists[-1])
	print(file_new)
	return file_new
