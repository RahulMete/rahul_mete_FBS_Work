# TYPE 1


# def prime():
#     n = int(input('Enter a number:'))
   
#     if (n % 2 == 0): 
#        print('False')
#     else:
#         print('True')
  
# prime()





# TYPE 2


# def prime(n):
#     if (n % 2 == 0):
#         print('False')
#     else:
#         print('True')
        
# n = int(input('Enter number: '))
# prime(n)





# TYPE 3

# def prime():
#     num = int(input('Enter a number:'))
#     flag = True
    
#     if num % 2 == 0:
#         flag = False
        
#     return flag

# res = prime()
# print(res)




#TYPE 4

def prime(num):
    flag = True
    
    if num % 2 == 0:
        flag = False
    
    return flag

num = int(input('Enter a number:'))
res = prime(num)
print(res)