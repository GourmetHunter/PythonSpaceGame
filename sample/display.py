import pygame

class Display:
	def __init__(self, width, heigth):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)
		self.BLUE = (0, 0, 255)
		self.screen = pygame.display.set_mode((width, heigth))
		pygame.display.set_caption("Space Game")

	def get_events(self):
		return pygame.event.get()

	def get_screen(self):
		return self.screen

	def drawscreen(self):
		pygame.display.flip()
		self.clock.tick(60)

	def quit(self):
		pygame.quit()