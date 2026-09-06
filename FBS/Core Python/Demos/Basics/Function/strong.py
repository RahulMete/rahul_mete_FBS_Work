#### TYPE 1

# def strong():
#     n = int(input("Enter a number: "))

#     temp = n 
#     sum = 0

#     while temp > 0:
#         digit = temp % 10 
    
#         fact = 1
#         for i in range(1, digit + 1):
#             fact = fact * i
        
#         sum = sum + fact
#         temp = temp // 10
    
#     if sum == n:
#         print("True")
#     else:
#         print("False")
        
# strong()
    
    

##### TYPE 2

# def strong(n):
    

#     temp = n 
#     sum = 0

#     while temp > 0:
#         digit = temp % 10 
    
#         fact = 1
#         for i in range(1, digit + 1):
#             fact = fact * i
        
#         sum = sum + fact
#         temp = temp // 10
    
#     if sum == n:
#         print("True")
#     else:
#         print("False")

# n = int(input("Enter a number: "))    
# strong(n)





####TYPE 3

# def strong():
#     n = int(input("Enter a number: "))

#     temp = n 
#     sum = 0

#     while temp > 0:
#         digit = temp % 10 
    
#         fact = 1
#         for i in range(1, digit + 1):
#             fact = fact * i
        
#         sum = sum + fact
#         temp = temp // 10
    
#     if sum == n:
#         return("True")
#     else:
#         return("False")
        
# res=strong()
# print(res)



#### TYPE 4

def strong(n):
   

    temp = n 
    sum = 0

    while temp > 0:
        digit = temp % 10 
    
        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i
        
        sum = sum + fact
        temp = temp // 10
    
    if sum == n:
        return("True")
    else:
        return("False")
    
n = int(input("Enter a number: "))
res=strong(n)
print(res)