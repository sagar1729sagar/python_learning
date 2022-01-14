import smtplib
from email.message import EmailMessage



email = EmailMessage()
email['Subject'] = 'Test email'
email['From'] = 'you@gmail.com'
email['To'] = 'someoneelse@gmail.com'
email.set_content("This is an email sent from python code")

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('you@gmail.com','password')
smtp_connector.send_message(email)

