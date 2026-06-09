#  E-Commerce Inventory & Sales Dashboard 
"""
Problem Statement 
An online store wants to manage products and sales. 
Example Structure products = {     
"P101": {         
"name": "Laptop",         
"price": 55000,         
"stock": 12,        
"sold": 25     } } 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).
"""
# ==========================================================
# E-Commerce Inventory & Sales Dashboard
# ==========================================================

# Dictionary to store product records

products = {}

# ==========================================================
# Input Details of 30 Products
# ==========================================================

print("Enter Details of 30 Products")

for i in range(30):

    print(f"\nProduct {i + 1}")

    # ------------------------------------------------------
    # Product ID Validation
    # Example: P101
    # ------------------------------------------------------

    while True:

        pid = input("Enter Product ID (Example: P101): ").upper()

        if pid in products:

            print("Product ID already exists.")

        elif pid.startswith("P") and pid[1:].isdigit() and len(pid) == 4:

            break

        else:

            print("Invalid Product ID.")

    # ------------------------------------------------------
    # Product Name Input
    # ------------------------------------------------------

    pname = input("Enter Product Name: ")

    # ------------------------------------------------------
    # Product Price Validation
    # ------------------------------------------------------

    while True:

        try:

            price = float(input("Enter Product Price: "))

            if price > 0:

                break

            else:

                print("Price must be greater than 0.")

        except ValueError:

            print("Enter numeric value only.")

    # ------------------------------------------------------
    # Product Stock Validation
    # ------------------------------------------------------

    while True:

        try:

            stock = int(input("Enter Available Stock: "))

            if stock >= 0:

                break

            else:

                print("Stock cannot be negative.")

        except ValueError:

            print("Enter integer value only.")

    # ------------------------------------------------------
    # Product Sold Validation
    # ------------------------------------------------------

    while True:

        try:

            sold = int(input("Enter Quantity Sold: "))

            if sold >= 0:

                break

            else:

                print("Sold quantity cannot be negative.")

        except ValueError:

            print("Enter integer value only.")

    # ------------------------------------------------------
    # Store Product Record
    # ------------------------------------------------------

    products[pid] = {
        "name": pname,
        "price": price,
        "stock": stock,
        "sold": sold
    }

print("\n30 Product Records Stored Successfully.")

# ==========================================================
# Menu Driven Program
# ==========================================================

