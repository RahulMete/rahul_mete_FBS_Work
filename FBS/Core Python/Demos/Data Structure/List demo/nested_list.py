# li = [10, 20, [30,[40, 50, 60,]], 70 ]

# print(li[2][0])
# print(li[2][1][1])


#### Homework
#li = [[10, 20], [30,40], [50, 60]]
# li = [5, [10, 20,], [30, 40], [50, 60]]

# WAP to calculate sum of all element 

# li = [[10, 20], [30,40], [50, 60]]


# sum = (li[0][0]+li[0][1] + li[1][0]+li[1][1] + li[2][0]+li[2][1])
# print(sum)
# print(len(li))


li = [5, [10, 20,], [30, 40], [50, 60]]

sum = (li[0] + li[1][0]+li[1][1] + li[2][0]+li[2][1] + li[3][0]+li[3][1])
print(len(li))
print(sum)