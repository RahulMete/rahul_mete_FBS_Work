# Sum of Digits of a Number

def sum_digit(num):
    sum = 0
    
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    
    return sum

n = int(input('Enter n:'))

print('sum of digit =', sum_digit(n))