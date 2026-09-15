# Write a program to calculate the sum of following series where n is input by user.
# # 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

n = int(input('Enter N:'))

sum = 0
fact = 1
i = 1

while i <= n:
    
    fact = fact * i
    sum = sum + i / fact 
    
    i += 1
    
print("sum=", sum)