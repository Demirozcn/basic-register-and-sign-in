#Written by Demir https://github.com/Demir017/basic-register-and-sign-in

# Register
blank = ''
signin_username = input('Please enter a username: ')

#Username lenght check
if len(signin_username) < 3:
    print('Username lenght needs to be at least 3 characters')
    exit()

#If the username is blank exit the code
if signin_username == blank:
    print('username cant be empty')
    exit()

signin_password = input('Now please enter a password: ')

#Password lenght check
if len(signin_password) < 8:
    print('Password lenght needs to be at least 8 characters')
    exit()

#if the password is blank exit the code
if signin_password == blank:
    print('username cant be empty')
    exit()

#Password double check for in case of any typos
password_confirmation = input('Please confirm your password: ')
if password_confirmation == signin_password:
    print('You registered succesfully! Please sign in now.')

#Exit the code if the passwords doesnt match
else:
    print('Passwords doesnt match')
    exit()


# Signing in
print('Welcome to the sign in screen.')
username = input('Please enter your username: ')
password = input('Please enter your password: ')

if username == signin_username and password == signin_password :
    print('Sign in succesful')

else:
    print('Sign in failed. Please check your password')