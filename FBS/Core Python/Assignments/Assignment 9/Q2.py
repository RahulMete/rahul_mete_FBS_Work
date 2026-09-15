# 2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrong(num):
    sum = 0
    temp = num
    
    while(temp > 0):
        d = temp % 10
        sum = sum + d ** 3
        temp = temp // 10
        
    if num == sum:
        print("Number is armstrong")
    else:
        print("number is not armstrong")
        
    return sum
    
num = int(input("enter number: "))
res = armstrong(num)
print(res)