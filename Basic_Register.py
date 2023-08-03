# Written by Demir https://github.com/Demir017/basic-register-and-sign-in

# Register
blank = ''
register_email = input('Please enter your email address: ')

if '@' not in register_email:
    print('Invalid email')
    exit()

if '.' not in register_email:
    print('Invalid email')
    exit()

if register_email == blank:
    print('Email address cannot be left blank')

register_username = input('Please enter a username: ')

# Username length check
if len(register_username) < 3:
    print('Username length needs to be at least 3 characters')
    exit()

# If the username is blank exit the code
if register_username == blank:
    print('username cant be empty')
    exit()

register_password = input('Now please enter a password: ')

# Password length check
if len(register_password) < 8:
    print('Password length needs to be at least 8 characters')
    exit()

# if the password is blank exit the code
if register_password == blank:
    print('username cant be empty')
    exit()

# Password double check for in case of any typos
password_confirmation = input('Please confirm your password: ')
if password_confirmation == register_password:
    print('You registered successfully! Please sign in now.')

# Exit the code if the passwords doesn't match
else:
    print('Passwords doesnt match')
    exit()

# Signing in

print('Welcome to the sign in screen.')
email = input('Please enter your email: ')
password = input('Please enter your password: ')

import random

verification_num = random.randint(000000, 999999)

from email.message import EmailMessage
import ssl
import smtplib

email_sender = '' # this is the email address that you will send the verification codes (must be a gmail account)
email_password = '' # this is the Google accounts app password. check this video if you don't know what to do https://www.youtube.com/watch?v=g_j6ILT-X0k
email_receiver = register_email

subject = 'Email verification code'
body =f'''Hello {register_username} your 2-step verification code is {verification_num}
Please do not share this code with anybody.'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


if email == register_email and password == register_password:
    print('Password is correct')

else:
    print('Sign in failed please check your email or password')
    exit(
    )

verification = input('Please enter the verification code we sent you via email: ')

if verification == str(verification_num):
    print('Code is correct sign in successful')

else:
    print('Code is incorrect sign in failed')
    exit()
