#WAP to calculate area of triangle and rectangle

#area of triangle
base = float(input("Enter base of triangle:"))
height = float(input("Enter height of triangle:"))

triangle_area = (base * height) /  2

#area of rectangle
lenght = float(input("Enter length of rectangle:"))
width = float(input("Enter width of rectangle:"))

rectangle_area = (lenght * width)

#print("Area of triangle is:", triangle_area)
#print("Area of rectangle is:", rectangle_area)
print(f'Area of triangle is: {triangle_area} and Area of rectangle is: {rectangle_area}')