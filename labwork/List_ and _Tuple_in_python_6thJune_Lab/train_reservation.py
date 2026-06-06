# Program for Train Reservation Waiting List
"""
Problem Statement 
Passenger records: 
passengers = [     
("Anuj", "Confirmed"),     
("Rahul", "Waiting"),     
("Priya", "Confirmed"),     
("Amit", "Waiting"),     
("Neha", "Confirmed") ]
Write a program to: 
• Display all waiting-list passengers.  
• Count confirmed and waiting passengers.  
• Find whether a specific passenger has a confirmed ticket.  
• Create separate lists for confirmed and waiting passengers.
"""

# Task 1: Store passenger records

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Task 2: Display all waiting-list passengers

print("Waiting List Passengers:")
for passenger in passengers:
    if passenger[1] == "Waiting":
        print(passenger[0])

# Task 3: Count confirmed and waiting passengers

confirmed_count = 0
waiting_count = 0

for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_count += 1
    else:
        waiting_count += 1

print("\nConfirmed Passengers =", confirmed_count)
print("Waiting Passengers =", waiting_count)

# Task 4: Check whether a specific passenger has a confirmed ticket

search_name = input("\nEnter passenger name: ")

found = False

for passenger in passengers:
    if passenger[0].lower() == search_name.lower():
        found = True

        if passenger[1] == "Confirmed":
            print("Passenger has a Confirmed Ticket")
        else:
            print("Passenger is on the Waiting List")

        break

if found == False:
    print("Passenger not found")

# Task 5: Create separate lists for confirmed and waiting passengers

confirmed_list = []
waiting_list = []

for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_list.append(passenger[0])
    else:
        waiting_list.append(passenger[0])

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)