import pygame
from pygame.sprite import Group 
from settings import Settings
import game_functions as gf
from ship import Ship
def run_game():
    pygame.init()
    pygame.display.set_caption("alien invasion")
    al_settings=Settings()
    screen=pygame.display.set_mode((al_settings.screen_width,al_settings.screen_heigth))
    al_ship=Ship(screen,al_settings)
    al_bullets=Group()
    while True:
        gf.check_events(al_settings,screen,al_ship,al_bullets)
        # 每次循环都更新飞船与子弹的位置
        al_ship.update()
        gf.update_bullets(al_bullets)
        gf.update_screen(al_settings,screen,al_ship,al_bullets)

run_game()