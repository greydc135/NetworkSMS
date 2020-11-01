import smtplib
from email.message import EmailMessage

def email_message(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = ""       # email goes here
    password = ""   # password goes here, missing because it's my own private email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    server.quit()

    