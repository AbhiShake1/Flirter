import smtplib  # simple main transmission protocol library


class EmailSenderService:
    def __init__(self, email: str, password: str):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.email = email
        self.password = password

    def send(self, msg: str, email_to="") -> None:
        # smtp server of gmail and port number
        self.server.starttls()  # start transfer layer security
        self.server.login(self.email, self.password)
        self.server.sendmail(self.email, email_to, msg)
        self.server.close()  # close anf log out
