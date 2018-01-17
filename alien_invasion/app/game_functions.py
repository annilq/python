import sys
import pygame
from bullet import Bullet
from alien import Alien
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

def create_fleet(screen,al_settings,ship,aliens):
	cols,rows=get_alien_cols_rows(screen,al_settings,ship)
	for row in range(rows):
		for col in range(cols):
			create_alien(screen,al_settings,aliens,row,col)


def get_alien_cols_rows(screen,al_settings,ship):
	alien=Alien(screen,al_settings)
	screen_width=al_settings.screen_width
	alien_width=alien.rect.width
	screen_width_space=screen_width-(2*alien_width)
	alien_cols=int(screen_width_space/(2*alien_width))

	ship_height=ship.rect.height
	screen_height=al_settings.screen_height
	alien_height=alien.rect.height
	screen_height_space=screen_height-(2*alien_height)-ship_height
	alien_rows=int((screen_height_space)/(2*alien_height))
	print(alien_cols,alien_rows)
	return (alien_cols,alien_rows)

# 创建外星人
def create_alien(screen,al_settings,aliens,row,col):
	alien=Alien(screen,al_settings)
	alien.x=alien.rect.width+2*alien.rect.width*col
	alien.y=alien.rect.height+2*alien.rect.height*row
	alien.rect.x=alien.x
	alien.rect.y=alien.y
	aliens.add(alien)

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

def update_aliens(al_settings,aliens):
	check_fleet_edges(al_settings,aliens)
	aliens.update()

def check_fleet_edges(al_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(al_settings,aliens)
			break

def change_fleet_direction(settings,aliens):
	for alien in aliens.sprites():
		alien.y+=settings.fleet_drop_speed
		alien.rect.y=alien.y
	settings.fleet_direction*=-1

def update_screen(settings,screen,ship,bullets,aliens):
	# 每次都要填充背景色，否则会有飞机移动痕迹
    screen.fill(settings.screen_bg)
    for bullet in bullets.sprites():
    	bullet.draw_bullet()
    ship.blitme()
    # draw方法会默认调用实例的blit方法surface_blit(spr.image, spr.rect)
    aliens.draw(screen)
    # for alien in aliens.sprites():
    # 	alien.blitme()
    pygame.display.flip()
