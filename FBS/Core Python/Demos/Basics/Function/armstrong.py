#TYPE 1


# def armstrong():
#     n = int(input('Enter number: '))
#     temp = n
#     count = 0
    
#     while temp > 0:
#         count += 1
#         temp = temp // 10
        
#     temp = n
#     total = 0
    
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         total = total + (d ** count)
        
#     if total == n:
#         print(True)
#     else:
#         print(False)
      
# armstrong()



### TYPE 2


# def armstrong(n):
#     temp = n
#     count = 0
    
#     while temp > 0:
#         count += 1
#         temp = temp // 10
        
#     temp = n
#     total = 0
    
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         total = total + (d ** count)
        
#     if total == n:
#         print(True)
#     else:
#         print(False)

# n = int(input('Enter number: '))
# armstrong(n)





#### TYPE 3

# def armstrong():
#     n = int(input('Enter number: '))
#     temp = n
#     count = 0
    
#     while temp > 0:
#         count += 1
#         temp = temp // 10
        
#     temp = n
#     total = 0
    
#     while temp > 0:
#         d = temp % 10
#         temp = temp // 10
#         total = total + (d ** count)
        
#     if total == n:
#         return(True)
#     else:
#         return(False)

# res = armstrong()
# print(res)




#### TYPE 4

def armstrong(n):
    
    temp = n
    count = 0
    
    while temp > 0:
        count += 1
        temp = temp // 10
        
    temp = n
    total = 0
    
    while temp > 0:
        d = temp % 10
        temp = temp // 10
        total = total + (d ** count)
        
    if total == n:
        return(True)
    else:
        return(False)

n = int(input('Enter number: '))
res = armstrong(n)
print(res)