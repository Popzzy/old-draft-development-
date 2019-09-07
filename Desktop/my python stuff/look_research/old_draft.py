#!/usr/bin/ env python
#old_draft.py  -- old draft game 
import random

board = [['X', 'X', 'X'], [' ']*3, ['O', 'O', 'O']]
board = [char for row in board for char in row]  // flatten board

def draw(board):
	#the out put of the game
    print(board[6] + '--------------' + board[7] + '--------------' + board[8])
    print("|\\             |             /|")
    print("| \\            |            / |")
    print("|  \\           |           /  |")
    print("|   \\          |          /   |")
    print("|    \\         |         /    |")
    print("|     \\        |        /     |")
    print("|      \\       |       /      |")
    print("|       \\      |      /       |")
    print("|        \\     |     /        |")
    print("|         \\    |    /         |")
    print("|          \\   |   /          |")
    print("|           \\  |  /           |")
    print("|            \\ | /            |")
    print("|             \\|/             |")
    print(board[3] + '--------------' + board[4] + '--------------' + board[5])
    print("|             /|\\             |")
    print("|            / | \\            |")
    print("|           /  |  \\           |")
    print("|          /   |   \\          |")
    print("|         /    |    \\         |")
    print("|        /     |     \\        |")
    print("|       /      |      \\       |")
    print("|      /       |       \\      |")
    print("|     /        |        \\     |")
    print("|    /         |         \\    |")
    print("|   /          |          \\   |")
    print("|  /           |           \\  |")
    print("| /            |            \\ |")
    print("|/             |             \\|")
    print(board[0] + '--------------' + board[1] + '--------------' + board[2])

def input_letters():
	#we use 'x' and 'o'
	#one will select what to use
	letter = ''
	while not(letter== 'X' or letter == 'O'):
		print('Would you like to be "x" or "o"?')
		letter = input().upper()
		"""change into upper case"""
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', "X"]
