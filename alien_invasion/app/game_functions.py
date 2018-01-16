import sys
import pygame
from bullet import Bullet
def check_events(settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			keydown_event(event,settings,screen,ship,bullets)
		elif event.type==pygame.KEYUP:
			keyup_event(ship)

def keydown_event(event,settings,screen,ship,bullets):
	if event.key==pygame.K_RIGHT:
		ship.moveing_right=True
	elif event.key==pygame.K_LEFT:
		ship.moveing_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullets(settings,screen,ship,bullets)
		
def keyup_event(ship):
	ship.moveing_right=False
	ship.moveing_left=False


# 发射子弹
def fire_bullets(settings,screen,ship,bullets):
	if len(bullets)<settings.max_bullets_num:
		bullets.add(Bullet(settings,screen,ship))
# 更新子弹
def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_screen(settings,screen,ship,bullets):
	# 每次都要填充背景色，否则会有飞机移动痕迹
    screen.fill(settings.screen_bg)
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
