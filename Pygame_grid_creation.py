'''
	Creating a grid in pygame for Conway's game of life
'''

import pygame

WHITE  = (255,255,255)
BLACK  = (0  ,0  ,0)
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 400

def main():
	global SCREEN, CLOCK
	pygame.init()
	SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	CLOCK = pygame.time.Cock()
	SCREEN.fill(BLACK)

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
	 		pygame.draw.rect(SCREEN, WHITE, rect, 1)