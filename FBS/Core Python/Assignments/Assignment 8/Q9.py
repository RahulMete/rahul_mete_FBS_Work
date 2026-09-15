# Check Whether Number is Palindrome or Not

def reverse_number(num):
    reverse = 0
    
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
        
    return reverse

def palindrome(num):
    rev = reverse_number(num)
    
    if num == rev:
        return True 
    else:
        return False
    
n = int(input('Enter n: '))

if palindrome(n):
    print('number is palindrome')
else:
    print('NUmber is not palindrome')