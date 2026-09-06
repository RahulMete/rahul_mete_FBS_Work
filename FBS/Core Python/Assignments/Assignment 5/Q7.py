# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

#  A )

# n = int(input('Enter number: '))
   
# fact = 1
# total = 0

# for i in range(1, n + 1):
#     fact = fact * i
#     total = total + fact
    
# print('Sum=', total) 


# B )

# n = int(input('Enter a number: '))  

# total = 0 

# for i in range(1 , n + 1):
#     total = total + (n ** i)
    
# print("sum=", total)


# C )

# n = int(input('Enter number: '))

# total = 0 
# term = 1

# for i in range(n):
#     total = total + term 
#     term = term * 2
    
# print('sum=', total)


#D )

# a = int(input("Enter a: "))

# total = 0

# for i in range(1, 11):
#     total = total + (a ** i) / i

# print("S =", total)


# E)
x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))

total = 0

for i in range(1, n + 1):
    term = (x ** i) / (2 * i - 1)

    if i % 2 == 0:
        total = total - term
    else:
        total = total + term

print("S =", total)