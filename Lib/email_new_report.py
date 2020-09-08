from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os
from Service import config
from Service import wirte_log


def send_mail(file_new):
    """
    定义发邮件
    :param file_new:
    :return:
    """
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    server = config.email()[0]
    # print(server)
    sender = config.email()[1]
    receiver = config.email()[2]
    name = config.email()[3]
    pwd = config.email()[4]
    msg = MIMEMultipart()
    # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    # 发送正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('自动化测试报告', 'utf-8')
    msg.attach(text)
    # 发送附件
    # Header()用于定义邮件标题
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename=WbfOpenApi_TestReport.html'
    msg.attach(msg_file)
    msg['from'] = sender  # 发送邮件的人
    msg['to'] = receiver
    # smtp = smtplib.SMTP()
    smtp = smtplib.SMTP_SSL(server, 465)
    # smtp.connect(server, 587)
    # smtp.connect(server, 465)
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(name, pwd)
    smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    smtp.quit()
    try:
        print('The email has been sent successfully !')
    except Exception as e:
        wirte_log.return_log(name, pwd, e)


def new_report(testreport):
    """
    查找测试报告目录，找到最新生成的测试报告文件
    :param testreport:
    :return:
    """
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    file_new = os.path.join(testreport, newreportname)
    return file_new







