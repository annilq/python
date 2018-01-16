import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self,settings,screen,ship):
		super().__init__()
		self.screen = screen
		self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_heigth)
		# 子弹大小
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		# 子弹大小
		self.y=self.rect.y
		self.speed_factor=settings.bullet_speed_factor
		self.bullet_color=settings.bullet_color

	def update(self):
		self.rect.y-=self.speed_factor
	
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.bullet_color,self.rect)
