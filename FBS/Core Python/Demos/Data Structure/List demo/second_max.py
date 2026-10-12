# second max 

li = [40, 50, 30, 60, 20, 10]

max = li[0]
smax = 0

for ind in range(1, len(li)):
    if (li[ind]> max):
        smax = max
    elif(li[ind]>smax):
        smax = li[ind]
        
print('max:', max)
print('smax:', smax)




# #Third Max number 

# li = [40, 50, 30, 60, 20, 10]

# max =li[0]
# sec_max = 0
# tmax = 0

# for ind in range(1, len(li)):
#     if(li[ind] > max):
#         tmax = sec_max
#         sec_max = max
#         max = li[ind]
        
#     elif (li[ind] > sec_max):
#             tmax = sec_max
#             sec_max = li[ind]
            
#     elif (li[ind] > tmax):
#             tmax = li[ind]
                

# print('Maximum number:', max)
# print('sec_max:', sec_max)
# print('tmax:', tmax)