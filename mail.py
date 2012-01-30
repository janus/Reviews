#!/usr/bin/env python

import smtplib
import urllib
from model.model  import helper

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address

#username = "" Add your mail's username
#sender_password =  "" Password here

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Activation Mail"
msg['From'] = me

# Create the body of the message (a plain-text and an HTML version).
def update_message(username):
  html = 	"""\
					<html>
					<head>Password Update</head>
					<body>
					<p>Hi  %s!<br>
					Please note that your password was update. If you are not the one that carried out this task, go now and reset your password
					</p> </body> </html>""" % (username,  )
  return html


def activation_message(username, my_hash):
  html = 	"""\
					<html>
					<head>Activation Mail</head>
					<body>
					<p>Hi  %s!<br>
					Please click here to activate your account <a href="http://localhost:8080/activation? %s">Click me</a> . You may also  copy and paste  http://localhost:8080/activation?%s" .
					</p> </body> </html>""" % (username,  my_hash, my_hash)
  return html
	
def get_password_message(password):
  html = 	"""\
					<html>
					<head>Password Reset</head>
					<body>
					<p>
					Please note that a new password was sent to your box,
					%s</p></body> </html>""" % (password,  )
  return html

def send_mail( email,name = None,activation_code =None, password=None):
		# Record the MIME types of both parts - text/plain and text/html.
		#part1 = MIMEText(text, 'plain')
  if activation_code and name:
    part2 = MIMEText(activation_message(name, urllib.urlencode({'activate':activation_code})) , 'html')
  elif name and password is None:
    part2 =  MIMEText(update_message(name) , 'html')#To do
  else:
    part2 =  MIMEText(get_password_message(password), 'html')
  msg['To'] = email
  msg.attach(part2)
  s = smtplib.SMTP('smtp.gmail.com:587')
  s.starttls()
  s.login(username, sender_password)
  s.sendmail(me, email, msg.as_string())
  s.quit()

#print helper.activation_hash()
#print urllib.urlencode({'coot' : helper.activation_hash()})
#send_mail(email="emekamicro@gmail.com", name="88999")
# Attach part message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)

