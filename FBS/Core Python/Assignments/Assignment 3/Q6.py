#Write a program to calculate profit or loss. 

cost_price = int(input('Enter cost price'))
selling_price = int(input('Enter selling ptice'))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("profit =", profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("loss =", loss)
    
else:
    print('no profit no loss')
    