# Online Food Ordering and Restaurant Management System
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MENU_FILE = os.path.join(BASE_DIR, "menu.txt")
# Create full path of cart.txt
CART_FILE = os.path.join(BASE_DIR, "cart.txt")
# Create full path of users.txt
USERS_FILE = os.path.join(BASE_DIR, "users.txt")
# Store logged in user
current_user = ""
print(MENU_FILE)
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to add food item
def add_food():

    # Take Food ID from user
    food_id = input("Enter Food ID: ")

    # Check if Food ID contains only numbers
    if not food_id.isdigit():
        print("Food ID Must Be Numbers Only")
        return

    # Take Food Name from user
    food_name = input("Enter Food Name: ")

    # Check if Food Name is empty
    if food_name == "":
        print("Food Name Cannot Be Empty")
        return

    # Check if Food Name contains only alphabets
    if not food_name.replace(" ", "").isalpha():
        print("Food Name Must Contain Alphabets Only")
        return

    # Take Category from user
    category = input("Enter Category: ")

    # Check if Category is empty
    if category == "":
        print("Category Cannot Be Empty")
        return

    # Check if Category contains only alphabets
    if not category.replace(" ", "").isalpha():
        print("Category Must Contain Alphabets Only")
        return

    try:
        # Take Price from user
        price = float(input("Enter Price: "))

        # Price should be greater than 0
        if price <= 0:
            print("Price Must Be Greater Than 0")
            return

    except ValueError:
        print("Invalid Price")
        return

    # Open menu.txt file in append mode
    file = open(MENU_FILE, "a")

    # Store food details in file
    file.write(
        food_id + "," +
        food_name + "," +
        category + "," +
        str(price) + "\n"
    )

    # Close the file
    file.close()

    print("Food Added Successfully")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to display all food items
