#TYPE 1

# def palindrome():
#     n = int(input('Enter a number:'))
#     original=n
#     reverse = 0
    
#     while(n>0):
#         d = n % 10
#         reverse = reverse*10+d
#         n = n//10
#     if(original == reverse):
#         print(True)
#     else:
#         print(False)
        
# palindrome()



###TYPE 2


# def palindrome(n):
   
#     original=n
#     reverse = 0
    
#     while(n>0):
#         d = n % 10
#         reverse = reverse*10+d
#         n = n//10
#     if(original == reverse):
#         print(True)
#     else:
#         print(False)
        
# n = int(input('Enter a number:'))
# palindrome(n)



###TYPE #


# def palindrome():
#     n = int(input('Enter a number:'))
   
#     original=n
#     reverse = 0
    
#     while(n>0):
#         d = n % 10
#         reverse = reverse*10+d
#         n = n//10
#     if(original == reverse):
#         return(True)
#     else:
#         return(False)
        
# res = palindrome()
# print(res)




#### TYPE 4


def palindrome(n):
   
    original=n
    reverse = 0
    
    while(n>0):
        d = n % 10
        reverse = reverse*10+d
        n = n//10
    if(original == reverse):
        return(True)
    else:
        return(False)
        
n = int(input('Enter a number:'))
res = palindrome(n)
print(res)