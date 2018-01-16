import pygame
class Ship(object):
	"""docstring for Ship"""
	def __init__(self, screen,settings):
		super().__init__()
		self.screen = screen
		self.image=pygame.image.load("./images/ship.bmp")
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		self.rect.centerx=float(self.screen_rect.centerx)
		self.rect.bottom=self.screen_rect.bottom
		self.ship_speed_factor=settings.ship_speed_factor
		self.moveing_right=False
		self.moveing_left=False

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""根据操作更新飞船位置"""
		if self.moveing_right and self.rect.right<self.screen_rect.right:
			self.rect.centerx+=self.ship_speed_factor
		if self.moveing_left and self.rect.left>self.screen_rect.left:
			self.rect.centerx-=self.ship_speed_factor



		