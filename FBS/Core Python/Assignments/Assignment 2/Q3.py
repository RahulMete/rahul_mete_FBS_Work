#Convert distant given in feet and inches into meter and centimeter.

feet = float(input("enter distance in feet:"))
inches = float(input("enter distance in inches:"))

#FORMULA  > total inches in meter = (feet * 12) + (inches * 12).                 (1 foot = 12 inches)
#FORMULA  > total inches * 2.54.                                                 (1 inch = 2.54 cm)
#FORMULA > total meter = total cm / 100.                                         (1 meter = 100 cm)

total_inches = (feet * 12)+ inches
total_cm = total_inches * 2.54
total_meter = total_cm / 100

print("Distance in meter is:", total_meter)
print("Distance in centimeter is:", total_cm)