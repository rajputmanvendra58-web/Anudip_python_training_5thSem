# City Population & Development Dashboard
"""
Problem Statement 
The government wants to analyze city data. Store details of at least 30 cities. 
Example Structure 
cities = {     
"Delhi":{         
"population": 32000000,         
"area": 1484,         
"literacy": 89  } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
"""

# City Population & Development Dashboard

cities = {}

while True:
    try:
        n = int(input("Enter number of cities: "))

        if n >= 30:
            break
        else:
            print("Minimum 30 cities required.")

    except ValueError:
        print("Enter valid number.")

for i in range(n):

    print("\nEnter Details of City", i + 1)

    # City Name
    while True:

        city = input("Enter City Name: ").strip()

        if city == "":
            print("City name cannot be empty.")

        elif city in cities:
            print("City already exists.")

        else:
            break

    # Population
    while True:

        try:
            population = int(input("Enter Population: "))

            if population > 0:
                break
            else:
                print("Population must be greater than 0.")

        except ValueError:
            print("Enter valid population.")

    # Area
    while True:

        try:
            area = float(input("Enter Area (sq km): "))

            if area > 0:
                break
            else:
                print("Area must be greater than 0.")

        except ValueError:
            print("Enter valid area.")

    # Literacy Rate
    while True:

        try:
            literacy = float(input("Enter Literacy Rate (%): "))

            if 0 <= literacy <= 100:
                break
            else:
                print("Literacy rate must be between 0 and 100.")

        except ValueError:
            print("Enter valid literacy rate.")

    cities[city] = {
        "population": population,
        "area": area,
        "literacy": literacy
    }

while True:

    print("\n===== City Population Dashboard =====")
    print("1. Display All City Details")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Cities With Literacy Above 90%")
    print("6. Cities With Literacy Below Average")
    print("7. Calculate Population Density")
    print("8. City With Highest Density")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. High Literacy Cities")
    print("12. Low Literacy Cities")
    print("13. National Summary Report")
    print("14. Rank Cities By Density")
    print("15. Exit")

    try:

        choice = int(input("Enter Choice: "))
        # --------------------------------------------------

        if choice == 1:

            print("\n===== All City Details =====")

            for city, data in cities.items():

                print("\nCity :", city)
                print("Population :", data["population"])
                print("Area :", data["area"])
                print("Literacy Rate :", data["literacy"])

        # --------------------------------------------------

        elif choice == 2:

            max_population = -1
            most_populated_city = ""

            for city, data in cities.items():

                if data["population"] > max_population:

                    max_population = data["population"]
                    most_populated_city = city

            print("\n===== Most Populated City =====")
            print("City :", most_populated_city)
            print("Population :", max_population)

        # --------------------------------------------------

        elif choice == 3:

            first = True

            for city, data in cities.items():

                if first:

                    min_population = data["population"]
                    least_populated_city = city
                    first = False

                elif data["population"] < min_population:

                    min_population = data["population"]
                    least_populated_city = city

            print("\n===== Least Populated City =====")
            print("City :", least_populated_city)
            print("Population :", min_population)

        # --------------------------------------------------

        elif choice == 4:

            total_population = 0

            for data in cities.values():

                total_population += data["population"]

            average_population = total_population / len(cities)

            print("\n===== Average Population =====")
            print("Average Population :", round(average_population, 2))

        # --------------------------------------------------

        elif choice == 5:

            print("\n===== Cities With Literacy Above 90% =====")

            found = False

            for city, data in cities.items():

                if data["literacy"] > 90:

                    print(city, "-", data["literacy"], "%")
                    found = True

            if found == False:

                print("No City Found.")
                        # --------------------------------------------------

        elif choice == 6:

            total_literacy = 0

            for data in cities.values():

                total_literacy += data["literacy"]

            average_literacy = total_literacy / len(cities)

            print("\n===== Cities With Literacy Below Average =====")

            found = False

            for city, data in cities.items():

                if data["literacy"] < average_literacy:

                    print(city, "-", data["literacy"], "%")
                    found = True

            if found == False:

                print("No City Found.")

        # --------------------------------------------------

        elif choice == 7:

            print("\n===== Population Density =====")

            for city, data in cities.items():

                density = data["population"] / data["area"]

                print(city, ":", round(density, 2), "people/sq km")

        # --------------------------------------------------

        elif choice == 8:

            max_density = -1
            highest_density_city = ""

            for city, data in cities.items():

                density = data["population"] / data["area"]

                if density > max_density:

                    max_density = density
                    highest_density_city = city

            print("\n===== City With Highest Density =====")
            print("City :", highest_density_city)
            print("Density :", round(max_density, 2))

        # --------------------------------------------------

        elif choice == 9:

            print("\n===== City Categories =====")

            for city, data in cities.items():

                population = data["population"]

                if population < 1000000:
                    category = "Small"

                elif population < 5000000:
                    category = "Medium"

                else:
                    category = "Large"

                print(city, ":", category)

        # --------------------------------------------------

        elif choice == 10:

            print("\n===== Development Priority List =====")

            found = False

            for city, data in cities.items():

                if data["literacy"] < 75:

                    print(city)
                    found = True

            if found == False:

                print("No City Requires Priority Development.")
                        # --------------------------------------------------

        elif choice == 11:

            high_literacy_cities = {}

            for city, data in cities.items():

                if data["literacy"] >= 90:

                    high_literacy_cities[city] = data

            print("\n===== High Literacy Cities =====")

            if len(high_literacy_cities) == 0:

                print("No High Literacy Cities Found.")

            else:

                for city, data in high_literacy_cities.items():

                    print("\nCity :", city)
                    print("Literacy Rate :", data["literacy"])

        # --------------------------------------------------

        elif choice == 12:

            low_literacy_cities = {}

            for city, data in cities.items():

                if data["literacy"] < 75:

                    low_literacy_cities[city] = data

            print("\n===== Low Literacy Cities =====")

            if len(low_literacy_cities) == 0:

                print("No Low Literacy Cities Found.")

            else:

                for city, data in low_literacy_cities.items():

                    print("\nCity :", city)
                    print("Literacy Rate :", data["literacy"])

        # --------------------------------------------------

        elif choice == 13:

            print("\n===== National Summary Report =====")

            total_population = 0
            total_area = 0
            total_literacy = 0

            for data in cities.values():

                total_population += data["population"]
                total_area += data["area"]
                total_literacy += data["literacy"]

            avg_population = total_population / len(cities)
            avg_literacy = total_literacy / len(cities)

            print("Total Cities :", len(cities))
            print("Total Population :", total_population)
            print("Total Area :", round(total_area, 2))
            print("Average Population :", round(avg_population, 2))
            print("Average Literacy Rate :", round(avg_literacy, 2))

        # --------------------------------------------------

        elif choice == 14:

            print("\n===== Ranking Cities By Density =====")

            temp = cities.copy()

            rank = 1

            while len(temp) > 0:

                max_density = -1
                ranked_city = ""

                for city, data in temp.items():

                    density = data["population"] / data["area"]

                    if density > max_density:

                        max_density = density
                        ranked_city = city

                print(rank, ".", ranked_city,
                      "-", round(max_density, 2))

                del temp[ranked_city]

                rank += 1

        # --------------------------------------------------

        elif choice == 15:

            print("Program Ended Successfully.")
            break

        # --------------------------------------------------

        else:

            print("Please Enter Choice Between 1 and 15.")

    except ValueError:

        print("Invalid Input. Enter A Number.")