import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from api_auto.api_po.utils.log_util import logger


class EmailSender:
    def __init__(self, smtp_host, smtp_port, user, password, use_tls=True):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.user = user
        self.password = password
        self.use_tls = use_tls

    def send_email(self, to, subject, body, html=False):
        try:
            # 创建一个带附件的 email 消息实例，MIMEMultipart 代表邮件正文和附件是 MIME 格式
            msg = MIMEMultipart()
            # 设置邮件的字符编码
            msg['From'] = Header(self.user, 'utf-8')
            msg['To'] = Header(to, 'utf-8')
            msg['Subject'] = Header(subject, 'utf-8')

            # 如果需要发送HTML内容
            if html:
                msg.attach(MIMEText(body, 'html', 'utf-8'))
            else:
                # 发送纯文本
                msg.attach(MIMEText(body, 'plain', 'utf-8'))

                # 创建 SMTP 连接
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            if self.use_tls:
                server.starttls()  # 启用 TLS
            server.login(self.user, self.password)  # 登录邮箱

            # 发送邮件
            server.sendmail(self.user, [to], msg.as_string())
            server.quit()  # 关闭连接
            logger.info("邮件发送成功！")

        except Exception as e:
            logger.error("邮件发送失败：", e)

        # 使用示例


    def send_email_with_html(self,to, subject,data):


        # 读取HTML文件内容
        html_file_path = "../allure-report/templt.html"
        try:
            with open(html_file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
        except FileNotFoundError:
            logger.error(f"文件未找到: {html_file_path}")
            return

            # 创建一个带附件的 email 消息实例，但这里我们实际上只发送HTML正文
        msg = MIMEMultipart('alternative')
        msg['From'] = Header(self.user, 'utf-8')
        msg['To'] = Header(to, 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        # 替换HTML模板
        html_content = self.replace_template(html_content, data)
        # 附加HTML正文
        part1 = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(part1)

        # 创建 SMTP 连接
        try:
            # 创建 SMTP 连接
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            if self.use_tls:
                server.starttls()  # 启用 TLS
            server.login(self.user, self.password)  # 登录邮箱

            # 发送邮件
            server.sendmail(self.user, [to], msg.as_string())
            server.quit()  # 关闭连接
            logger.info("邮件发送成功！")

        except Exception as e:
            logger.error("邮件发送失败：", e)

    # 替换模板中的关键数据
    def replace_template(self,template, data):
        for key, value in data.items():
            template = template.replace("{{ " + key + " }}", value)
        return template

if __name__ == "__main__":
    # 假设使用Gmail，请替换成你的SMTP服务器信息
    email_sender = EmailSender(smtp_host='', smtp_port=587, user='',
                               password='')
    # email_sender.send_email('*@163.com', '测试邮件', '这是邮件正文。http://localhost:63342/mywork/api_auto/api_po/allure-report/2024-09-12/', html=False)

    # 发送HTML邮件
    # email_sender.send_email('*@163.com', '自动化测试结果', '<h1>这是管理后台自动化测试结果</h1>', html=True)
    # 准备邮件数据
    data = {
        "allure_url": "http://localhost:63342/mywork/api_auto/api_po/allure-report/20240912/",
        "total_num": "10",
        "passed_num": "10",
        "failed_num": "10",
        "error_num": "10",
        "skipped_num": "10"
    }
    email_sender.send_email_with_html( '*@163.com', '测试HTML邮件', data)
