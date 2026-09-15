# 3. Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

emp = int(input("Enter number of employees: "))

count = 1
grand_total = 0

while count <= emp:

    bs = float(input("Enter basic salary: "))

    if bs < 20000:
        da = bs * 10 / 100
        ta = bs * 12 / 100
        hra = bs * 15 / 100
    else:
        da = bs * 15 / 100
        ta = bs * 18 / 100
        hra = bs * 20 / 100

    net_salary = bs + da + ta + hra

    print("Employee", count, "Total Salary =", net_salary)

    grand_total = grand_total + net_salary
    count = count + 1

print("Total Salary of All Employees =", grand_total)