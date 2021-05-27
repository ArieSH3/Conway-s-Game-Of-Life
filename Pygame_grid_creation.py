'''
	Creating a grid in pygame for Conway's game of life
'''

import pygame
# from pygame.locals import *

WHITE  = (255,255,255)
BLACK  = (0  ,0  ,0)
GREEN  = (50, 200, 50)
WINDOW_WIDTH  = 1030
WINDOW_HEIGHT = 1030

def main():
	global SCREEN, CLOCK
	pygame.init()
	SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	CLOCK = pygame.time.Clock()
	SCREEN.fill(WHITE)

	while True:
		drawGrid()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()


def drawGrid():
	block_size = 20 # Set the size of the grid block
	for x in range(0, WINDOW_WIDTH, block_size):
	 	for y in range(0, WINDOW_HEIGHT, block_size):
	 		rect = pygame.Rect(x, y, block_size, block_size)
	 		pygame.draw.rect(SCREEN, BLACK, rect, 1)



main()