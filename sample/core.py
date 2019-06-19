from GameState import main_menu
import display
import pygame

class Core:
	def __init__(self):
		self.states = {
			'mainmenu': main_menu.MainMenu()
		}
		self.active_state = self.states.get('mainmenu')
		self.display = display.Display(1280, 720)
		self._running = True

	def run(self):
		while(self._running):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self._running = False
			self.update()
			self.draw()
		self.display.quit()

	def update(self):
		self.active_state.update()

	def draw(self):
		self.display.get_screen().fill(self.display.BLACK)
		self.active_state.draw(self.display.get_screen())
		self.display.drawscreen()