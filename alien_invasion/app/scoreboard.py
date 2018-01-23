import pygame.font


class Scoreboard():
    def __init__(self, settings, screen, stats):
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        score=round(self.stats.score,-1)
        score_str="{:,}".format(score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.screen_bg)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        score=round(self.stats.high_score,-1)
        score_str="{:,}".format(score)
        self.high_score_image = self.font.render(
            score_str, True, self.text_color, self.settings.screen_bg)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx - 20
        self.high_score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
