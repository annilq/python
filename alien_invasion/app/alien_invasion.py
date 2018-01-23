import game_functions as gf
import pygame
from button import Button
from game_stat import GameStat
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    pygame.display.set_caption("alien invasion")
    al_settings = Settings()
    stat = GameStat(al_settings)
    screen = pygame.display.set_mode((al_settings.screen_width,
                                      al_settings.screen_height))
    # 飞船
    al_ship = Ship(screen, al_settings)
    # 外星人
    al_aliens = Group()
    gf.create_fleet(screen, al_settings, al_ship, al_aliens)
    # 子弹
    al_bullets = Group()
    # 开始按钮
    al_button = Button(al_settings, screen, "play")
    # 记分牌
    sb = Scoreboard(al_settings, screen, stat)
    while True:
        gf.check_events(al_settings, screen, stat, al_ship, al_bullets,
                        al_button)
        if stat.game_active:
            # 每次循环都更新飞船与子弹的位置
            al_ship.update()
            gf.update_aliens(al_settings, screen, al_ship, al_aliens,
                             al_bullets, stat,sb)

            gf.update_bullets(al_settings, screen,stat, al_ship, al_bullets,
                              al_aliens, sb)
                              
        gf.update_screen(al_settings, screen, al_ship, al_bullets, al_aliens,
                         stat, al_button, sb)


run_game()
