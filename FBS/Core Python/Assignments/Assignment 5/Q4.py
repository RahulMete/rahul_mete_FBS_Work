# WAP to print Armstrong number within a given range

start = int(input('Enter starting number: '))
end = int(input('Enter ending number: '))

for num  in range(start, end + 1):
    temp = num
    count = 0
    
    while temp > 0:
        count += 1
        temp = temp // 10
        
    temp = num
    total = 0
    
    while temp > 0:
        d = temp % 10
        temp = temp // 10
        total = total + (d ** count)
        
    if total == num:
        print(num)