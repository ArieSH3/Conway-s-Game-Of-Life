'''
	Author: Stefan Popovic
	Date  : 26/05/2021

	About : Creating a Conway's game of life to be run in terminal with ASCII characters

	Resources: Drawing a grid in pygame
			   ||||||||||||||||||||||||
			   https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame
			   http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

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
GRID_SIZE = 150 # 60*5 # 60

fps = 0.1 #0.01

WHITE  = (255,255,255)
BLACK  = (0  ,0  ,0)
GREEN  = (100,200,100)
BLUE   = (100,100,250)

WINDOW_WIDTH  = 1000
WINDOW_HEIGHT = 1000

block_width  = WINDOW_WIDTH//GRID_SIZE # 4 # 20
block_height = WINDOW_HEIGHT//GRID_SIZE # 4 # 20

# Outer boundary for all the nested lists
outer_list = []

# ALIVE and DEAD pixels(characters) that will be displayed on grid
DEAD = '0'
ALIVE = '1'

# 			---- MAIN PROGRAM FUNCTION ----
def main():
	global screen, clock
	pygame.init()
	creating_grid()
	# Setting the starting position of alive cells
	# outer_list[GRID_SIZE//2][GRID_SIZE//2] = ALIVE
	# outer_list[GRID_SIZE//2+1][GRID_SIZE//2] = ALIVE
	# outer_list[GRID_SIZE//2+2][GRID_SIZE//2] = ALIVE
	# outer_list[GRID_SIZE//2+2][GRID_SIZE//2+1] = ALIVE
	# outer_list[GRID_SIZE//2+1][GRID_SIZE//2+2] = ALIVE
	for x in range(0,GRID_SIZE,2):
		for y in range(GRID_SIZE):
			outer_list[x][y] = ALIVE

	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption('Game of Life')

	clock = pygame.time.Clock()
	screen.fill(BLACK)

	#unpacking_lists()

	while True:
		time.sleep(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		step_by_step_grid_draw()
		running_game()


# Draws a grid in pygame
def step_by_step_grid_draw():
	tracker = 0
	for row in range(0, GRID_SIZE):
		for column in range(0, GRID_SIZE):
			colour = BLACK
			if outer_list[row][column] == ALIVE:
				colour = WHITE
			else:
				colour = BLACK
			rect = pygame.Rect(row*block_width, column*block_height, block_width, block_height)
			pygame.draw.rect(screen, colour, rect)
	pygame.display.update()



# Creates a grid with 4 pixels(characters) in the middle in the shape of upside down T
def creating_grid():
	for i in range(GRID_SIZE):
		nested_list = []
		for j in range(GRID_SIZE):
				nested_list.append(DEAD)

		outer_list.append(nested_list)


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
