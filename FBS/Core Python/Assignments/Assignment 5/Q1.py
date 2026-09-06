# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# # times. After that program to terminate.

userid = "admin"
password = "1234"


uid = input('Enter user id: ')
pwd = input('Enter password: ')

for attempts in range(3):
    if userid == uid and password == pwd:
        print('Loginn succesful')
        break
    else:
        print('Invalid user ID or Password')

else:
    print("3 attempts completed. Program terminated.")