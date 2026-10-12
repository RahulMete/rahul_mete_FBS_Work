def print_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))
    
    print(f"Factors of {num} : {', '.join(factors)}")


print_factors(12)