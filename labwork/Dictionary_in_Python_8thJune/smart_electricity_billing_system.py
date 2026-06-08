# Smart Electricity Billing System 
"""
Problem Statement 
Monthly electricity consumption (units) is stored as: units = {     
"House101": 320,     
"House102": 180,     
"House103": 510,     
"House104": 275,     
"House105": 150,     
"House106": 430,     
"House107": 220,     
"House108": 390,     
"House109": 145,     
"House110": 600 }
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate total units consumed.  
5. Create lists:  
    o Low Consumption (< 200)  
    o Medium Consumption (200–400)  
    o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).
"""
# creating the dictionary to store the monthly electricity consumption of each house
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}
# Task 1: Display houses consuming more than 400 units
print("Houses consuming more than 400 units:")
for house, consumption in units.items():
    if consumption > 400:
        print(f"  {house}: {consumption} units")
# Task 2: Find the highest-consuming house
highest_consuming_house = list(units.items())
high_house=highest_consuming_house[0][0]
high_consumption=highest_consuming_house[0][1]
for item in highest_consuming_house:
    if item[1]>high_consumption:
        high_house=item[0]
        high_consumption=item[1]
print(f"Highest-consuming house: {high_house} with {high_consumption} units")
# Task 3: Find the lowest-consuming house
lowest_consuming_house = list(units.items())
low_house=lowest_consuming_house[0][0]
low_consumption=lowest_consuming_house[0][1]
for item in lowest_consuming_house:
    if item[1]<low_consumption:
        low_house=item[0]
        low_consumption=item[1]
print(f"Lowest-consuming house: {low_house} with {low_consumption} units")
# Task 4: Calculate total units consumed
total_units = sum(units.values())
print(f"Total units consumed: {total_units}")
# Task 5: Create lists for low, medium, and high consumption
low_consumption_list = []
medium_consumption_list = []
high_consumption_list = []
for house, consumption in units.items():
    if consumption < 200:
        low_consumption_list.append(house)
    elif 200 <= consumption <= 400:
        medium_consumption_list.append(house)
    else:
        high_consumption_list.append(house)
print(f"Low Consumption (< 200): {low_consumption_list}")
print(f"Medium Consumption (200–400): {medium_consumption_list}")
print(f"High Consumption (> 400): {high_consumption_list}")
# Task 6: Count houses eligible for an energy-saving campaign (consumption > 300)
eligible_houses_count = sum(1 for consumption in units.values() if consumption > 300)
print(f"Houses eligible for energy-saving campaign (consumption > 300): {eligible_houses_count}")

"""
output:
Houses consuming more than 400 units:
  House103: 510 units
  House106: 430 units
  House110: 600 units
Highest-consuming house: House110 with 600 units
Lowest-consuming house: House109 with 145 units
Total units consumed: 3220
Low Consumption (< 200): ['House102', 'House105', 'House109']
Medium Consumption (200–400): ['House101', 'House104', 'House107', 'House108']
High Consumption (> 400): ['House103', 'House106', 'House110']
Houses eligible for energy-saving campaign (consumption > 300): 4
"""