# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# # 4*4*4*4)

n = int(input("Enter number: "))

temp = n
digits = len((str(n)))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10 
    
if sum == n:
    print("Armstrong Number ")
else: 
    print("Not Armstrong Number ")
    
#OR

num = int(input('Enter number : '))
temp = num
count = 0

while(temp>0):
    count += 1
    temp = temp // 10 

    
temp = num
sum = 0
while(temp>0):
    d = temp % 10
    temp = temp // 10
    sum = sum + (d ** count)

    
if(sum == num):
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not armstrong number')