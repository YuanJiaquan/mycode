# 发送附件  pytest+jenkins 下载工具就行  json文件

import smtplib
# 发送附件
from email.mime.multipart import MIMEMultipart
# 发送正文
from email.mime.text import MIMEText
# 头部
from email.header import Header

con=smtplib.SMTP_SSL('smtp.qq.com','465')
con.login('772878309@qq.com','dziluhwygqbvbcjj')
sender='772878309@qq.com'
receiver=['704046058@qq.com']

# 发送附件
# 创建一个信件
message=MIMEMultipart()
# 先找到这个文件
content=open('./1.html','rb').read()
# 写信
file1=MIMEText(content,'base64','utf-8')
# 信封取个名字 附件名  有个html文件发送
file1['Content-Disposition']='attachment;filename="a.html"'
# 把信放在信封中
message.attach(file1)

# 发送人
message['From']=Header('秋水大宝贝<2804555260@qq.com>')
# 收件人
message['To']=Header('秋水小宝宝')
# 标题
message['Subject']=Header('秋水真好看')

# 发送邮件
con.sendmail(sender,receiver,message.as_string())

# 先压缩文件  zip包 把zip包以附件的形式发送给负责人  负责人在去下载，解压再看
# pytest  allure测试报告  界面 链接，点击链接 在登录就可以看到了