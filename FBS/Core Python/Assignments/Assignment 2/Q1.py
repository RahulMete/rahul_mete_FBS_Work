#Convert the time entered in hh,min and sec into seconds.

hh = int(input("enter hours:"))
min = int(input("enter minutes:"))
sec = int(input("enter seconds:"))

#FORMULA > 1 hour = 3600 seconds 1 minute = 60 second.  #Total Seconds = (Hours × 3600) + (Minutes × 60) + Seconds

total_seconds = (hh* 3600) + (min * 60) + sec

print("Total seconds is:", total_seconds)
 