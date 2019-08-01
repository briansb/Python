# https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
# and had to change a GMail setting....Allow less secure apps

import smtplib

gmail_user = '4brianbirmingham'
gmail_password = 'Luger9mm'

sent_from = gmail_user
to = ['brian.birmingham@odysseysr.com', '4brianbirmingham@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, whats up?\n\n- This is a test message'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except Exception as e:
    print("Didn't work\n")
    print(e.__doc__)
    print(e.message)
