# City Temperature Monitoring System 
"""
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = {     
"Delhi": 41,     
"Mumbai": 33,     
"Chennai": 37,     
"Kolkata": 39,     
"Bengaluru": 28,     
"Pune": 30,     
"Jaipur": 42,     
"Lucknow": 40,     
"Hyderabad": 35,     
"Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C. 
"""
# creating a dictionary for temperature
temperature = {     
"Delhi": 41,     
"Mumbai": 33,     
"Chennai": 37,     
"Kolkata": 39,     
"Bengaluru": 28,     
"Pune": 30,     
"Jaipur": 42,     
"Lucknow": 40,     
"Hyderabad": 35,     
"Ahmedabad": 43 
}

# Task 1: to Display cities having temperature above 40°C.
print ("Cities having temperature above 40°C:")
for city,temp in temperature.items():
    if temp>40:
        print(city)

# Task 2: to Find the hottest city.
dict_items=list(temperature.items())
top_city=dict_items[0][0]
top_temp=dict_items[0][1]
for item in dict_items:
    if item[1]>top_temp:
        top_city=item[0]
        top_temp=item[1]
print("Top Performer: ",top_city,"(",top_temp,")")

# Task 3: to Find the coolest city. 
dict_items=list(temperature.items())
top_city=dict_items[0][0]
top_temp=dict_items[0][1]
for item in dict_items:
    if item[1]<top_temp:
        top_city=item[0]
        top_temp=item[1]
print("Top Performer: ",top_city,"(",top_temp,")")

# Task 4: to Calculate average temperature.
average_temp=sum(temperature.values())/len(temperature)
print("Average Temperature :- ",average_temp,"°C")

# Task 5: to Create a list of pleasant cities (temperature < 35°C).
# Task 5: Create a list of pleasant cities (temperature < 35°C)
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)
print("Pleasant Cities:")
print(pleasant_cities)

# Task 6: Count cities with temperature between 35°C and 40°C
count = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1
print("Cities Between 35°C and 40°C:", count)

"""
Output:-
Cities having temperature above 40°C:
Delhi
Jaipur
Ahmedabad
Top Performer:  Ahmedabad ( 43 )
Top Performer:  Bengaluru ( 28 )
Average Temperature :-  36.8 °C
Pleasant Cities:
['Mumbai', 'Bengaluru', 'Pune']
Cities Between 35°C and 40°C: 4
"""
