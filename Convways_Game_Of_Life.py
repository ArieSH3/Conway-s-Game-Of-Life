'''
	Author: Stefan Popovic
	Date  : 26/05/2021

	About : Creating a Conway's game of life to be run in terminal with ASCII characters

	Rules:
		1. Any live cell with two or three live neighbours survives
		2. Any dead cell with three live neighbours becomes a live cell
		3. All other live cells die in the next generation. Similarly, all other dead cells stay dead

		** All cells with no pixel(character) are considered dead and can be revived regardless if
		   there was or wasn't a character alive there before.
	
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

import numpy # Will use to speed up looping through nested lists
import pprint
import time


# Will be used for both a number of elements in nested list and the number of nested lists
grid_size = 60

# Outer boundary for all the nested lists
outer_list = []

# Alive and dead pixels(characters) that will be displayed on grid
dead = ' '
alive = '#'

# Elements for borders
top_bottom_border = '_'
left_right_border = '|'


# 			---- MAIN PROGRAM FUNCTION ----
def main():
	
	creating_grid()
	# unpacking_lists()
	
	while True:
		time.sleep(2)
		running_game()
		unpacking_lists()





# Creates a grid with 4 pixels(characters) in the middle in the shape of upside down T
def creating_grid():
	for i in range(grid_size):
		nested_list = []
		for j in range(grid_size):
			# Checking if to draw top or bottom border
			if i==0 or i== grid_size-1:
				nested_list.append(top_bottom_border)
			# Checking if to draw left or right border
			elif j==0 or j== grid_size-1:
				nested_list.append(left_right_border)
			# Adding alive characters to specific spot in grid                         -------
			elif i==int(grid_size/2)-4 and j>int(grid_size/2)-5 and j<int(grid_size/2)+5:
				nested_list.append(alive)
			# Adding alive characters to specific spot in grid                         -------
			elif i==int(grid_size/2)-3 and j>int(grid_size/2)-5 and j<int(grid_size/2)+5:
				nested_list.append(alive)
			# Adding alive characters to specific spot in grid                         -------
			elif i==int(grid_size/2)-2 and j>int(grid_size/2)-5 and j<int(grid_size/2)+5:#	 |__ Just a custom addition of elements to grid
				nested_list.append(alive)					#		                         |   Can be changed however you like
			# Adding alive characters to specific spot in grid                         ------
			elif i==int(grid_size/2)-1 and j>int(grid_size/2)-5 and j<int(grid_size/2)+5:
				nested_list.append(alive)
			# Adds all the dead characters to the grid
			else:
				nested_list.append(dead)

		outer_list.append(nested_list)


def running_game():
	for i in range(len(outer_list)):
		for j in range(len(outer_list[i])):
			log = 0
			# Checks left of the element
			if j != 0:
				if outer_list[i][j-1] == alive:
					log += 1
			# Checks right of the element
			if j != grid_size-1: 
				if outer_list[i][j+1] == alive:
					log += 1
			# Checks above the element
			if i != 0:
				if outer_list[i-1][j] == alive:
					log += 1
			# Checks below the element
			if i != grid_size-1:
				if outer_list[i+1][j] == alive:
					log += 1
			# Checks top left
			if i != 0 and j != 0:
				if outer_list[i-1][j-1] == alive:
					log += 1
			# Checks top right
			if i != 0 and j != grid_size-1:
				if outer_list[i-1][j+1] == alive:
					log += 1
			# Checks bottom left
			if i != grid_size-1 and j != 0:
				if outer_list[i+1][j-1] == alive:
					log += 1
			# Checks bottom right
			if i != grid_size-1 and j != grid_size-1:
				if outer_list[i+1][j+1] == alive:
					log += 1

			# Checks if cell can be alive in current situation		
			if log<2 or log>3:
				outer_list[i][j] = dead
			# Checks if cell is dead and if it has 3 alive neighbour cells
			# then that dead cell will come alive
			if outer_list[i][j] == dead and log == 3:
				outer_list[i][j] = alive

# Unpacking nested lists for nicer grid print look
def unpacking_lists():
	for row in outer_list:
		print(*row)







main()
