#Write a program to swap two numbers without using third variable.

x = int(input("Enter first number"))
y = int(input("Enter second number"))

print(f'before swapping x:{x}, y:{y}.')

x, y=y,x

print(f'after swapping x:{x}, y:{y}')
