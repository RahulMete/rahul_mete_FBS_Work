days = int(input("enter number of days:"))

years = days // 365                   # // divide the total days by 365 to find complete years.
remaining_days = days % 365           # % It gives the days left after removing complete years.

weeks = remaining_days // 7 
remaining_days = remaining_days % 7

print("years:", years)
print("weeks", weeks)
print("days", remaining_days)