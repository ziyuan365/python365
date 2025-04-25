import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import psutil 
from game_stats import GameStats 

def check_memory_usage(max_memory_mb=1024):
    process = psutil.Process()
    memory_usage = process.memory_info().rss / (1024 * 1024)  # MB
    if memory_usage > max_memory_mb:
        print(f"内存占用过高（{memory_usage:.2f}MB),程序终止！")
        sys.exit(1)

class AlienInvasion:
    def __init__(self):#__init__ 是 Python 的构造函数，在创建类实例时自动调用
        
        #初始化所有 Pygame 模块，这是使用 Pygame 前的必要步骤
        pygame.init()   

        self.clock=pygame.time.Clock()

        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        #全屏模式下运行游戏
        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        
        self.settings.screen_width = self.screen.get_rect().width

        self.settings.screen_height = self.screen.get_rect().height

        self.stats = GameStats(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

        #游戏启动后处于活动状态
        self.game_active = True

    def run_game(self):
        #开始游戏主循环
        while True:
            self._check_events()

            if self.game_active == True:

                self.ship.update()

                self._updata_bullets()

                self._update_aliens()

                self._updata_screen()

            self.clock.tick(60)

            if pygame.time.get_ticks() % 1000 == 0:  # 每秒检查一次
                check_memory_usage(1024)  # 限制1GB内存

            #监听键盘和鼠标事件
    def _check_events(self):
            for event in pygame.event.get():    #获取所有发生的事件（如按键、鼠标移动等）
                if event.type == pygame.QUIT:   #检查是否是窗口关闭事件
                   
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                     self._check_KEYDOWN_events(event)

                elif event.type == pygame.KEYUP:
                     self._check_KEYUP_events(event)


    def _check_KEYDOWN_events(self,event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()

    def _check_KEYUP_events(self,event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _updata_bullets(self):
        self.bullets.update()

        #删除以消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collsions()
        
    def _check_bullet_alien_collsions(self):
        #检查是否有子弹击中了外星人，如果有则删除相应子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True ,True
        )
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
    def _fire_bullet(self):
         #创建一颗子弹，并将其加入编组bullet
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    #每次循环时都重绘屏幕
    def _updata_screen(self):
            self.screen.fill(self.settings.bg_color)

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            #让外星人现身
            self.aliens.draw(self.screen)

            #让最近绘制的屏幕可见
            pygame.display.flip()

    def _create_fleet(self):
         #创建一个外形舰队

         #创建一个外星人,再不断添加，直到没有空间添加外星人为止
         alien = Alien(self)
         alien_width,alien_height = alien.rect.size

         current_x,current_y = alien_width,alien_height
         while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width -  2* alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            current_y += 2 * alien_height
            current_x = alien_width

    def _create_alien(self,x_position,y_position):
         new_alien = Alien(self)

         new_alien.x = x_position

         new_alien.rect.x = x_position

         new_alien.rect.y = y_position

         self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()

        self.aliens.update()

        #检测外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        #在右外星人到达边缘的时候采取相应措施
        for alien in self.aliens.sprites():     #alien继承了aliens的属性所以alien可以调用check_edges（）
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #将整个外星人舰队向下移动，并改变他们的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        #响应飞船和外星人的碰撞
        #将ships_left减为1
        
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
        else :
            self.game_active = False

        #创建一个新的外星人舰队，并将飞船位置放在底部中央
        self._create_fleet()
        self.ship._center_ship()

        #暂停
        sleep(0.5)
    def _check_aliens_bottom(self):
        #检查是否有外星人抵达了屏幕下边缘
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #像飞船被撞一样进行处理
                self._ship_hit()
                break

            
if __name__ == "__main__":
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()