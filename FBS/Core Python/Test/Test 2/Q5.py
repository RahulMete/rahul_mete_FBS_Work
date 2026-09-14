# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

p1 = float(input('Enter value of product 1:'))
p2 = float(input('Enter value of product 2:'))
p3 = float(input('Enter value of product 3:'))
p4 = float(input('Enter value of product 4:')) 
p5 = float(input('Enter value of product 5:'))

Total = p1 + p2 + p3 + p4 + p5
GST = Total * 18 / 100
bill = Total + GST

print('Total =', Total)
print('GST =', GST)
print('Final Bill=', bill)