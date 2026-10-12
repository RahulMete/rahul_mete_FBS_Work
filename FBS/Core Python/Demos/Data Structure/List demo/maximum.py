#write a program to find out maximum number in the given list

li = [40, 50, 30, 60, 20, 10]

max =li[0]

for ind in range(1, len(li)):
    if (li[ind] > max):
        max = li[ind]
        
        
print('Maximum number:', max)