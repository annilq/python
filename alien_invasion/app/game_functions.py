import sys
from time import sleep

import pygame
from alien import Alien
from bullet import Bullet


def check_events(settings, screen, stat, ship, bullets, al_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_event(ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, stat, al_button, mouse_x, mouse_y)


# 鼠标事件
def check_play_button(settings, stat, al_button, mouse_x, mouse_y):
    button_click = al_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stat.game_active:
        stat.reset_stats()
        stat.game_active = True
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)


# 键盘事件
def keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(settings, screen, ship, bullets)


# 获取一共有几排几列外星人
def get_alien_cols_rows(screen, al_settings, ship):
    alien = Alien(screen, al_settings)
    screen_width = al_settings.screen_width
    alien_width = alien.rect.width
    screen_width_space = screen_width - (2 * alien_width)
    alien_cols = int(screen_width_space / (2 * alien_width))

    ship_height = ship.rect.height
    screen_height = al_settings.screen_height
    alien_height = alien.rect.height
    screen_height_space = screen_height - (2 * alien_height) - ship_height
    alien_rows = int((screen_height_space) / (2 * alien_height))
    print(alien_cols, alien_rows)
    return (alien_cols, alien_rows)


def keyup_event(ship):
    ship.moveing_right = False
    ship.moveing_left = False


# 创建外星人群
def create_fleet(screen, al_settings, ship, aliens):
    cols, rows = get_alien_cols_rows(screen, al_settings, ship)
    for row in range(rows):
        for col in range(cols):
            create_alien(screen, al_settings, aliens, row, col)


# 创建外星人
def create_alien(screen, al_settings, aliens, row, col):
    alien = Alien(screen, al_settings)
    alien.x = alien.rect.width + 2 * alien.rect.width * col
    alien.y = alien.rect.height + 2 * alien.rect.height * row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


# 发射子弹
def fire_bullets(settings, screen, ship, bullets):
    if len(bullets) < settings.max_bullets_num:
        bullets.add(Bullet(settings, screen, ship))


# 更新子弹
def update_bullets(settings, screen,stat, ship, bullets, aliens,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for aliens in  collisions.values():
        # 每次可能击中多个外星人，需要乘以个数
        stat.score+=settings.alien_points*len(aliens)
        # 每次分数改变都要重新绘制
        sb.prep_score()
        check_high_score(stat,sb)
        
    # 外星人没了要创建新的
    if len(aliens) == 0:
        bullets.empty()
        # 设置等级
        stat.level+=1
        sb.prep_level()
        settings.increase_speed()
        create_fleet(screen, settings, ship, aliens)


def check_high_score(stat,sb):
    if stat.score>stat.high_score:
        stat.high_score=stat.score
        sb.prep_high_score()
        

# 更新外星人
def update_aliens(settings, screen, ship, aliens, bullets, stat,sb):
    check_fleet_edges(settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, ship, aliens, bullets, stat,sb)
    # 检测是否撞到底部
    check_aliens_bottom(settings, screen, ship, aliens, bullets, stat,sb)


# 飞船撞击
def ship_hit(settings, screen, ship, aliens, bullets, stat,sb):
    if stat.ship_left_limit > 0:
        stat.ship_left_limit -= 1
        sb.prep_ships()
        bullets.empty()
        aliens.empty()
        ship.center_ship()
        create_fleet(screen, settings, ship, aliens)
        sleep(0.5)
    else:
        stat.reset_stats()
        stat.game_active = False
        pygame.mouse.set_visible(True)


# 检测是否撞到边缘
def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


# 改变外星人移动方向
def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.y += settings.fleet_drop_speed
        alien.rect.y = alien.y
    settings.fleet_direction *= -1


# 检测是否装到了底部
def check_aliens_bottom(settings, screen, ship, aliens, bullets, stat,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, screen, ship, aliens, bullets, stat,sb)
            break
    pass


# 更新试图
def update_screen(settings, screen, ship, bullets, aliens, stat, al_button,sb):
    # 每次都要填充背景色，否则会有飞机移动痕迹
    screen.fill(settings.screen_bg)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # draw方法会默认调用实例的blit方法surface_blit(spr.image, spr.rect)
    aliens.draw(screen)
    # for alien in aliens.sprites():
    # 	alien.blitme()
    sb.show_score()
    if not stat.game_active:
        al_button.draw_button()
    # 这句一定要在最后，不然他下面的操作都无效
    pygame.display.flip()
