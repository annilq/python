import sys
import pygame
def check_events(ship):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			keydown_event(event,ship)
		elif event.type==pygame.KEYUP:
			keyup_event(ship)
def keydown_event(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moveing_right=True
	elif event.key==pygame.K_LEFT:
		ship.moveing_left=True

def keyup_event(ship):
	ship.moveing_right=False
	ship.moveing_left=False

def update_screen(settings,screen,ship):
	# 每次都要填充背景色，否则会有飞机移动痕迹
    screen.fill(settings.screen_bg)
    ship.blitme()
    pygame.display.flip()
