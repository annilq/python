import pygame
from pygame.sprite import Group 
from settings import Settings
from game_stat import GameStat
import game_functions as gf
from ship import Ship
from button import Button
def run_game():
    pygame.init()
    pygame.display.set_caption("alien invasion")
    al_settings=Settings()
    stat=GameStat(al_settings)
    screen=pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    al_ship=Ship(screen,al_settings)
    al_aliens=Group()
    gf.create_fleet(screen,al_settings,al_ship,al_aliens)
    al_bullets=Group()
    al_button=Button(al_settings,screen,"play")
    while True:
        gf.check_events(al_settings,screen,stat,al_ship,al_bullets,al_button)
        if stat.game_active:
            # 每次循环都更新飞船与子弹的位置
            al_ship.update()
            gf.update_aliens(al_settings,screen,al_ship,al_aliens,al_bullets,stat) 
            gf.update_bullets(al_settings,screen,al_ship,al_bullets,al_aliens)
        gf.update_screen(al_settings,screen,al_ship,al_bullets,al_aliens,stat,al_button)

run_game()