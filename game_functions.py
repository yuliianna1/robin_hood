import pygame, sys
from bullet import Bullet
from enemy import Enemy
from  tile import Tile


def check_events(screen, game_settings, hero, bullets, heroes):

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
                    new_bullet = Bullet(screen, game_settings, hero, bullets, heroes)
                    bullets.add(new_bullet)
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                hero.moving_right = False
            if i.key == pygame.K_LEFT:
                hero.moving_left = False
            if i.key == pygame.K_DOWN:
                hero.moving_bottom = False


def update_screen(screen, game_settings, hero, bullets, heroes, enemy1,tiles,trap,coin,cave,lian, bird, arrows):
    for wall in tiles:
        screen.blit(wall.image, wall.rect)
        if hero.moving_right:
            wall.rect.x -= 6
        elif hero.moving_left:
            wall.rect.x += 6
    for traps in trap:
        screen.blit(traps.image, traps.rect)
        if hero.moving_right:
            traps.rect.x -= 6
        elif hero.moving_left:
            traps.rect.x += 6
    for caves in cave:
        screen.blit(caves.image,caves.rect)
        if hero.moving_right:
            caves.rect.x -= 6
        elif hero.moving_left:
            caves.rect.x += 6
    for lians in lian:
        screen.blit(lians.image,lians.rect)
        if hero.moving_right:
            lians.rect.x -= 6
        elif hero.moving_left:
            lians.rect.x += 6
    for coins in coin:
        screen.blit(coins.image, coins.rect)
        if hero.moving_right:
            coins.rect.x -= 6
        elif hero.moving_left:
            coins.rect.x += 6
    if pygame.sprite.groupcollide(heroes, arrows, False, True):
        hero.arrows_counter += 1
    for arrow in arrows:
        arrow.blitme()

    #check collides with bird
    if pygame.sprite.collide_rect(hero, bird):
        hero.rect.x = 0

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
        game_settings.bg = pygame.image.load("img/a-tunnel-vector.png").convert()
        game_settings.bg = pygame.transform.scale(game_settings.bg, (1600, 900))
        #if game_settings.bg.rect.x < 0:
        #    game_settings.bg = pygame.transform.flip(game_settings.bg, True, False)
        level2(tiles, trap, cave, lian, coin)
        # screen.blit(bg, (bg.get_rect().width, 0))

    if pygame.sprite.spritecollideany(hero,coin):
        coin_el = pygame.sprite.spritecollideany(hero, coin)

        coin.remove(coin_el)

    if pygame.sprite.spritecollideany(hero,tiles):
        print(hero.rect.y)
        if hero.make_jump:
            hero.make_jump = False
            hero.jump_counter = 30

    if enemy1.lep:
        if hero.moving_right:
            enemy1.x -= 3
        elif hero.moving_left:
            enemy1.x += 3
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
    bird.blitme()

def level2(tiles, trap, cave, lian, coin):
    level2 = ["    b",
              "    b",
              "    b",
              "    b         c         ",
              "    b        bbb         ",
              "    b                      b     bbb                                          bb",
              "    b             b       bbb                                               bbbb",
              "    b            bb                                                    b       bb",
              "    b     bbbbb                 b                         bb           bb     bbb",
              "    bbbb                      bbbbb              bb     bb            b         bb",
              "                                             bb     bb       bb     b        bbbbbbb",
              "         Z              Z  Z  tttttZt   Z                       bb     Z    bb     Z",               #bose location
              "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbttttttttttttttttttttZtbbbbbbbbbbbbbbbbbbbbWbbWbWbWWWbWbbWWbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
              "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",

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
            x += 64
        y += 64
        x = 0
