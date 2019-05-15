import pygame, sys

import boss
from bullet import Bullet
from enemy import Enemy
from  tile import Tile
from boss import Boss




def check_events(hero, game_settings, bullets, screen):

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                hero.moving_right = True
            if i.key == pygame.K_LEFT:
                hero.moving_left = True
            if i.key == pygame.K_DOWN:
                hero.moving_bottom = True
            if i.key == pygame.K_UP:
                hero.rect.y -= 2
                hero.make_jump = True
            if len(bullets) != 5:
                if i.key == pygame.K_SPACE:
                    hero.shoot = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                hero.moving_right = False
            if i.key == pygame.K_LEFT:
                hero.moving_left = False
            if i.key == pygame.K_DOWN:
                hero.moving_bottom = False


def update_screen(screen, game_settings, hero, bullets, enemy1, tiles, trap, coin,cave, lian, boss1, hp, hart, arow, chest, num, num1, aroow, bird, all_tiles):
    if hero.shoot_counter > (len(hero.shoot_img) - 1) * 8:
        new_bullet = Bullet(game_settings, screen, hero)
        bullets.add(new_bullet)


    for group_tile in all_tiles:
        for tile in group_tile:
            screen.blit(tile.image, tile.rect)
            if hero.moving_right and hero.colided == False:
                tile.rect.x -= 6
            elif hero.moving_left and hero.colided == False:
                tile.rect.x += 6

    for nums in num:
        screen.blit(nums.image, nums.rect)
    for num1s in num1:
        screen.blit(num1s.image, num1s.rect)
    for harts in hart:
        screen.blit(harts.image, harts.rect)
    for arows in arow:
        screen.blit(arows.image, arows.rect)
    for chests in chest:
        screen.blit(chests.image, chests.rect)

    if hero.make_jump:
        hero.jump(game_settings)
    if pygame.sprite.spritecollideany(hero,trap):
        hero.rect.x = 0
    if pygame.sprite.spritecollideany(hero, cave):
        tiles.empty()
        trap.empty()
        cave.empty()
        hero.rect.x = 0
        lian.empty()
        coin.empty()
        aroow.empty()
        game_settings.bg = pygame.image.load("img/a-tunnel-vector.png").convert()
        game_settings.bg = pygame.transform.scale(game_settings.bg, (1600, 900))
        #if game_settings.bg.rect.x < 0:
        #    game_settings.bg = pygame.transform.flip(game_settings.bg, True, False)
        level2(tiles, trap, cave, lian, coin, hart)
        # screen.blit(bg, (bg.get_rect().width, 0))

    if pygame.sprite.spritecollideany(hero,coin):
        coin_el = pygame.sprite.spritecollideany(hero, coin)

        coin.remove(coin_el)

    if pygame.sprite.spritecollideany(hero,aroow):
        aroow_el = pygame.sprite.spritecollideany(hero, aroow)

        aroow.remove(aroow_el)

        for num1s in num1:
            num1s.counter += 1
            if num1s.counter == 10:
                num1s.counter = 0
            num1s.image = pygame.image.load("img/tile/" + str(num1s.counter) + ".png").convert_alpha()

    if pygame.sprite.spritecollideany(hero,tiles):
        if hero.make_jump:
            hero.make_jump = False
            hero.jump_counter = 30

    if pygame.sprite.spritecollideany(bird, bullets):
        bird.alive = False

    if bird.alive:
        bird.blitme()


    if boss1.lep:
        if hero.moving_right and hero.colided == False:
            boss1.x -= 6
        elif hero.moving_left and hero.colided == False:
            boss1.x += 6
        boss1.draw_boss()
        boss1.update()

    if enemy1.lep:
        if hero.moving_right and hero.colided == False:
            enemy1.x -= 6
        elif hero.moving_left and hero.colided == False:
            enemy1.x += 6
        enemy1.draw_enemy()
        enemy1.update()
    hero.update()
    for bullet in bullets:
        bullet.draw_bullet()
        if bullet.rect.y > 800:
             bullets.remove(bullet)
        if bullet.rect.x < hero.rect.x + 350:
            # bullet.trans()
            bullet.rect.x += 6
            bullet.rect.y -= 0.5
        elif bullet.rect.x != hero.rect.x + 500 and bullet.rotate_arrow:
            bullet.image = pygame.transform.rotate(bullet.image, -15)
            bullet.rotate_arrow = False
        elif bullet.rect.x != hero.rect.x + 500:
            bullet.rect.x += 6
            bullet.rect.y += 1
        if bullet.rect.x > enemy1.x and bullet.rect.y < enemy1.y + 200 and bullet.rect.y > enemy1.y:
            enemy1.lep = False
            enemy1.x = 0
            enemy1.y = 0
            bullets.remove(bullet)
        elif bullet.rect.x > boss1.x and bullet.rect.y < boss1.y + 200 and bullet.rect.y > boss1.y:
            hp -= 1
        elif hp == 0:
            boss1.lep = False
            boss1.x = 0
            boss1.y = 0



def level2(tiles, trap, cave, lian, coin, hart):
    level2 = ["hhh b",
              "C   b",
              "A   b",
              "    b         c         ",
              "    b        bbb         ",
              "    b                      b     bbb                                          bb",
              "    b             b       bbb                                               bbbb",
              "    b            bb                                                    b       bb",
              "    b     bbbbb                 b                         bb           bb     bbb",
              "    bbbb                      bbbbb              bb     bb            b         bb",
              "                                             bb     bb       bb     b        bbbbbbb",
              "         Z               Z  Z  tttttZt   Z                       bb     Z    bb     Z",               #bose location
              "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbttttttttttttttttttttZtbbbbbbbbbbbbbbbbbbbbWbbWbWbWWbbbbbbbbbbbbbbbb",
              "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",

              ]
    x = y = 0
    for row in level2:
        for col in row:
            if col == "Z":
                Tile(x, y, "stone06.png", tiles)
            elif col == "a":
                Tile(x, y, "barrel.png", tiles)
            elif col == "b":
                Tile(x, y, "rocky03.png", tiles)
            elif col == "g":
                Tile(x, y, "grass.png", tiles)
            elif col == "t":
                Tile(x, y, "trap.png", trap)
            elif col == "c":
                Tile(x, y, "coin.png", coin)
            elif col == "i":
                Tile(x, y, "island.png", tiles)
            elif col == "E":
                Tile(x, y, "cave.png", cave)
            elif col == "W":
                Tile(x, y, "water.png", lian)
            elif col == "h":
                Tile(x, y, "hart.png", hart)

            x += 64
        y += 64
        x = 0
