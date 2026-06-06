# Program for E-Commerce Order Analysis

"""
Problem Statement

An online store records orders as:
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. 
"""

# List of orders (Product Name, Price)
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Display products costing more than ₹1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(product, "-", price)

# Find the most expensive product
most_expensive = orders[0]

for item in orders:
    if item[1] > most_expensive[1]:
        most_expensive = item

print("\nMost Expensive Product:", most_expensive[0], "-", most_expensive[1])

# Calculate total order value
total_value = 0

for product, price in orders:
    total_value += price

print("Total Order Value: ₹", total_value)

# Count products costing below ₹1000
count = 0

for product, price in orders:
    if price < 1000:
        count += 1

print("Products costing below ₹1000:", count)