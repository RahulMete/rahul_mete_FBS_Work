#Write a program to swap two numbers using third variable.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(f'Before swapping: a = {a}, b = {b}')
c = a 
a = b
b = c

print(f'After swapping: a = {a}, b = {b}')

#print("after swapping:", a)
#print("first number is:", a)
#print("second number is:", b)

