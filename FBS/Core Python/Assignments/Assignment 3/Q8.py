# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
userID = input("Enter the user Id= ")
password = input("Enter the password= ")

if userID =="Admin@1" and password == "0007":
    systemcaptcha=random.randint(1000,10000)
    print(systemcaptcha)
    captcha=int(input("Enter the captcha "))
    if captcha==systemcaptcha:
        print("Succesfully log in ")
    else:
        print("Invalid captcha ")
else:
    print("Invalid ID and password")
          
    