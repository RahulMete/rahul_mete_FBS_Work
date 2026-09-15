# Write a program to find sum of digits using recursion.

def sum_digit(num):
    sum = 0
    
    while(num>0):
        d = num % 10
        sum = sum + d
        num = num // 10
        break
    
    if(num == 0):
        return sum
    
    return sum + sum_digit(num)

num = int(input('Enter numer:'))
res = sum_digit(num)
print(res)