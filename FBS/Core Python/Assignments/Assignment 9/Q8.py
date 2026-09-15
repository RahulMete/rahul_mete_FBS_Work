# Write a program to check whether a number is prime or not using recursion.

def prime(num, i):
    
    if (i == num):
        return True
    
    if (num % i == 0):
        return False
    
    return prime(num, i + 1)

n = int(input('Enter a number'))

res = prime(n, 2)

if(res):
    print('Number is prime')
else:
    print('Number is not prime')