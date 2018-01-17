import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self,screen,settings):
		super().__init__()
		self.screen = screen
		self.settings=settings
		self.image = pygame.image.load("./images/alien.bmp")
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)

	def check_edges(self):
		screen=self.screen.get_rect()
		if self.rect.right>screen.right:
			return True
		if self.rect.left<0:
			return True

	def update(self):
		self.x+=(self.settings.alien_speed_factor*self.settings.fleet_direction)
		self.rect.x=self.x

	def blitme(self):
		self.screen.blit(self.image,self.rect)

