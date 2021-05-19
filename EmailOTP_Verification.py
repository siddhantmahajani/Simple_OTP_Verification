import os
import math
import random
import smtplib
from email.mime.text import MIMEText

digits = "0123456789"

OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

fromEmail = '{fromEmail}'

mailServer = smtplib.SMTP('{host}', '{port}')
mailServer.starttls()
mailServer.login('{authenticationId}', '{authenticationPassword}')
toEmail = input('Please enter your email: ')
otpMimeMessage = MIMEText(OTP + " is your One Time Password. Please do not share it with anyone.")
otpMimeMessage['Subject'] = 'One time password'
otpMimeMessage['From'] = fromEmail
otpMimeMessage['To'] = toEmail
mailServer.sendmail(fromEmail, toEmail, otpMimeMessage.as_string())

otp = input('Enter your OTP: ')
if otp == OTP:
    print('Verification successful!')
else:
    print("Invalid OTP. Please enter valid OTP.")
