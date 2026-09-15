# heck Whether Number is Armstrong Number or Not

def armstrong(num):
    original = num
    digits = len(str(num))
    sum = 0 
    
    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10
        
    if sum == original:
        return True
    else:
        return False
    
n = int(input('Enter n: '))

if armstrong(n):
    print('Number is armstrong')
else:
    print('Number is not armstrong')