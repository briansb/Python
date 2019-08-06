# https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
# and had to change a GMail setting....Allow less secure apps

import os
import smtplib
import sys

from configparser import ConfigParser

def send_email(subject, to_address, cc_address, bcc_address, body_text):
    # program location
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

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
    
    BODY = "\r\n".join((
        "From: %s" % from_address,
        # for single email
        #"To: %s" % to_address,
        # for multiple destination addresses
        "To: %s" % ', '.join(to_address),
        "CC: %s" % ', '.join(cc_address),
        "BCC: %s" % ', '.join(bcc_address), 
        "Subject: %s" % subject,
        "",
        body_text))
    # I'm not sure why we have to combine them
    emails = to_address + cc_address + bcc_address
    print(BODY)

    try:
        server = smtplib.SMTP_SSL(host, 465)
        server.ehlo()
        server.login(email_user, email_password)
        server.sendmail(from_address, emails, BODY)
        server.close()
        print('Email sent!')
    except Exception as e:
        print("Didn't work\n")
        print(e.__doc__)
        print(e.message)


if __name__ == "__main__":
    subject = "OMG. You MUST read this."
    # for single email
    # to_address = "4brianbirmingham@gmail.com"
    # for multiple destinations
    to_address = ["4brianbirmingham@gmail.com"]
    cc_address = ["brian.birmingham@gmail.com"]
    bcc_address = ["4brianbirmingham@gmail.com"]
    body_text = "Hey.  Hey.  Hey."
    send_email(subject, to_address, cc_address, bcc_address, body_text)
