# Food Delivery Performance Tracker 
"""
Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
    1. fastest_delivery(times) 
    Returns the shortest delivery time. 
    2. delayed_orders(times) 
    Returns a list of orders taking more than 45 minutes. 
    3. average_delivery_time(times) 
    Returns the average delivery time. 
    4. delivery_category(times) 
    Displays order categories: 
        • Fast → ≤ 30 minutes  
        • Normal → 31–45 minutes  
        • Delayed → > 45 minutes 
"""
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
#----------------------------------------------
# Function to find the fastest delivery time    
# ----------------------------------------------
def fastest_delivery(times):
    return min(times)

#----------------------------------------------
# Function to find delayed orders
# ----------------------------------------------
def delayed_orders(times):
    delayed = [time for time in times if time > 45]
    return delayed

#----------------------------------------------
# Function to calculate average delivery time 
# ----------------------------------------------
def average_delivery_time(times):
    return sum(times) / len(times)


#----------------------------------------------
# Function to categorize delivery times
# ----------------------------------------------
def delivery_category(times):
    print("Delivery Categories:")
    for time in times:
        if time <= 30:
            category = "Fast"
        elif 31 <= time <= 45:
            category = "Normal"
        else:
            category = "Delayed"
        print(f"Time: {time} minutes - Category: {category}")


#----------------------------------------------
# Main function to execute the requirements
#----------------------------------------------
if __name__ == "__main__":
    print(f"Fastest Delivery Time: {fastest_delivery(delivery_time)} minutes")
    
    delayed = delayed_orders(delivery_time)
    print(f"Delayed Orders (more than 45 minutes): {delayed}")
    
    avg_time = average_delivery_time(delivery_time)
    print(f"Average Delivery Time: {avg_time:.2f} minutes")
    
    delivery_category(delivery_time)