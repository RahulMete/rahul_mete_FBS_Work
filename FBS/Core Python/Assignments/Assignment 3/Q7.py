# Write a program to check if user has entered correct userid and password.

user_id = input("Enter a user ID ")
password = input("Enter a password ")

if user_id == "Admin" and password == "1234":
    print("Login successful")
    
else:
    print("Incorrect user id or password")