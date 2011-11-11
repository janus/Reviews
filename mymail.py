#!/usr/bin/env python

import smtplib
import urllib
from mydatamodel import helper

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "ffffff@gmail.com"  #config
#you = "bbbbb@yahoo.com"

username = "newcity" #config
password = "7777"  #config

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Activation Mail"
msg['From'] = me

# Create the body of the message (a plain-text and an HTML version).
def get_message(username, my_hash):
	html = 	"""\
					<html>
					<head>Activation Mail</head>
					<body>
					<p>Hi  %s!<br>
					Please click here to activate your account <a href="http://localhost:8080/activation? %s">Click me</a> . You may also  copy and paste  http://localhost:8080/activation?%s" .
					</p> </body> </html>""" % (username,  my_hash, my_hash)
	return html
	

def send_mail(name, email, activation_code =None):
		# Record the MIME types of both parts - text/plain and text/html.
		#part1 = MIMEText(text, 'plain')
		if activation_code:
			part2 = MIMEText(get_message(name, urllib.urlencode({'activate':activation_code})) , 'html')
		else:
			part2 = None #To do
		msg['To'] = email
		msg.attach(part2)
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.starttls()
		s.login(username, password)
		s.sendmail(me, email, msg.as_string())
		s.quit()