while True:

    print("\n========== MENU ==========")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Stock After Sales")
    print("4. Find Out Of Stock Products")
    print("5. Find Products With Stock Less Than 5")
    print("6. Calculate Total Inventory Value")
    print("7. Find Best Selling Product")
    print("8. Find Least Selling Product")
    print("9. Calculate Total Revenue")
    print("10. Generate Low Stock Report")
    print("11. Products With Above Average Sales")
    print("12. Promotion Eligible Products")
    print("13. Exit")

    choice = input("Enter Your Choice: ")

    # ======================================================
    # Display All Products
    # ======================================================

    if choice == "1":

        if len(products) == 0:

            print("No Product Records Found.")

        else:

            print("\nProduct Records")

            for pid, details in products.items():

                print("-" * 40)
                print("Product ID :", pid)
                print("Name       :", details["name"])
                print("Price      :", details["price"])
                print("Stock      :", details["stock"])
                print("Sold       :", details["sold"])

    # ======================================================
    # Add New Product
    # ======================================================

    elif choice == "2":

        pid = input("Enter Product ID: ").upper()

        if pid in products:

            print("Product ID already exists.")

        elif not (pid.startswith("P")
                  and pid[1:].isdigit()
                  and len(pid) == 4):

            print("Invalid Product ID.")

        else:

            pname = input("Enter Product Name: ")

            try:

                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Available Stock: "))
                sold = int(input("Enter Quantity Sold: "))

                if price <= 0:

                    print("Price must be greater than 0.")

                elif stock < 0 or sold < 0:

                    print("Stock and Sold quantity cannot be negative.")

                else:

                    products[pid] = {
                        "name": pname,
                        "price": price,
                        "stock": stock,
                        "sold": sold
                    }

                    print("Product Added Successfully.")

            except ValueError:

                print("Invalid Input.")
            # ======================================================
    # Update Stock After Sales
    # ======================================================

    elif choice == "3":

        pid = input("Enter Product ID: ").upper()

        if pid not in products:

            print("Product ID not found.")

        else:

            try:

                sale_quantity = int(input("Enter Quantity Sold: "))

                if sale_quantity <= 0:

                    print("Sale quantity must be greater than 0.")

                elif sale_quantity > products[pid]["stock"]:

                    print("Insufficient stock available.")

                else:

                    products[pid]["stock"] -= sale_quantity
                    products[pid]["sold"] += sale_quantity

                    print("Stock Updated Successfully.")

                    print("Remaining Stock :",
                          products[pid]["stock"])

            except ValueError:

                print("Enter integer value only.")

    # ======================================================
    # Find Out Of Stock Products
    # ======================================================

    elif choice == "4":

        print("\nOut Of Stock Products")

        found = False

        for pid, details in products.items():

            if details["stock"] == 0:

                print(
                    pid,
                    details["name"]
                )

                found = True

        if found == False:

            print("No Out Of Stock Products Found.")

    # ======================================================
    # Find Products With Stock Less Than 5
    # ======================================================

    elif choice == "5":

        print("\nProducts With Stock Less Than 5")

        found = False

        for pid, details in products.items():

            if details["stock"] < 5:

                print(
                    pid,
                    details["name"],
                    "Stock =", details["stock"]
                )

                found = True

        if found == False:

            print("No Product Found.")

    # ======================================================
    # Calculate Total Inventory Value
    # Inventory Value = Price × Stock
    # ======================================================

    elif choice == "6":

        total_inventory_value = 0

        for details in products.values():

            total_inventory_value += (
                details["price"] *
                details["stock"]
            )

        print(
            "\nTotal Inventory Value =",
            total_inventory_value
        )

    # ======================================================
    # Find Best Selling Product
    # ======================================================

    elif choice == "7":

        best_product = None

        for pid in products:

            if best_product is None:

                best_product = pid

            elif products[pid]["sold"] > \
                 products[best_product]["sold"]:

                best_product = pid

        print("\nBest Selling Product")

        print("Product ID :", best_product)
        print("Name       :",
              products[best_product]["name"])
        print("Sold       :",
              products[best_product]["sold"])

    # ======================================================
    # Find Least Selling Product
    # ======================================================

    elif choice == "8":

        least_product = None

        for pid in products:

            if least_product is None:

                least_product = pid

            elif products[pid]["sold"] < \
                 products[least_product]["sold"]:

                least_product = pid

        print("\nLeast Selling Product")

        print("Product ID :", least_product)
        print("Name       :",
              products[least_product]["name"])
        print("Sold       :",
              products[least_product]["sold"])
        # ======================================================
    # Calculate Total Revenue Generated
    # Revenue = Price × Sold Quantity
    # ======================================================

    elif choice == "9":

        total_revenue = 0

        for details in products.values():

            total_revenue += (
                details["price"] *
                details["sold"]
            )

        print(
            "\nTotal Revenue Generated =",
            total_revenue
        )

    # ======================================================
    # Generate Low Stock Report
    # Products Having Stock Less Than 5
    # ======================================================

    elif choice == "10":

        print("\nLow Stock Report")

        found = False

        for pid, details in products.items():

            if details["stock"] < 5:

                print(
                    pid,
                    details["name"],
                    "Stock =",
                    details["stock"]
                )

                found = True

        if found == False:

            print("No Low Stock Products Found.")

    # ======================================================
    # Products Whose Sales Are Above Average
    # ======================================================

    elif choice == "11":

        total_sales = 0

        for details in products.values():

            total_sales += details["sold"]

        average_sales = total_sales / len(products)

        print(
            "\nAverage Sales =",
            round(average_sales, 2)
        )

        print("\nProducts With Above Average Sales")

        found = False

        for pid, details in products.items():

            if details["sold"] > average_sales:

                print(
                    pid,
                    details["name"],
                    "Sold =",
                    details["sold"]
                )

                found = True

        if found == False:

            print("No Product Found.")

    # ======================================================
    # Promotion Eligible Products
    # Sales Less Than 10
    # ======================================================

    elif choice == "12":

        promotion_products = {}

        for pid, details in products.items():

            if details["sold"] < 10:

                promotion_products[pid] = details

        print("\nPromotion Eligible Products")

        if len(promotion_products) == 0:

            print("No Promotion Products Found.")

        else:

            for pid, details in promotion_products.items():

                print(
                    pid,
                    details["name"],
                    "Sold =",
                    details["sold"]
                )

    # ======================================================
    # Exit Program
    # ======================================================

    elif choice == "13":

        print("\nProgram Terminated Successfully.")
        break

    # ======================================================
    # Invalid Choice Handling
    # ======================================================

    else:

        print("Invalid Choice. Please Enter 1 to 13.")    