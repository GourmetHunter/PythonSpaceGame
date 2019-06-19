import pygame

class MainMenu():
	def update(self):
		print("Update")

	def draw(self, screen):
		pygame.draw.line(screen, (255, 0, 0), [0, 0], [100, 100], 5)