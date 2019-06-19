from GameState import main_menu

class Core:
	def __init__(self):
		self.states = {
			'mainmenu': main_menu.MainMenu()
		}
		self.active_state = self.states.get('mainmenu')

	def run(self):
		self.active_state.update()
		self.active_state.draw()