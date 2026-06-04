#Program for Shopping cart bill
# Initialize total bill amount
total_bill = 0
# Take item prices until user enters 0
while True:
    price = float(input("Enter Item Price: "))
    # Stop taking input if price is 0
    if price == 0:
        break
    # Add item price to total bill
    total_bill += price
# Display the final bill amount
print("Total Bill Amount: ₹", total_bill)