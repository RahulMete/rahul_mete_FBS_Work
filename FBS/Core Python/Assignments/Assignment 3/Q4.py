#Write a program to input all sides of a triangle and check whether triangle is valid or not.

A = int(input('Enter first side'))
B = int(input('Enter second side'))
C = int(input('Enter third side'))

if A + B > C and A + C > B and B + C > A: 
    print("Triangle is valid")
else:
    print("Triangle is not valid")