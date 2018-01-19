class GameStat():
	"""docstring for GameStat"""
	def __init__(self,settings):
		super().__init__()
		self.settings = settings
		self.game_active = True
		self.reset_stats()

	def reset_stats(self):
		self.ship_left_limit = self.settings.ship_left_limit