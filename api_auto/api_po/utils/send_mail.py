# send_email.py
import yagmail


def send_report_via_email(to_email, smtp_host, smtp_port, smtp_user, smtp_pass):
    yag = yagmail.SMTP(smtp_host, smtp_user, smtp_pass, smtp_port)
    yag.send(
        to=to_email,
        subject="Test Report",
        contents="Please find attached the test report.",
        attachments=['/path/to/allure-report/allure-results/index.html']
    )


# 使用示例
send_report_via_email('recipient@example.com', 'smtp.example.com', 587, 'your_email@example.com', 'your_password')