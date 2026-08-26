# num = int(input('Enter number'))

# while(num > 0):
#     d = num % 10
#     print(d)
#     num = num // 10
    
    

num = int(input("Enter number"))

sum = 0 
while(num > 0):
    d = num % 10
   # print(d)
    sum += d    # sum = sum + d
    num = num // 10
print(sum)