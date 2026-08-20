#WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter the cost price of the book:"))
discount = float(input("Enter the discount percentage:"))

#FORMULA 
discount_amount = (cost_price * discount) / 100
selling_price = cost_price - discount_amount

print("discount amount is:", discount_amount)
print("selling price of book is:", selling_price)