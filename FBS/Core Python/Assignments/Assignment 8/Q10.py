# Check Whether Year is Leap Year or Not

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
year = int(input('Enter a year: '))

if leap_year(year):
    print("Year is leap Year")
else:
    print("Year is not leap Year")