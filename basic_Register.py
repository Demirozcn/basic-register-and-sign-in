# Written by Demir https://github.com/demirozcn/basic-register-and-sign-in
test = True
blank = ''
register_email = True

#The test = True is just for loops if you wonder

while test == True:
    register_email = input('Please enter your email address: ')
    if '@' in register_email:
        pass
    else:
        print('Invalid email')
        continue

    if '.' in register_email:
         break
    else:
        print('Invalid email')



register_username = True

while test == True:
    register_username = input('Please enter a username: ')
    if len(register_username) > 3:
       break
    else:
        print('invalid username')


register_password = True

while test == True:
    register_password = input('Now please enter a password: ')
    if len(register_password) < 8:
        print('Password length needs to be at least 8 characters')
        continue
    else:
        break

password_confirmation = True

while test == True:
    password_confirmation = input('Please confirm your password: ')
    if password_confirmation == register_password:
        print('You registered successfully! Please sign in now.')
        break
    else:
        print('Passwords doesnt match')
        continue

# Signing in

print('Welcome to the sign in screen.')

email = True

while test == True:
    email = input('Please enter your email: ')
    if email == register_email:
        break
    else:
        print('Sign in failed please check your email')
        continue

password = True

while test == True:
    password = input('Please enter your password: ')
    if password == register_password:
        break
    else:
        print('Sign in failed please check your password')
        continue


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

verification = True

while test == True:
    verification = input('Please enter the verification code we sent you via email: ')
    if verification == str(verification_num):
        print('Code is correct sign in successful')
        break

    else:
        print('Code is incorrect sign in failed')
        continue
