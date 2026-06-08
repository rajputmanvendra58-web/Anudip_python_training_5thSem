# Program for Flight Booking Analysis 
# Problem Statement 
# A flight reservation system stores passenger records as tuples: 
# bookings = (     
# ("P101", "Delhi", "Confirmed"),     ("P102", "Mumbai", "Waiting"),     
# ("P103", "Delhi", "Confirmed"),     ("P104", "Chennai", "Cancelled"),     ("P105", "Mumbai", "Confirmed"),     ("P106", "Delhi", "Waiting") ) 
# Where: • Passenger ID  • Destination  • Booking Status
# Tasks Write a Python program to: 
# 1. Display all passengers whose booking status is Confirmed.  
# 2. Count the number of passengers travelling to Delhi.  
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.  
# 4. Create a list containing passenger IDs with Waiting status.  
# 5. Determine which destination has the highest number of bookings.   



# Flight Booking Analysis Using Tuples

# Creating booking data
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# -----------------------------------------
# Task 1 : Display all confirmed passengers

print("----------------------Confirmed Passengers--------------------------------")
for record in bookings:
    if record[2] == "Confirmed":
        print("Passenger ID :", record[0])
        print("Destination :", record[1])
        print("----------------------")

# -----------------------------------------
# Task 2 : Count passengers travelling to Delhi

count_delhi = 0

for record in bookings:
    if record[1] == "Delhi":
        count_delhi += 1

print("---------------------Passengers Travelling to Delhi :---------------------------------", count_delhi)

# -----------------------------------------
# Task 3 : Count Confirmed, Waiting and Cancelled bookings

confirmed = 0
waiting = 0
cancelled = 0

for record in bookings:

    if record[2] == "Confirmed":
        confirmed += 1

    elif record[2] == "Waiting":
        waiting += 1

    elif record[2] == "Cancelled":
        cancelled += 1

print("Confirmed :", confirmed)
print("Waiting :", waiting)
print("Cancelled :", cancelled)

# -----------------------------------------
# Task 4 : Create a list of passenger IDs with Waiting status

waiting_list = []

for record in bookings:
    if record[2] == "Waiting":
        waiting_list.append(record[0])

print("--------------------------------Waiting List :---------------------------------", waiting_list)

# -----------------------------------------
# Task 5 : Find destination with highest number of bookings

delhi = 0
mumbai = 0
chennai = 0

for record in bookings:

    if record[1] == "Delhi":
        delhi += 1

    elif record[1] == "Mumbai":
        mumbai += 1

    elif record[1] == "Chennai":
        chennai += 1

if delhi > mumbai and delhi > chennai: #checking for delhi if it is most booked
    most_booked = "Delhi"

elif mumbai > delhi and mumbai > chennai: #checking for mumbai if it is most booked
    most_booked = "Mumbai"

else:
    most_booked = "Chennai" # checking for chennai if it is most booked

print("--------------------------Most Booked Destination :----------------", most_booked)