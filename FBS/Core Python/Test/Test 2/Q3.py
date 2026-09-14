# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

import math 

r = 20
l = 50
b = 40

perimeter = 2* l + 3.14 * r
wire = perimeter * 5
cost = wire * 35

print("Total cost of fencing =", cost)