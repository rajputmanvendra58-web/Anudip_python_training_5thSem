#Program to enter 11 player scores using List
player_score=[]
#loop for 11 players
for i in range (11):
    score=int(input("Enter the score of player {}: " .format(i+1)))
    player_score.append(score)
print("\n-----------PLAYER SCORES-----------")
print("Score of player{}: ",player_score)

#for finding the highest score
max_score=player_score[0]
for index in range (1,len(player_score)):
    if player_score[index]>max_score:
        max_score=player_score[index]
print("The Highest Score is : ",max_score)