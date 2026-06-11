# Problem 10: Smart City Waste Collection Management System
"""
Problem Statement 
The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
Sample Data 
waste = { 
"Sector1": 320,     
"Sector2": 180,     
"Sector3": 510,     
"Sector4": 275,     
"Sector5": 150,     
"Sector6": 430,     
"Sector7": 220,     
"Sector8": 390,     
"Sector9": 145,     
"Sector10": 600 } 
Tasks 
1. Display sectors generating more than 400 kg of waste.  
2. Find the sector generating maximum waste.  
3. Find the sector generating minimum waste.  
4. Calculate the total waste collected.  
5. Categorize sectors:  
    o Low Waste (<200 kg)  
    o Medium Waste (200–400 kg)  
    o High Waste (>400 kg)  
6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
7. Save the awareness campaign list to campaign_sectors.txt.
"""

# Smart City Waste Collection Management System

# Dictionary storing waste collected from each sector
waste = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# ----------------------------------
# Task 1 : Display Sectors Generating
# More Than 400 kg Waste
# ----------------------------------
print("Sectors Generating More Than 400 kg Waste:")
print("-" * 45)

for sector, amount in waste.items():
    if amount > 400:
        print(sector)

# ----------------------------------
# Task 2 : Find Maximum Waste Sector
# ----------------------------------
max_sector = list(waste.keys())[0]

for sector, amount in waste.items():
    if amount > waste[max_sector]:
        max_sector = sector

print("\nMaximum Waste Generation:")
print(f"{max_sector} ({waste[max_sector]} kg)")

# ----------------------------------
# Task 3 : Find Minimum Waste Sector
# ----------------------------------
min_sector = list(waste.keys())[0]

for sector, amount in waste.items():
    if amount < waste[min_sector]:
        min_sector = sector

print("\nMinimum Waste Generation:")
print(f"{min_sector} ({waste[min_sector]} kg)")

# ----------------------------------
# Task 4 : Calculate Total Waste
# ----------------------------------
total_waste = 0

for amount in waste.values():
    total_waste += amount

print("\nTotal Waste Collected:", total_waste, "kg")

# ----------------------------------
# Task 5 : Categorize Sectors
# ----------------------------------
low_waste = []
medium_waste = []
high_waste = []

for sector, amount in waste.items():

    if amount < 200:
        low_waste.append(sector)

    elif amount <= 400:
        medium_waste.append(sector)

    else:
        high_waste.append(sector)

print("\nLow Waste:")
print(low_waste)

print("\nMedium Waste:")
print(medium_waste)

print("\nHigh Waste:")
print(high_waste)

# ----------------------------------
# Task 6 : Awareness Campaign List
# (Waste > 300 kg)
# ----------------------------------
campaign_sectors = []

for sector, amount in waste.items():

    if amount > 300:
        campaign_sectors.append(sector)

print("\nSectors Requiring Awareness Campaign:")

for sector in campaign_sectors:
    print(sector)

print("\nTotal Sectors Requiring Campaign:",
      len(campaign_sectors))

# ----------------------------------
# Task 7 : Save Campaign List to File
# ----------------------------------
try:
    file = open("campaign_sectors.txt", "w")

    for sector in campaign_sectors:
        file.write(sector + "\n")

    file.close()

    print("\nCampaign Report Generated Successfully.")

except:
    print("Error while creating file!")