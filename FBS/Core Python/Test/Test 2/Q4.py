# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

l = int(input('Enter length:'))
h = int(input('Enter height:'))
b = int(input('Enter breadth:'))
rate = float(input('Enter painting rate:'))

area = 2 * h * (l + b)
cost = area * rate

print('area of four walls =', area)
print('cost of painting =', cost)