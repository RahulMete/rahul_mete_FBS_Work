for i in range(1, 5):

    for j in range(1, 6 - i):
        print(' ', end=' ')

    print(1, end=' ')

    for j in range(1, 2 * i - 2):
        print(' ', end=' ')

    if i > 1:
        print(i)
    else:
        print()

for i in range(1, 6):
    print(i, end='   ')