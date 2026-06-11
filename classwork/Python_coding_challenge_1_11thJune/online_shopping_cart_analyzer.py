# Problem 5: Online Shopping Cart Analyzer
"""
Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.
"""

# Online Shopping Cart Analyzer

# List containing product prices
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# ----------------------------------
# Task 1 : Calculate Total Cart Value
# ----------------------------------
total_value = 0

for price in cart:
    total_value += price

print("Total Cart Value : ₹", total_value)

# ----------------------------------
# Task 2 : Find Most Expensive and Cheapest Product
# ----------------------------------
most_expensive = cart[0]
cheapest = cart[0]

for price in cart:

    if price > most_expensive:
        most_expensive = price

    if price < cheapest:
        cheapest = price

print("Most Expensive Product : ₹", most_expensive)
print("Cheapest Product : ₹", cheapest)

# ----------------------------------
# Task 3 : Count Premium Shipping Products
# (Price > ₹1000)
# ----------------------------------
premium_count = 0

for price in cart:

    if price > 1000:
        premium_count += 1

print("Premium Shipping Eligible Products :", premium_count)

# ----------------------------------
# Task 4 : Generate Discount List
# (Products Above ₹1500)
# ----------------------------------
discount_products = []

for price in cart:

    if price > 1500:
        discount_products.append(price)

print("Discount Eligible Products :", discount_products)

# ----------------------------------
# Task 5 : Calculate Average Product Price
# ----------------------------------
average_price = total_value / len(cart)

print("Average Product Price : ₹", average_price)