class Settings(object):
	"""docstring for Setting"""
	def __init__(self):
		super().__init__()
		# 屏幕设置
		self.screen_width = 900
		self.screen_heigth = 600
		self.screen_bg = (230,230,230)
		# 飞船速度设置
		self.ship_speed_factor=0.5
		# 子弹设置
		self.bullet_speed_factor=2
		self.bullet_width=5
		self.bullet_heigth=10
		self.bullet_color=(0,0,0)
		self.max_bullets_num=3
		