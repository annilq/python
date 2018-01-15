import pygame
from settings import Settings
import game_functions as gf
from ship import Ship
def run_game():
    pygame.init()
    pygame.display.set_caption("alien invasion")
    al_settings=Settings()
    screen=pygame.display.set_mode((al_settings.screen_width,al_settings.screen_heigth))
    al_ship=Ship(screen,al_settings)
    while True:
        gf.check_events(al_ship)
        # 每次循环都更新飞船位置
        al_ship.update()
        gf.update_screen(al_settings,screen,al_ship)

run_game()