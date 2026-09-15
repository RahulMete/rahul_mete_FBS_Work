# Write a program to print Fibonacci series using recursion.

def fibonacci(a,b,n):
    
    if(n > 0):
        print(a, end=' ')
        fibonacci(b, a+b, n-1)
        
n = int(input('Enter number of terms:'))

fibonacci(1, 1, n )