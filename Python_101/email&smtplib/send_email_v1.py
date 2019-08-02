# https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
# and had to change a GMail setting....Allow less secure apps

import smtplib

def send_email(host, subject, to_address, from_address, body_text):
    BODY = "\r\n".join((
        "From: %s" % from_address,
        "To: %s" % to_address,
        "Subject: %s" % subject,
        "",
        body_text))

    try:
        server = smtplib.SMTP_SSL(host, 465)
        server.ehlo()
        gmail_user = '4brianbirmingham'
        gmail_password = 'Luger9mm'
        server.login(gmail_user, gmail_password)
        server.sendmail(from_address, [to_address], BODY)
        server.close()
        print('Email sent!')
    except Exception as e:
        print("Didn't work\n")
        print(e.__doc__)
        print(e.message)


if __name__ == "__main__":
    host = "smtp.gmail.com"
    subject = "OMG. You MUST read this."
    to_address = "4brianbirmingham@gmail.com"
    from_address = "4brianbirmingham@gmail.com"
    body_text = "Hey.  Hey.  Hey."
    send_email(host, subject, to_address, from_address, body_text)
