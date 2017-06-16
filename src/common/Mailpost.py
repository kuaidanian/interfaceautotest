import os,time
import smtplib
from smtplib import SMTPDataError
from email.mime.text import MIMEText
from src.common.log import Log
from config import globalparam

def sendmail(file_new):
    logger = Log()
    mail_from = globalparam.mail_from_address
    mail_to = globalparam.mail_accept_address
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #定义标题
    msg['Subject'] = u"RKYSB2G Interface Test Report"
    msg['From'] = mail_from
    msg['To'] = ''.join(mail_to)
    #定义发送时间(不定义的可能有的邮件客户端会不显示发送时间)
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    try:
        smtp = smtplib.SMTP()
        #连接SMTP服务器，此处用的163的SMTP服务器
        smtp.connect('smtp.163.com')
        #用户名密码
        smtp.login('18381671067@163.com', 'zhyo123456789')
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp.quit()
        print('email has send out !')
        logger.info("发送邮件成功")
    except SMTPDataError:
        logger.error('发送邮件失败')
        raise

#查找测试报告，调用发邮件功能
def sendreport():
    logger = Log()
    result_dir = './report/htmlreport/'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print(u'最新测试生成的报告:'+lists[-1])
    if len(lists) > 2:
        print(u'待删除的报告'+lists[1])
        logger.info("开始删除测试报告"+lists[1])
        os.remove(result_dir+lists[1])
        if os.path.exists(result_dir + lists[1]) == False:
            logger.info("删除测试报告成功" + lists[1])
        else:
            logger.info("删除测试报告失败" + lists[1])
    else:
        logger.info("不需要删除测试报告")
    #找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    if globalparam.isneedsendMail == 1:
        logger.info("获取是否发送邮件参数：为是~~是~~准备开始发送")
        #调用发邮件模块
        sendmail(file_new)
    else:
        logger.info("获取是否发送邮件参数：为否")
        print("不发送测试报告······")


if __name__ == "__main__":
    #执行发邮件
    sendreport()
