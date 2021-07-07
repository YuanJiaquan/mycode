import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

con=smtplib.SMTP_SSL('smtp.qq.com','465')
con.login('772878309@qq.com','dziluhwygqbvbcjj')
sender='772878309@qq.com'
receiver=['704046058@qq.com']
ccer=['2055408412@qq.com']
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')

smtp_server = input('SMTP server: ')

msg=MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()


try:
    # 发送邮件  由谁发送  邮局发送 con  发送邮件失败
    con.sendmail(sender,receiver,msg.as_string())
    print('发送邮件成功')
except Exception:
    print('无法发送邮件')


