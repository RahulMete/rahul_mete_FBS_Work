for i in range(4):

    num = 1

    # 1. Spaces
    for j in range(4 - i - 1):
        print("  ", end="")


    for j in range(i + 1):
        print(num, end="   ")

        
        num = num * (i - j) // (j + 1)            # 3. Calculate next number

    print()