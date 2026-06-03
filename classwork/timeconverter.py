#program to convert seconds into hours, minutes and seconds

seconds = int(input("Enter time in seconds: "))

#validate seconds
if(seconds < 0):
    exit("Time cannot be negative")

#conversion
hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

#print result
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)