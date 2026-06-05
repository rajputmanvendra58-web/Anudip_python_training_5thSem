# Electricity Bill Calculator using while loop
units = int(input("Enter units consumed: "))
bill = 0
i = 1
# Calculate bill unit by unit
while i <= units:
    if i <= 100:
        bill += 5
    elif i <= 200:
        bill += 7
    else:
        bill += 10
    i += 1
# Determine category
if units <= 100:
    category = "Low Consumption"
elif units <= 200:
    category = "Medium Consumption"
else:
    category = "High Consumption"

# Display result
print("\n----- Electricity Bill -----")
print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)