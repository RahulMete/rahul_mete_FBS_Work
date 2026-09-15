# Write a program to find sum of n numbers using recursion.

def sum_num(n):
    
    if(n == 0):
        return 0
    
    for i in range(1, 2):
        return n + sum_num(n - 1)
    
n = int(input('Enter a number:'))

res = sum_num(n)
print(res)