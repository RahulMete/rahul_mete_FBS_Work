# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n



# A)
# def sum_series(n):
#     sum = 0 
    
#     for i in range(1, n + 1):
#         sum = sum + i
        
#     return sum

# n = int(input('Enter n: '))

# print("sum =", sum_series(n))



# B)
# def factorial(num):
#     fact = 1 
    
#     for i in range(1, num + 1):
#         fact = fact * i
        
#     return fact

# def sum_factorial(n):
#     sum = 0
    
#     for i in range(1, n + 1):
#         sum = sum + factorial(i)
        
#     return sum 

# n = int(input('Enter n:'))

# print('sum =', sum_factorial(n))



# C)

def sum_power(n):
    sum = 0
    
    for i in range(1, n + 1):
        sum= sum + i ** i 
        
    return sum

n = int(input('Enter n: '))

print('sum =', sum_power(n))