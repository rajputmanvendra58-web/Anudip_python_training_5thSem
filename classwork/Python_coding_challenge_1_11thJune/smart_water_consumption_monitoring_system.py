# Problem 8: Smart Water Consumption Monitoring System 
"""
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data water_usage = {     
"House101": 1800,     
"House102": 2200,     
"House103": 3500,     
"House104": 2800,     
"House105": 1600,     
"House106": 4100,     
"House107": 2400,     
"House108": 3900,     
"House109": 1500,     
"House110": 4500 } 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
    o Low (<2000 litres)  
    o Medium (2000–3500 litres)  
    o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres). 
"""

# Smart Water Consumption Monitoring System

# Dictionary storing water consumption of houses
water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# ----------------------------------
# Task 1 : Houses consuming more than 3000 litres
# ----------------------------------
print("Houses Consuming More Than 3000 Litres:")
print("-" * 40)

for house, consumption in water_usage.items():
    if consumption > 3000:
        print(house)

# ----------------------------------
# Task 2 : Find Highest and Lowest Consumer
# ----------------------------------
highest_house = list(water_usage.keys())[0]
lowest_house = list(water_usage.keys())[0]

for house, consumption in water_usage.items():

    if consumption > water_usage[highest_house]:
        highest_house = house

    if consumption < water_usage[lowest_house]:
        lowest_house = house

print("\nHighest Consumption:")
print(f"{highest_house} ({water_usage[highest_house]} litres)")

print("\nLowest Consumption:")
print(f"{lowest_house} ({water_usage[lowest_house]} litres)")

# ----------------------------------
# Task 3 : Calculate Total Consumption
# ----------------------------------
total_consumption = 0

for consumption in water_usage.values():
    total_consumption += consumption

print("\nTotal Consumption:", total_consumption, "litres")

# ----------------------------------
# Task 4 : Categorize Houses
# ----------------------------------
low = []
medium = []
high = []

for house, consumption in water_usage.items():

    if consumption < 2000:
        low.append(house)

    elif consumption <= 3500:
        medium.append(house)

    else:
        high.append(house)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# ----------------------------------
# Task 5 : Count Eligible Households
# (>2500 litres)
# ----------------------------------
eligible_count = 0

for consumption in water_usage.values():

    if consumption > 2500:
        eligible_count += 1

print("\nEligible Households:", eligible_count)