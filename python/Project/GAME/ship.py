import pygame

class Ship():
    '''
    管理飞船类
    '''
    def __init__(self,ai_game):
        #初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load(r"D:\code\python\Project\GAME\images\ship.bmp")
        self.rect=self.image.get_rect()

        #每一艘飞船都放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom

        #飞船的属性x中储存一个浮点数
        self.x = float(self.rect.x)

        #移动标志（飞船一开始不动）
        self.moving_right = False
        self.moving_left = False


    def update(self):
        #根据移动标志调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

            # self.rect.x += 1

        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed

            # self.rect.x -= 1

        #根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def _center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)