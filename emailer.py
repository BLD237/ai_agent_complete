import smtplib
from email.mime.text import MIMEText
from config import EMAIL, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email(subject, body, to_email):
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)