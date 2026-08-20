#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

c = float(input("enter temprature in celsius:"))

#given formula (C/5 = (F-32)/9) 
#Rearranging formula we get F = (C × 9/5) + 32

f = (c * 9/5) + 32

print("temprature in fahrenheit is:", f)
