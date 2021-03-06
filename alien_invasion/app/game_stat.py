class GameStat():
    """docstring for GameStat"""

    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0
        self.level=1

    def reset_stats(self):
        self.ship_left_limit = self.settings.ship_left_limit
        self.score = 0
