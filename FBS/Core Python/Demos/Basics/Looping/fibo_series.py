num = int(input('How many fibonacci numbers you want:'))

a = -1
b = 1

for i in range(num):
    c = a + b
    print(c, end = "_")
    a = b 
    b = c