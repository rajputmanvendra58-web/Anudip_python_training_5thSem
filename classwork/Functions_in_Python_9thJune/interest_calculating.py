#to import a module
import interestcalculator
#function to calculate simple interest
#--- main program ---
principal = float(input("Enter the principal(in Rs) : : "))
#validate the principal amount
if principal < 0:
    exit("Principal amount cannot be negative.")
#input of rate of interest
rate = float(input("Enter the rate of interest (in %): "))
#validate the rate of interest
if rate < 0:
    exit("Rate of interest cannot be negative.")
#input of time period
time =int(input("Enter the time period (in years): "))
#validate the time period
if time < 0:
    exit("Time period cannot be negative.")
#---------------------------------------------
print("---------------------------------------")
#to calculate simple interest
si = interestcalculator.simple_interest(principal, rate, time)
#displaying simple interest
print("Simple Interest : Rs", si)