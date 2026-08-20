#Program to Find the Roots of a Quadratic Equation

a = float (input("Enter a:"))
b = float (input("Enter b:"))
c = float (input("Enter c:"))

#calculate the discriminant
d = b**2 - 4*a*c 

#calculates roots

if d > 0:
    root1 = (-b + d**0.5)/(2*a)
    root2 = (-b - d**0.5)/(2*a)
     
    print("the eroots are  real and different")
    print("root1 is:", root1)
    print("root2 is:", root2)

elif d == 0:
  
  root = -b / (2*d)
  print("the roots are real and equal")
else:
  print("the roots are complex:")