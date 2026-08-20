#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic = float(input("Enter Basic salary of employee:"))

da = (10/100)* basic
ta = (12/100)* basic
hra = (15/100)* basic

total_salary = basic + da + ta + hra

print("total salary of employee is:", total_salary) 
