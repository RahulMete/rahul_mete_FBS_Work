# Write a program to accept year from user and check if it is a leap year or not.

year = int(input('Enter a year: '))

if year % 400 == 0:
    print("Leap year")
elif year % 200 == 0:
    print('Not Leap Year')
elif year % 4 == 0:
    print("Leap Year")
else:
    print('Not Leap Year')   