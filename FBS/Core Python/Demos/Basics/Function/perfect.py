#### TYPE 1

# def perfect():
#     n = int(input("Enter a Number: "))

#     sum = 0

#     for i in range(1, n):
#         if n % i == 0:
#             sum = sum + i
        
#     if sum == n:
#         print("True")
#     else:
#         print("False")
        
# perfect()




#### Type 2

# def perfect(n):
    
#     sum = 0
    
#     for i in range(1,n):
#         if n % i == 0:
#             sum = sum + i
    
#     if sum == n:
#         print('True')
#     else:
#         print('False')

# n = int(input('Enter a number:'))
# perfect(n)




#### TYPE 3

# def perfect():
#     n = int(input('Enter a number:'))
#     sum = 0
    
#     for i in range(1,n):
#         if n % i == 0:
#             sum = sum + i
    
#     if sum == n:
#         return('True')
#     else:
#         return('False')


# res=perfect()
# print(res)



##### TYPE 4


def perfect(n):
    
    sum = 0
    
    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    
    if sum == n:
        return('True')
    else:
        return('False')

n = int(input('Enter a number:'))
res=perfect(n)
print(res)