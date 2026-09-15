def sum_series(num):
    sum = 0
    for i in range(1, num + 1):
        fact = 1
        
        for j in range(1, i + 1):
            fact = fact * j
        sum = sum + fact
        
    return sum
    
num = int(input('Enter a number :'))
res = sum_series(num)
print(res)