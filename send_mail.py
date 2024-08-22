import smtplib

sender = "sender@example.com"
receivers = ["receiver1@example.com", "receiver2@example.com"]


def format_mail(mail):
    return "{} ".format(mail.split("@")[0], mail)


message = """From: {}
To: {}
Subject: Example Subject

This is a test mail example
""".format("{} ".format(sender.split("@")[0], sender), ", ".join(map(format_mail, receivers)))


try:
    print("sending message: " + message)
    with smtplib.SMTP('example-smpt.com', 25) as session:
        session.sendmail(sender, receivers, message)
    print("message sent")
except smtplib.SMTPException:
    print("could not send mail")