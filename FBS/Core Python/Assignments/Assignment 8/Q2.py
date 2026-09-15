# 2. Write a program to calculate area of circle

def area_circle(radius):
    area = 3.14 * radius * radius
    return area

r = float(input("Enter a radius:"))

print('Area of circle =', area_circle(r))