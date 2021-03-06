class Settings(object):
    """docstring for Setting"""

    def __init__(self):
        super().__init__()
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.screen_bg = (230, 230, 230)
        # 飞船速度设置
        self.ship_left_limit = 3
        # 子弹设置
        self.bullet_width = 5
        self.bullet_heigth = 10
        self.bullet_color = (0, 0, 0)
        self.max_bullets_num = 3
        # 外星人设置
        self.fleet_drop_speed = 20
        # 1和-1表示方向
        self.fleet_direction = 1
        # 等级设置
        self.speed_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.alien_speed_factor = 0.5
        self.bullet_speed_factor = 2
        self.alien_points = 50 

    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_points =int(self.alien_points* self.speed_scale)
