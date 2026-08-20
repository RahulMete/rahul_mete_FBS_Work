#Find the sum of three-digit number.

num = int(input("Enter a three-digit number:"))

a = num // 100                 #EX:- Hundreds digit = 456 // 100 = 4
b = (num // 10)% 10            #Tens digit = (456 // 10) % 10 = 5
c = num % 10                   #units digit = 456 % 10 = 6              sum= 4+5+6=15

sum = a + b + c

print("sum of digits =", sum)
    