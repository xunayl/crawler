import smtplib
import email.mime.multipart
import email.mime.text
import codecs


def task():
    res = []
    with codecs.open('user', 'r') as f:
        for i in range(2):
            res.append(f.readline().replace('\n', ''))
    mail_user = res[0]
    mail_password = res[1]

    msg = email.mime.multipart.MIMEMultipart()
    ##from和to的名字可以随便取,为发件人和收件人的显示
    msg['from'] = 'yxu_py@163.com'
    msg['to'] = 'shyu_ee@163.com'
    ###subject为邮件名称
    msg['subject'] = '自动推送'
    ###邮件内容
    content = '我是萌萌的机器人~~~,正在完善功能中,期待后期的自动推送噢~'
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    try:
        # smtp = smtplib
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com', '25')
        smtp.login(mail_user, mail_password)
        smtp.sendmail('yxu_py@163.com', 'shyu_ee@163.com', str(msg))
        smtp.quit()
        print('已发送')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

