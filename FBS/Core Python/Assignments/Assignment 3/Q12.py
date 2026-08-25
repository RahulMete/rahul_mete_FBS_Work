# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))

if num >= 100 and num <= 999:
    if(num // 100) == (num % 10):
        print("Number is palidrome")
    else: 
        print("Number is not palidroome")
else:
    print("Enter a 3 digit number")