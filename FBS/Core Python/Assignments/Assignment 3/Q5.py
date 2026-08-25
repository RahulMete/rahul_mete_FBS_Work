#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = int(input('Enter first side:'))
side2 = int(input('Enter second side:'))
side3 = int(input('Enter third side'))

if side1 == side2 == side3:                                      #All three side equal means triangle is Equilateral
    print("Triangle is equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:         #If two side are equal means triangle is isosceles
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")                                 #If all sides are different means triangle is scalene