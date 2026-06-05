# Program for Inventory Stock Alert System
# Problem Statement 
# An inventory manager stores stock quantities as:
# stock = [25, 5, 0, 12, 3, 18, 0, 30] 
# Write a program to:
# 1. Display products that are out of stock.
# 2. Display products that need restocking (quantity less than 10).
# 3. Count available products. 
# 4. Create a new list containing only products with stock greater than or equal to 15.


#List containing stock quantities of product
stock=[25, 5, 0, 12, 3, 18, 0, 30] 

#Counter for out of stock products
out_of_stock=0

#List for the product that need restocking
restock_required=[]

#Counter for Available products
available_products=0

#List for containing only products with stock greater than or equal to 15.
great_stock=[]

#Traverse through Stock list
for qty in stock:
    #for checking the product is out of stock
    if qty==0:
        out_of_stock+=1
    #for checking if the product needs restocking
    if qty<10:
        restock_required.append(qty)
    #for checking of available products
    if qty>0:
        available_products+=1
    #for creating the new list conataining the products with stock greater than or equal to 15.
    if qty>=15:
        great_stock.append(qty)

#For Displaying the Results
print("Out of Stock Products: ",out_of_stock)
print("Restock Required: ",restock_required)
print("Available Products: ",available_products)
print("Healthy Stock: ",great_stock)
