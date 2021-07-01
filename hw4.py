import random

#problem A.

def expo(x,y):
#==========================================
# Purpose: Raises the power of one number to another and returns result
# Input Parameter(s): 
# x: Base of operation
# y: Exponent of operation
# Return Value(s): Power of x raised to y 
#==========================================
    prod = 1
    i = 0
    while i < y:
        total = 0
        j = 0
        while j < x:
            total += prod
            j += 1
            print("prod",prod,"total",total)
        prod = total
        i += 1
    return prod

#problem B.

def rps_round():
#==========================================
# Purpose: Pits user against computer in a round of 'Rock, paper, scissors', and returns outcome
# Input Parameter(s): None
# Return Value(s): -1, 0, and 1 for a user loss, tie, and a user victory, respectively 
#==========================================
	user_move = input("Enter R, P, or S: ")
	while user_move != 'R' and user_move != 'P' and user_move != 'S':
		print("Invalid Input")
		user_move = input("Enter R, P, or S: ")
	comp_move = random.choice('RPS')
	if user_move == "R" and comp_move == "R":
		print("Computer selects", comp_move)
		print("Tie!")
		return 0
	elif user_move == "R" and comp_move == "P":
		print("Computer selects", comp_move)
		print("Computer wins!")
		return -1
	elif user_move == "R" and comp_move == "S":
		print("Computer selects", comp_move)
		print("Player wins!")
		return 1
	elif user_move == "P" and comp_move == "R":
		print("Computer selects", comp_move)
		print("Player wins!")
		return 1
	elif user_move == "P" and comp_move == "P":
		print("Computer selects", comp_move)
		print("Tie!")
		return 0
	elif user_move == "P" and comp_move == "S":
		print("Computer selects", comp_move)
		print("Computer wins!")
		return -1
	elif user_move == "S" and comp_move == "R":
		print("Computer selects", comp_move)
		print("Computer wins!")
		return -1
	elif user_move == "S" and comp_move == "P":
		print("Computer selects", comp_move)
		print("Player wins!")
		return 1
	elif user_move == "S" and comp_move == "S":
		print("Computer selects", comp_move)
		print("Tie!")
		return 0

#problem C.

def rps_game(num_wins):
#==========================================
# Purpose: Pits user against computer in a game of 'rock, paper, scissors', and returns winner
# Input Parameter(s):
# num_wins: number of rounds won required to win the game
# Return Value(s): -1, and 1 for computer victory and user victory, respectively
#==========================================
	user_wins = 0
	comp_wins = 0
	while user_wins < num_wins and comp_wins < num_wins:
		rps_result = rps_round()
		if rps_result == 1:
			user_wins += 1
		elif rps_result == -1:
			comp_wins += 1
		print("")
		print("")
		print("player wins:", user_wins)
		print("Computer wins:", comp_wins)
		print("")
		print("")
	if user_wins > comp_wins:
		return 1
	if comp_wins > user_wins:
		return -1















