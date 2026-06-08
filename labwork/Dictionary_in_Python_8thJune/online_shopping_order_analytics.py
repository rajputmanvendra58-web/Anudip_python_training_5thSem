# Online Shopping Order Analytics 
"""
Problem Statement 
An e-commerce company stores product sales data as: 
sales = {     
"Laptop": 15,     
"Mouse": 45,     
"Keyboard": 32,     
"Monitor": 12,     
"Headphones": 28,     
"Printer": 8,     
"Webcam": 20,     
"Speaker": 18,     
"Tablet": 10,     
"Router": 25 
}
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.  
"""

# Creating a dictionary to store product sales data
sales = {     
"Laptop": 15,     
"Mouse": 45,     
"Keyboard": 32,     
"Monitor": 12,     
"Headphones": 28,     
"Printer": 8,     
"Webcam": 20,     
"Speaker": 18,     
"Tablet": 10,     
"Router": 25 
}

# Task 1 : to  Display products sold more than 20 times.
print("Products sold more than 20 times:- ") 
for product,quantity in sales.items():
    if quantity > 20:
        print(product)

# Task 2 : to Find the best-selling product.
dict_items=list(sales.items())
best_product=dict_items[0][0]
best_selling=dict_items[0][1]
for item in dict_items:
    if item[1]>best_selling:
        best_product=item[0]
        best_selling=item[1]
print("Best Selling Product: ", best_product,"(",best_selling, ")")

# Task 3 : to Find the least-selling product.
dict_items=list(sales.items())
least_product=dict_items[0][0]
least_selling=dict_items[0][1]
for item in dict_items:
    if item[1]<least_selling:
        least_product=item[0]
        least_selling=item[1]
print(" Least-Selling Product ", least_product,"(",least_selling, ")")

# Task 4 : to Calculate total products sold.
total_sold=sum(sales.values())
print("Total Units Sold :- ", total_sold)

# Task 5 : to Create a list of products requiring promotion (sales < 15).
promotion_products=[]
for product,quantity in sales.items():
    if quantity<15:
        promotion_products.append(product)
print("Products Requiring Promotion:")
print(promotion_products)

# Task 6: Count products having sales between 10 and 30
count = 0
for quantity in sales.values():
    if 10 <= quantity <= 30:
        count += 1
print("Products Having Sales Between 10 and 30:", count)


"""
Output:-
Products sold more than 20 times:- 
Mouse
Keyboard
Headphones
Router
Best Selling Product:  Mouse ( 45 )
 Least-Selling Product  Printer ( 8 )
Total Units Sold :-  213
Products Requiring Promotion:
['Monitor', 'Printer', 'Tablet']
Products Having Sales Between 10 and 30: 7
"""