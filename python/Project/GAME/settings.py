class Settings:
    '''
    存储游戏中所有设置的类
    '''
    def __init__(self):
        #初始化游戏设置

        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed = 5
        self.ship_limit = 0

        #子弹设置
        self.bullet_speed = 6.0
        self.bullet_width = 1200
        self.bullet_height = 3
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 100

        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        #fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1