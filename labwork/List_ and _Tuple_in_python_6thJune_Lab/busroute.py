# Program for Bus Route Monitoring 
"""
Problem Statement 
Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] 
Write a program to: 
• Find the busiest stop.  
• Display stops with fewer than 10 passengers.  
• Calculate average passengers.  
• Determine whether any stop exceeded 25 passengers.  
"""

# Problem Statement 8: Bus Route Monitoring

# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Task 1: Find the busiest stop
max_passengers = max(passengers)
busiest_stop = passengers.index(max_passengers) + 1

print("Busiest Stop:", busiest_stop)
print("Passengers at Busiest Stop:", max_passengers)

# Task 2: Display stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1, ":", passengers[i], "passengers")

# Task 3: Calculate average passengers
average = sum(passengers) / len(passengers)

print("\nAverage Passengers:", average)

# Task 4: Determine whether any stop exceeded 25 passengers
exceeded = False

for count in passengers:
    if count > 25:
        exceeded = True
        break

if exceeded:
    print("At least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")