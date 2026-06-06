# Program for Warehouse Product Inspection 
"""
 Problem Statement 
 Product IDs and quality status: 
 products = [     
 (101, "Pass"),     
 (102, "Fail"),     
 (103, "Pass"),     
 (104, "Fail"),     
 (105, "Pass") ] 
 Write a program to: 
 • Display failed product IDs.  
 • Count passed and failed products.  
 • Calculate pass percentage.  
 • Stop checking if 3 failures are found. 
 """

# Problem Statement 9: Warehouse Product Inspection

# Product IDs and quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# Task 1: Display failed product IDs
print("Failed Product IDs:")
for product_id, status in products:
    if status == "Fail":
        print(product_id)

# Task 2: Count passed and failed products
pass_count = 0
fail_count = 0

for product_id, status in products:
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)

# Task 3: Calculate pass percentage
total_products = len(products)
pass_percentage = (pass_count / total_products) * 100

print("Pass Percentage:", pass_percentage, "%")

# Task 4: Stop checking if 3 failures are found
failure_count = 0

print("\nChecking Products:")
for product_id, status in products:
    print("Product ID:", product_id, "-", status)

    if status == "Fail":
        failure_count += 1

    if failure_count == 3:
        print("3 failures found. Stopping inspection.")
        break