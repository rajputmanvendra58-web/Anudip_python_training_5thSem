# Cricket Tournament Analytics System 
"""
Problem Statement 
Store statistics of at least 30 cricket players. 
Example Structure 
players = {     
"Virat": {         
"runs": 645,         
"matches": 12,         
"wickets": 0     } 
} 
Requirements 
1. Display all player statistics.  
2. Find highest run scorer.  
3. Find lowest run scorer.  
4. Calculate average runs.  
5. Find player with maximum wickets.  
6. Find all-rounders (runs > 300 and wickets > 5).  
7. Display players scoring above average.  
8. Create categories:  
o Star Performer  
o Good Performer  
o Average Performer  
o Poor Performer  
9. Generate team statistics.  
10. Display top 5 batsmen.  
11. Display top 5 bowlers.  
12. Create a separate dictionary for award winners.
"""
# Cricket Tournament Analytics System

players = {}

while True:
    try:
        n = int(input("Enter number of players: "))

        if n >= 30:
            break

        else:
            print("Minimum 30 players required.")

    except ValueError:
        print("Enter valid number.")

for i in range(n):

    print("\nEnter Details of Player", i + 1)

    while True:

        name = input("Enter Player Name: ").strip()

        if name == "":
            print("Name cannot be empty.")

        elif name in players:
            print("Player already exists.")

        else:
            break

    while True:

        try:
            runs = int(input("Enter Runs: "))

            if runs >= 0:
                break

            else:
                print("Runs cannot be negative.")

        except ValueError:
            print("Enter valid runs.")

    while True:

        try:
            matches = int(input("Enter Matches Played: "))

            if matches > 0:
                break

            else:
                print("Matches must be greater than 0.")

        except ValueError:
            print("Enter valid matches.")

    while True:

        try:
            wickets = int(input("Enter Wickets Taken: "))

            if wickets >= 0:
                break

            else:
                print("Wickets cannot be negative.")

        except ValueError:
            print("Enter valid wickets.")

    players[name] = {
        "runs": runs,
        "matches": matches,
        "wickets": wickets
    }

