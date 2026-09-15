# Write a program to reverse a given number using recursive function.

def reverse(num, rev):

    while(num > 0):
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
        break

    if(num > 0):
        return reverse(num, rev)
    else:
        return rev


num = int(input("Enter a number: "))

res = reverse(num, 0)

print("Reverse =", res)