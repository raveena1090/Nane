#!/usr/bin/env python3

Player1 = input("Enter name for player1: ")
Player2 = input ("Enter name for player2: ")
print("Rules- Rock beats Scissors, Scissors beats Paper, Paper beats Rock")

print("Pick one: Rock, Paper, or Scissors")

P1 =input("%s, your pick?" % Player1)
P2 =input("%s, And yours?" % Player2)

def compare(P1, P2):
	if P1 == P2:
		return("Tie! Game Over!")
	elseif P1 == 'Rock':
		if P2 == 'Paper':
			return(Player2 + "Congratulations paper Wins!")
			else:
				return("Congratulations Scissors Wins!")
	elif P1 == 'Paper':
		if P2 == 'Scissors':
			return(Player2 + "Congratulations Scissors Wins!")
			else:
				return("Congratulations Rock Wins!")
	elif P1 == 'Rock':
		if P2  == 'Scissors':
			return(Player1 + "Congratulations Rock Wins!")
			else:
				return("Congratulations Paper Wins!")
			else:
				return("wrong Input! Pick One Rock , Paper , Scissors.")
				sys.exit()

print(compare(P1, P2))
