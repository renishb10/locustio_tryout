import smtplib
from . import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail(object):
    def Send(self, to_emailids = [], messageHtml = ""):
        
        try:
            #My Email configuration
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Link"
            msg['From'] = config.EMAIL_ADDRESS

            for emailId in to_emailids:
                msg['To'] = emailId

                text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
                html = messageHtml
                print(html)

                part1 = MIMEText(text, 'plain')
                part2 = MIMEText(html, 'html')

                msg.attach(part1)
                msg.attach(part2)

                # Send the message via local SMTP server.
                s = smtplib.SMTP('smtp.gmail.com')
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
                # sendmail function takes 3 arguments: sender's address, recipient's address
                # and message to send - here it is sent as one string.
                s.sendmail(config.EMAIL_ADDRESS, emailId, msg.as_string())
                s.quit()
        
        except Exception as ex:
            print(ex)