class Settings:
    """储存游戏中所有的类"""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 190, 60, 60
        self.bullets_allowed = 15
        self.fleet_drop_speed=10
        self.ship_limit=3
        self.score_scale=1.5
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 5.0
        self.bullet_speed = 2.0
        self.alien_speed = 3.0
        self.fleet_direction = 1
        self.aliens_points = 50
    def increase_speed(self):
        """提高速度"""
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.aliens_points= int(self.aliens_points*self.score_scale)
        print(self.aliens_points)