import os
import smtplib
import sys

from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

def send_email_with_attachment(subject, to_address, cc_address, bcc_address, body_text, path):
    # program location
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")
    header = 'Content-Disposition', 'attachment; filename="%s"' % path

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Configuration file not found.")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_address = cfg.get("smtp", "from_address")
    email_user = cfg.get("smtp", "user")
    email_password = cfg.get("smtp", "password")

    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if body_text:
        msg.attach( MIMEText(body_text) )
    msg["To"] = ', '.join(to_address)
    msg["cc"] = ', '.join(cc_address)
    msg["bcc"] = ', '.join(bcc_address)

    attachment = MIMEBase('application', "octet-stream")
    try:
        with open(path, "rb") as fh:
            data = fh.read()
        attachment.set_payload( data )
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % file_to_attach
        print(msg)
        sys.exit(1)
     
    emails = to_address + cc_address + bcc_address
    
    try:
        server = smtplib.SMTP_SSL(host, 465)
        server.ehlo()
        server.login(email_user, email_password)
        server.sendmail(from_address, emails, msg.as_string())
        server.close()
        print('Email sent!')
    except Exception as e:
        print("Didn't work\n")
        print(e.__doc__)
        print(e.message)


if __name__ == "__main__":
    subject = "OMG. You MUST read this attachment."
    # for single email
    # to_address = "4brianbirmingham@gmail.com"
    # for multiple destinations
    to_address = ["4brianbirmingham@gmail.com"]
    cc_address = ["brian.birmingham@gmail.com"]
    bcc_address = ["4brianbirmingham@gmail.com"]
    body_text = "Hey.  Hey.  Hey.  See attachment."
    path = "attachment.txt"
    send_email_with_attachment(subject, to_address, cc_address, bcc_address, body_text, path)
