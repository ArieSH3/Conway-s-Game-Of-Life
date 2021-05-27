'''
	Author: Stefan Popovic
	Date  : 26/05/2021

	About : Creating a Conway's game of life to be run in terminal with ASCII characters

	Resources: Drawing a grid in pygame
			   ||||||||||||||||||||||||
			   https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame

	Rules:
		1. Any live cell with two or three live neighbours survives
		2. Any DEAD cell with three live neighbours becomes a live cell
		3. All other live cells die in the next generation. Similarly, all other DEAD cells stay DEAD

		** All cells with no pixel(character) are considered DEAD and can be revived regardless if
		   there was or wasn't a character ALIVE there before.
	
	How it will work:
	
		Will maybe use nested lists for grid or just use one list and manually set that each
	row has for example 10 pixels(characters) so it might be easier to add and subtract 10 +-1
	to determine if there are any neighbours above, below or diagonally above or below with.

	Alternative for nested lists is that I can check current list +-1 (list above and list below)
	and the same position of current pixel(character) and +-1 to check its diagonals in which case
	again every of those possible 8 positions around element will be checked.

	List:
					__  __  __
		nest 1:    |__||__||__|
				    __  __  __
		nest 2:	   |__||##||__|	- Element ## checks position +-1 which are right and left of it
				    __  __  __    then checks its position on list above and then +-1 for that
		nest 3:	   |__||__||__|   and then checks its position on list below and again +-1 for
								  its immediate neighbours.
								  
								  In the end, all possible neighbours are checked for and if there
								  is a pixel(character) on one of those positions, current pixel
								  logs how many of them there are and according to the rules it 
								  either lives or dies.
'''

import pygame
import time


# Will be used for both a number of elements in nested list and the number of nested lists
GRID_SIZE = 60

# Outer boundary for all the nested lists
outer_list = []

# ALIVE and DEAD pixels(characters) that will be displayed on grid
DEAD = ' '
ALIVE = '#'

# 			---- MAIN PROGRAM FUNCTION ----
def main():
	
	creating_grid()
	placing_initial_characters()
	time.sleep(2)
	while True:
		time.sleep(0.5)
		running_game()
		unpacking_lists()




# Creates a grid with 4 pixels(characters) in the middle in the shape of upside down T
def creating_grid():
	for i in range(GRID_SIZE):
		nested_list = []
		for j in range(GRID_SIZE):
				nested_list.append(DEAD)

		outer_list.append(nested_list)



# Placing characters on the grid
# Current setup creates vertical lines sepparated by one empty space
def placing_initial_characters():
	for i in range(0,len(outer_list),2): # Step is set to 2
		for j in range(0,len(outer_list[i])):
			# Adding ALIVE characters to specific spot in grid                         ------
			#if i==int(GRID_SIZE/2)-1 and j>int(GRID_SIZE/2)-5 and j<int(GRID_SIZE/2)+5:
			#if i==int(GRID_SIZE/2)-1 or i==int(GRID_SIZE/2)-2 or i==int(GRID_SIZE/2)-3:
			outer_list[i][j] = ALIVE

	for row in outer_list:
		print(*row)




# Runs the game and does checks for positions around current element and if its
# ALIVE or DEAD so it can apply the rules in the end
def running_game():
	for i in range(len(outer_list)):
		for j in range(len(outer_list[i])):
			log = 0
			# Checks left of the element
			if j != 0:
				if outer_list[i][j-1] == ALIVE:
					log += 1
			# Checks right of the element
			if j != GRID_SIZE-1: 
				if outer_list[i][j+1] == ALIVE:
					log += 1
			# Checks above the element
			if i != 0:
				if outer_list[i-1][j] == ALIVE:
					log += 1
			# Checks below the element
			if i != GRID_SIZE-1:
				if outer_list[i+1][j] == ALIVE:
					log += 1
			# Checks top left
			if i != 0 and j != 0:
				if outer_list[i-1][j-1] == ALIVE:
					log += 1
			# Checks top right
			if i != 0 and j != GRID_SIZE-1:
				if outer_list[i-1][j+1] == ALIVE:
					log += 1
			# Checks bottom left
			if i != GRID_SIZE-1 and j != 0:
				if outer_list[i+1][j-1] == ALIVE:
					log += 1
			# Checks bottom right
			if i != GRID_SIZE-1 and j != GRID_SIZE-1:
				if outer_list[i+1][j+1] == ALIVE:
					log += 1

			

			#          ** APPLYING RULES **

			# Checks if cell can be ALIVE in current situation		
			if log<2 or log>3:
				outer_list[i][j] = DEAD
			# Checks if cell is DEAD and if it has 3 ALIVE neighbour cells
			# then that DEAD cell will come ALIVE
			if outer_list[i][j] == DEAD and log == 3:
				outer_list[i][j] = ALIVE



# Unpacking nested lists for nicer grid print look
def unpacking_lists():
	for row in outer_list:
		print(*row)







main()
