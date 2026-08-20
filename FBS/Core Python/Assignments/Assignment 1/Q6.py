#Write a Program to input two angles from user and find third angle of the triangle.

Angle1 = float(input("Enter first angle:"))
Angle2 = float(input("Enter second angle:"))

Angle3 = 180 - (Angle1 + Angle2)

print("The third angle is:", Angle3)
