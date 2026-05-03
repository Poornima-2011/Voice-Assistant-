#email_sender.py
import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, content, from_email, from_password):
    try:
        email = EmailMessage()
        email['From'] = from_email
        email['To'] = to_email
        email['Subject'] = subject
        email.set_content(content)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(from_email, from_password)
            smtp.send_message(email)
        return True
    except Exception as e:
        print("Error:", e)
        return False
