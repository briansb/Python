import smtplib

HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "4brianbirmingham@gmail.com"
FROM = "4brianbirmingham@gmail.com"
text = "Python 3.4 rules them all!"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
    ))

server = smtplib.SMTP(HOST,587)
server.login("4brianbirmingham","Luger9mm")
server.sendmail(FROM, [TO], BODY)
server.quit()
