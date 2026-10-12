def factorial(n):
    if n < 0:
        return "factorial does not exist for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = 10
result = factorial(num)
print(f"factorial of {num} is {result}")