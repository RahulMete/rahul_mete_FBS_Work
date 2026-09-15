# 1. Write a program to calculate area of rectangle   

def area_reactangle(length, breadth):
    area = length * breadth 
    return area

l =  float(input('Enter length:'))
b = float(input('Enter breadth:'))

print('Area of reactangle=', area_reactangle(l,b))