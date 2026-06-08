# Cricket Tournament Statistics 
"""
Problem Statement 
Runs scored by players in a tournament: runs = {     
"Virat": 645,     
"Rohit": 512,     
"Gill": 698,     
"Rahul": 435,     
"Hardik": 278,     
"Pant": 534,     
"Surya": 389,     
"Jadeja": 301,     
"Iyer": 455,     
"KL": 410 } 
Tasks 
1. Display players scoring more than 500 runs.  
2. Find the Orange Cap winner.  
3. Find the lowest scorer.  
4. Calculate total runs scored.  
5. Create a list of players scoring below 400.  
6. Count players scoring between 400 and 600 runs.  
"""

# Given data
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}
# 1. Display players scoring more than 500 runs
players_above_500 = [player for player, score in runs.items() if score > 500]
print("Players scoring more than 500 runs:", players_above_500)
# 2. Find the Orange Cap winner
orange_cap_winner = max(runs, key=runs.get)
print("Orange Cap winner:", orange_cap_winner)
# 3. Find the lowest scorer
lowest_scorer = min(runs, key=runs.get)
print("Lowest scorer:", lowest_scorer)
# 4. Calculate total runs scored
total_runs = sum(runs.values())
print("Total runs scored:", total_runs)
# 5. Create a list of players scoring below 400
players_below_400 = [player for player, score in runs.items() if score < 400]
print("Players scoring below 400 runs:", players_below_400)
# 6. Count players scoring between 400 and 600 runs
players_between_400_and_600 = [player for player, score in runs.items() if 400 <= score <= 600]
count_between_400_and_600 = len(players_between_400_and_600)
print("Number of players scoring between 400 and 600 runs:", count_between_400_and_600)


"""
Output:
Players scoring more than 500 runs: ['Virat', 'Rohit', 'Gill', 'Pant']
Orange Cap winner: Gill
Lowest scorer: Hardik
Total runs scored: 4757
Players scoring below 400 runs: ['Hardik', 'Surya', 'Jadeja']
Number of players scoring between 400 and 600 runs: 4
"""