def view_food():

    try:

        # Open menu file in read mode
        file = open(MENU_FILE, "r")

        # Read all records from file
        foods = file.readlines()

        # Check if file is empty
        if len(foods) == 0:
            print("No Food Items Available")
            file.close()
            return

        # Display heading
        print("\nID\tNAME\t\tCATEGORY\tPRICE")
        print("-" * 50)

        # Loop through each food record
        for food in foods:

            # Split record using comma
            data = food.strip().split(",")

            # Display food details
            print(
                data[0], "\t",
                data[1], "\t\t",
                data[2], "\t",
                data[3]
            )

        # Close file after reading
        file.close()

    # Handle file not found error
    except FileNotFoundError:
        print("Menu File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to update food details
def update_food():

    # Take Food ID from user
    food_id = input("Enter Food ID To Update: ")

    try:

        # Open file in read mode
        file = open(MENU_FILE, "r")

        # Read all records
        foods = file.readlines()

        # Close file
        file.close()

        # Variable to check whether Food ID exists
        found = False

        # Open file in write mode
        file = open(MENU_FILE, "w")

        # Loop through all food records
        for food in foods:

            # Split record using comma
            data = food.strip().split(",")

            # Check if Food ID matches
            if data[0] == food_id:

                found = True

                print("Food Found")

                # Take new food name
                new_name = input("Enter New Food Name: ")

                # Check if name is empty
                if new_name == "":
                    print("Food Name Cannot Be Empty")
                    file.close()
                    return

                # Take new category
                new_category = input("Enter New Category: ")

                # Check if category is empty
                if new_category == "":
                    print("Category Cannot Be Empty")
                    file.close()
                    return

                # Take new price
                new_price = input("Enter New Price: ")

                # Write updated record
                file.write(
                    food_id + "," +
                    new_name + "," +
                    new_category + "," +
                    new_price + "\n"
                )

            else:

                # Keep old record unchanged
                file.write(food)

        # Close file after update
        file.close()

        # Display result
        if found:
            print("Food Updated Successfully")
        else:
            print("Food ID Not Found")

    # Handle file not found error
    except FileNotFoundError:
        print("Menu File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to delete food item
def delete_food():

    # Take Food ID from user
    food_id = input("Enter Food ID To Delete: ")

    try:

        # Open file in read mode
        file = open(MENU_FILE, "r")

        # Read all records
        foods = file.readlines()

        # Close file
        file.close()

        found = False

        # Open file in write mode
        file = open(MENU_FILE, "w")

        # Loop through all records
        for food in foods:

            # Split record using comma
            data = food.strip().split(",")

            # Check if Food ID matches
            if data[0] == food_id:

                found = True

                print("Food Deleted Successfully")

            else:

                # Keep remaining records
                file.write(food)

        # Close file
        file.close()

        # Check if Food ID exists
        if not found:
            print("Food ID Not Found")

    # Handle file not found error
    except FileNotFoundError:
        print("Menu File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to register new user
def register_user():

    # Take username from user
    username = input("Enter Username: ")

    # Check if username is empty
    if username == "":
        print("Username Cannot Be Empty")
        return

    # Take password from user
    password = input("Enter Password: ")

    # Password should contain minimum 6 characters
    if len(password) < 6:
        print("Password Must Contain At Least 6 Characters")
        return

    # Check duplicate username
    try:

        # Open file in read mode
        file = open(USERS_FILE, "r")

        # Check all existing users
        for user in file:

            # Split record using comma
            data = user.strip().split(",")

            # Check if username already exists
            if data[0] == username:

                print("Username Already Exists")

                file.close()

                return

        # Close file
        file.close()

    # Ignore error if file does not exist
    except FileNotFoundError:
        pass

    # Open file in append mode
    file = open(USERS_FILE, "a")

    # Store username and password
    file.write(
        username + "," +
        password + "\n"
    )

    # Close file
    file.close()

    print("Registration Successful")
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Function for user login
def login_user():

    # Take username from user
    username = input("Enter Username: ")

    # Take password from user
    password = input("Enter Password: ")

    try:

        # Open file in read mode
        file = open(USERS_FILE, "r")

        # Check all users
        for user in file:

            # Split record using comma
            data = user.strip().split(",")

            if data[0] == username and data[1] == password:

                global current_user

                current_user = username

                print("Login Successful")

                file.close()

                return True

        # Close file
        file.close()

        print("Invalid Username Or Password")

        return False

    # Handle file not found error
    except FileNotFoundError:

        print("No Users Registered")

        return False
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Function to search food by name
def search_by_name():

    # Take food name from user
    food_name = input("Enter Food Name: ")

    found = False

    try:

        # Open file in read mode
        file = open(MENU_FILE, "r")

        # Loop through all records
        for food in file:

            # Split record using comma
            data = food.strip().split(",")

            # Check food name
            if data[1].lower() == food_name.lower():

                found = True

                print("\nFood Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Category:", data[2])
                print("Price:", data[3])

        # Close file
        file.close()

        if not found:
            print("Food Not Found")

    except FileNotFoundError:
        print("Menu File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to search food by category
def search_by_category():

    # Take category from user
    category = input("Enter Category: ")

    found = False

    try:

        # Open file
        file = open(MENU_FILE, "r")

        for food in file:

            data = food.strip().split(",")

            # Check category
            if data[2].lower() == category.lower():

                found = True

                print(
                    data[0], "\t",
                    data[1], "\t",
                    data[2], "\t",
                    data[3]
                )

        file.close()

        if not found:
            print("Category Not Found")

    except FileNotFoundError:
        print("Menu File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to search food by price
def search_by_price():

    # Take maximum price
    max_price = float(input("Enter Maximum Price: "))

    found = False

    try:

        # Open file
        file = open(MENU_FILE, "r")

        for food in file:

            data = food.strip().split(",")

            # Check price
            if float(data[3]) <= max_price:

                found = True

                print(
                    data[0], "\t",
                    data[1], "\t",
                    data[2], "\t",
                    data[3]
                )

        file.close()

        if not found:
            print("No Food Found")

    except FileNotFoundError:
        print("Menu File Not Found")

#-------------------------------------------------------------------------------------------------------------------------------------------
# Function for search menu
def search_menu():

    while True:

        print("\n===== FOOD SEARCH =====")
        print("1. Search By Name")
        print("2. Search By Category")
        print("3. Search By Price")
        print("4. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            search_by_name()

        elif choice == "2":
            search_by_category()

        elif choice == "3":
            search_by_price()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to add food item to cart
def add_to_cart():

    # Check user login
    if current_user == "":
        print("Please Login First")
        return

    # Take Food ID from user
    food_id = input("Enter Food ID: ")

    found = False

    try:

        # Open menu file
        file = open(MENU_FILE, "r")

        # Search food item
        for food in file:

            data = food.strip().split(",")

            # Check Food ID
            if data[0] == food_id:

                found = True

                food_name = data[1]

                price = float(data[3])

                # Take quantity
                quantity = int(input("Enter Quantity: "))

                # Calculate total amount
                total_price = quantity * price

                # Open cart file
                cart = open(CART_FILE, "a")

                # Store cart details
                cart.write(
                    current_user + "," +
                    food_id + "," +
                    food_name + "," +
                    str(quantity) + "," +
                    str(total_price) + "\n"
                )

                cart.close()

                print("Item Added To Cart")

                break

        file.close()

        if not found:
            print("Food ID Not Found")

    except FileNotFoundError:
        print("Menu File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# Function to view cart items
def view_cart():

    # Check user login
    if current_user == "":
        print("Please Login First")
        return

    try:

        # Open cart file
        file = open(CART_FILE, "r")

        # Read all cart records
        carts = file.readlines()

        # Close file
        file.close()

        found = False

        print("\n===== MY CART =====")
        print("Food ID\tFood Name\tQuantity\tTotal")

        # Loop through cart records
        for cart in carts:

            data = cart.strip().split(",")

            # Show only logged in user's cart
            if data[0] == current_user:

                found = True

                print(
                    data[1], "\t",
                    data[2], "\t\t",
                    data[3], "\t\t",
                    data[4]
                )

        if not found:
            print("Cart Is Empty")

    except FileNotFoundError:
        print("Cart File Not Found")
#--------------------------------------------------------------------------------------------------------------------------------------------
# Function to update cart quantity
def update_cart():

    # Check user login
    if current_user == "":
        print("Please Login First")
        return

    # Take Food ID from user
    food_id = input("Enter Food ID To Update: ")

    try:

        # Open cart file
        file = open(CART_FILE, "r")

        carts = file.readlines()

        file.close()

        found = False

        # Open cart file in write mode
        file = open(CART_FILE, "w")

        # Loop through all cart records
        for cart in carts:

            data = cart.strip().split(",")

            # Check user and food id
            if data[0] == current_user and data[1] == food_id:

                found = True

                # Take new quantity
                quantity = int(input("Enter New Quantity: "))

                # Calculate new total price
                price_per_item = float(data[4]) / int(data[3])

                total_price = quantity * price_per_item

                # Write updated record
                file.write(
                    data[0] + "," +
                    data[1] + "," +
                    data[2] + "," +
                    str(quantity) + "," +
                    str(total_price) + "\n"
                )

            else:

                # Keep old record
                file.write(cart)

        file.close()

        if found:
            print("Cart Updated Successfully")
        else:
            print("Food ID Not Found In Cart")

    except FileNotFoundError:
        print("Cart File Not Found")
#-------------------------------------------------------------------------------------------------------------------------------------------
# # Function to remove item from cart
def remove_from_cart():

    # Check user login
    if current_user == "":
        print("Please Login First")
        return

    # Take Food ID from user
    food_id = input("Enter Food ID To Remove: ")

    try:

        # Open cart file
        file = open(CART_FILE, "r")

        carts = file.readlines()

        file.close()

        found = False

        # Open cart file in write mode
        file = open(CART_FILE, "w")

        # Loop through all cart records
        for cart in carts:

            data = cart.strip().split(",")

            # Check user and food id
            if data[0] == current_user and data[1] == food_id:

                found = True

            else:

                # Keep remaining records
                file.write(cart)

        file.close()

        if found:
            print("Item Removed From Cart")
        else:
            print("Food ID Not Found In Cart")

    except FileNotFoundError:
        print("Cart File Not Found")
#--------------------------------------------------------------------------------------------------------------------------------------------

while True:
    print("\n==============================ONLINE FOOD ORDERING SYSTEM==============================")
    print("1. Register User")
    print("2. Login User")
    print("3. Current User")
    print("\n================================= MENU MANAGEMENT =====================================")
    print("4. Add Food")
    print("5. View Food")
    print("6. Update Food")
    print("7. Delete Food")
    print("\n====================================SEARCH FOOD========================================")
    print("8. Search Food")
    print("\n==================================CART MANAGEMENT======================================")
    print("9. Add to Cart")
    print("10. View Cart")
    print("11. Update Cart")
    print("12. Remove from the Cart")
    print("13. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        login_user()

    elif choice == "3":
        print("Logged In User:", current_user)

    elif choice == "4":
        add_food()
    
    elif choice == "5":
        view_food()

    elif choice == "6":
        update_food()

    elif choice == "7":
        delete_food()
        
    elif choice == "8":
        search_menu()
        
    elif choice == "9":
        add_to_cart()
        
    elif choice == "10":
       view_cart() 

    elif choice=="11":
        update_cart()
    
    elif choice == "12":
        remove_from_cart()
 
    elif choice == "13":
     print("Thank You")
     break   
    else:
        print("Invalid Choice")