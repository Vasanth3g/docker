__author__ = 'srv'

import smtplib
from datetime import date
from datetime import time
from datetime import datetime
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = 'u.u.u.u'  # Email Address from the email you want to send an email
password = 'p.p.p.p'  # Password
server = smtplib.SMTP('outlook.office365.com:587')

"""
SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.
"""

# Create the body of the message (a HTML version for formatting).
html = """<html>\n<body><p>Please find the apk file and build report in  attachment.</p><br/><br/><br/><br/><br/><br/><br/>Thanks <br/> Support Team</b> \n<br/><br/><br/><img src="http://50.234.9.225/stage_softwares/logo.jpg" width="130" height="90"><br/>\n<br/><b>Mail System | Support Team \n<br/><b>Evolution Digital (India) Pvt Ltd | evolutiondigital.com </b><br/>SKCL Design Square, 3rd Floor, S11 &12 <br/>Thiru Vi ka Industrial Estate, Guindy | Chennai - 600032 <p style = "font-family:georgia,garamond,serif;font-size:12px;font-style:italic;" >The information in this message is confidential and may be legally privileged. If you are not the intended recipient,  you may not use it or disclose it to others. If you have received this message in error, please notify me immediately.</p>\n</body>\n</html> """


# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg):
    server = smtplib.SMTP('outlook.office365.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

# Read email list txt
#email_list = [line.strip() for line in open('email.txt')]
list="t.t.t.t"
email_list=list.split(" ")

for to_addrs in email_list:
    msg = MIMEMultipart()
    from_addr='u.u.u.u'
    temp = datetime.time(datetime.now())
    msg['Subject'] = "APK BUILD SUCCEED {}".format(temp)
    msg['From'] = from_addr
    msg['To'] = to_addrs

    # Attach HTML to the email
    body = MIMEText(html, 'html')
    msg.attach(body)

    # Attach Cover Letter to the email
    cover_letter = MIMEApplication(open("app/build/outputs/apk/release/app-release-unsigned.apk", "rb").read())
    #cover_letter = MIMEApplication(open("file1.pdf", "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename="app-release-unsigned.apk")
    msg.attach(cover_letter)

    # Attach Resume to the email
    cover_letter = MIMEApplication(open("app/build/reports/lint-results.html", "rb").read())
    #cover_letter = MIMEApplication(open("file2.pdf", "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename="reports.html")
    msg.attach(cover_letter)

    try:
    	send_mail(username, password, from_addr, to_addrs, msg)
    	print "Email successfully sent to", to_addrs
    except SMTPAuthenticationError:
        print 'SMTPAuthenticationError'
        print "Email not sent to", to_addrs
    #except SMTPException:
    #    print('error')
