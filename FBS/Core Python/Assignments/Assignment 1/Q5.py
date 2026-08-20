#Write a program to enter P, T, R and calculate Compound Interest.

P = float(input("Enter principal amount (P): "))
T = float(input("Enter time (T): "))
R = float(input("Enter the rate of interest (R): "))

CI = P * (1 + R/100)**T - P

print("Compound interest =", CI)
