for i in range(1, 11):
    
    if i <= 5:
        n = i
    else:
        n = 11 - i
        
    for j in range(1, 6-n):
        print(' ', end=' ')
        
    for j in range(1, 6 * n):
        if j == 1 or j == 2 * n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
            
    print()