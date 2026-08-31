# 9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter a starting Number: "))
end = int(input("Enter a ending Number: "))
n = int(input("Enter a number to divide by: "))

for i in range(start, end + 1):
    if i % n == 0:
        print(i)