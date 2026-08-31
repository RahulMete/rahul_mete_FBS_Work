# 1. WAP to print all even numbers until n.

n = int(input('Enter n: '))

for i in range(2, n + 1, 2):
    print(i)
    
    
#OR 


n = int(input("Enter n: "))

i = 2
while i <= n:
    print(i)
    i += 2