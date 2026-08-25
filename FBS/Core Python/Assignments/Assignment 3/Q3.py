#Write a program to input angles of a triangle and check whether triangle is valid or not.

A1= int(input('Enter the first angle:'))
A2= int(input('Enter the second angle:'))
A3= int(input('Enter the third angle:'))

sum=A1+A2+A3

if sum == 180:
    print('Valid Triangle')
else:
    print('Triangle is not valid')