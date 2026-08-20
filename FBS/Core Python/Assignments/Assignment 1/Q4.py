#Write a program to enter P, T, R and calculate simple Interest.

P = float(input("Enter principal amount(P)"))
T = float(input("Enter time (T)"))
R = float(input("Enter rate of interest (R)"))

SI = P * T * R / 100

print("Simple interest =", SI)