while True:

    print("\n===== Cricket Tournament Analytics =====")
    print("1. Display All Players")
    print("2. Highest Run Scorer")
    print("3. Lowest Run Scorer")
    print("4. Average Runs")
    print("5. Maximum Wickets")
    print("6. Find All-Rounders")
    print("7. Players Above Average")
    print("8. Categorize Players")
    print("9. Team Statistics")
    print("10. Top 5 Batsmen")
    print("11. Top 5 Bowlers")
    print("12. Award Winners")
    print("13. Tournament Report")
    print("14. Exit")

    try:

        choice = int(input("Enter Choice: "))
        # --------------------------------------------------

        if choice == 1:

            print("\n===== All Player Statistics =====")

            for name, data in players.items():

                print("\nPlayer Name :", name)
                print("Runs :", data["runs"])
                print("Matches :", data["matches"])
                print("Wickets :", data["wickets"])

        # --------------------------------------------------

        elif choice == 2:

            max_runs = -1
            top_player = ""

            for name, data in players.items():

                if data["runs"] > max_runs:
                    max_runs = data["runs"]
                    top_player = name

            print("\n===== Highest Run Scorer =====")
            print("Player Name :", top_player)
            print("Runs :", max_runs)

        # --------------------------------------------------

        elif choice == 3:

            first = True

            for name, data in players.items():

                if first:
                    min_runs = data["runs"]
                    low_player = name
                    first = False

                elif data["runs"] < min_runs:
                    min_runs = data["runs"]
                    low_player = name

            print("\n===== Lowest Run Scorer =====")
            print("Player Name :", low_player)
            print("Runs :", min_runs)

        # --------------------------------------------------

        elif choice == 4:

            total_runs = 0

            for data in players.values():
                total_runs += data["runs"]

            average_runs = total_runs / len(players)

            print("\n===== Average Runs =====")
            print("Average Runs =", round(average_runs, 2))

        # --------------------------------------------------

        elif choice == 5:

            max_wickets = -1
            best_bowler = ""

            for name, data in players.items():

                if data["wickets"] > max_wickets:
                    max_wickets = data["wickets"]
                    best_bowler = name

            print("\n===== Maximum Wickets =====")
            print("Player Name :", best_bowler)
            print("Wickets :", max_wickets)
                    # --------------------------------------------------

        elif choice == 6:

            print("\n===== All Rounders =====")

            found = False

            for name, data in players.items():

                if data["runs"] > 300 and data["wickets"] > 5:
                    print(name)
                    found = True

            if found == False:
                print("No All-Rounders Found.")

        # --------------------------------------------------

        elif choice == 7:

            total_runs = 0

            for data in players.values():
                total_runs += data["runs"]

            average_runs = total_runs / len(players)

            print("\n===== Players Above Average =====")
            print("Average Runs =", round(average_runs, 2))

            found = False

            for name, data in players.items():

                if data["runs"] > average_runs:
                    print(name, "-", data["runs"])
                    found = True

            if found == False:
                print("No Player Found.")

        # --------------------------------------------------

        elif choice == 8:

            print("\n===== Player Categories =====")

            for name, data in players.items():

                runs = data["runs"]

                if runs >= 500:
                    category = "Star Performer"

                elif runs >= 300:
                    category = "Good Performer"

                elif runs >= 150:
                    category = "Average Performer"

                else:
                    category = "Poor Performer"

                print(name, ":", category)

        # --------------------------------------------------

        elif choice == 9:

            total_runs = 0
            total_wickets = 0
            total_matches = 0

            for data in players.values():

                total_runs += data["runs"]
                total_wickets += data["wickets"]
                total_matches += data["matches"]

            print("\n===== Team Statistics =====")

            print("Total Players :", len(players))
            print("Total Runs :", total_runs)
            print("Total Wickets :", total_wickets)
            print("Total Matches :", total_matches)

            print("Average Runs :", round(total_runs / len(players), 2))
            print("Average Wickets :", round(total_wickets / len(players), 2))
                    # --------------------------------------------------

        elif choice == 10:

            print("\n===== Top 5 Batsmen =====")

            temp = players.copy()

            count = 0

            while count < 5 and len(temp) > 0:

                max_runs = -1
                best_player = ""

                for name, data in temp.items():

                    if data["runs"] > max_runs:
                        max_runs = data["runs"]
                        best_player = name

                print(count + 1, ".", best_player, "-", max_runs)

                del temp[best_player]

                count += 1

        # --------------------------------------------------

        elif choice == 11:

            print("\n===== Top 5 Bowlers =====")

            temp = players.copy()

            count = 0

            while count < 5 and len(temp) > 0:

                max_wickets = -1
                best_bowler = ""

                for name, data in temp.items():

                    if data["wickets"] > max_wickets:
                        max_wickets = data["wickets"]
                        best_bowler = name

                print(count + 1, ".", best_bowler, "-", max_wickets)

                del temp[best_bowler]

                count += 1

        # --------------------------------------------------

        elif choice == 12:

            award_winners = {}

            for name, data in players.items():

                if data["runs"] > 500 or data["wickets"] > 15:

                    award_winners[name] = data

            print("\n===== Award Winners =====")

            if len(award_winners) == 0:

                print("No Award Winners Found.")

            else:

                for name, data in award_winners.items():

                    print("\nPlayer :", name)
                    print("Runs :", data["runs"])
                    print("Wickets :", data["wickets"])

        # --------------------------------------------------

        elif choice == 13:

            print("\n===== Tournament Report =====")

            total_runs = 0
            total_wickets = 0
            total_matches = 0

            max_runs = -1
            top_player = ""

            max_wickets = -1
            top_bowler = ""

            for name, data in players.items():

                total_runs += data["runs"]
                total_wickets += data["wickets"]
                total_matches += data["matches"]

                if data["runs"] > max_runs:
                    max_runs = data["runs"]
                    top_player = name

                if data["wickets"] > max_wickets:
                    max_wickets = data["wickets"]
                    top_bowler = name

            print("Total Players :", len(players))
            print("Total Runs :", total_runs)
            print("Total Wickets :", total_wickets)
            print("Total Matches :", total_matches)

            print("\nHighest Run Scorer")
            print(top_player, "-", max_runs)

            print("\nHighest Wicket Taker")
            print(top_bowler, "-", max_wickets)

            print("\nAverage Runs :", round(total_runs / len(players), 2))
            print("Average Wickets :", round(total_wickets / len(players), 2))

        # --------------------------------------------------

        elif choice == 14:

            print("Program Ended Successfully.")
            break

        # --------------------------------------------------

        else:

            print("Please Enter Choice Between 1 and 14.")

    except ValueError:

        print("Invalid Input. Enter A Number.")