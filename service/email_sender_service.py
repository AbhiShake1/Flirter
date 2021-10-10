from smtplib import SMTP  # simple main transmission protocol library
from email.message import EmailMessage


class EmailSenderService:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def send(self, subject: str, msg: str, email_to="") -> None:
        # smtp server of gmail and port number
        server = SMTP("smtp.gmail.com", 587)
        server.starttls()  # start transfer layer security
        server.login(self.email, self.password)  # log in to account
        email: EmailMessage = EmailMessage()
        email["From"] = self.email  # sender email
        email["To"] = email_to  # receiver email
        email["Subject"] = subject  # subject
        email.set_content(msg)  # email body
        server.send_message(email)  # send email
        server.close()  # close and log out
