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


# Will be used for both a number of elements in nested list and the number of nested lists
grid_size = 20 

outer_list = []
no_element = ' '
element = '#'

# Setting up pretty printer so nested lists are printed below eachother instead of next to eachother
pp = pprint.PrettyPrinter(indent=1)

for i in range(grid_size):
	nested_list = []
	for j in range(grid_size):
		if i==grid_size-1 and j>grid_size-2 and j<grid_size+2:
			nested_list.append(element)
		else:
			nested_list.append(no_element)

	outer_list.append(nested_list)

pp.pprint(outer_list)
input()
# print(outer_list)

