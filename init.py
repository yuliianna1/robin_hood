import pygame, sys, os
from settings import Settings
from robin_hood import Robin_hood
from bird import Bird
import game_functions as g_f
from pygame.sprite import Group
from enemy import Enemy
from tile import Tile
from arrow import Arrow


clock = pygame.time.Clock()


def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    bullets = Group()
    arrows = Group()
    heroes = Group()
    pygame.display.set_caption("The best game in the world")
    # bg = pygame.image.load(game_settings.bg).convert()
    # bg = pygame.transform.scale(bg, (1600, 900))
    enemy1 = Enemy(screen, game_settings)
    bird = Bird(screen, game_settings)
    arrow1 = Arrow(screen, 900, 700)
    arrow2 = Arrow(screen, 1000, 700)
    arrows.add(arrow1)
    arrows.add(arrow2)
    trap = Group()
    tiles = Group()
    coin = Group()
    cave = Group()
    lian = Group()
    level1 = ["",
              "",
              "",
              "                                                                                                            ",
              "                                                                                                            ",
              "                                                                                                            ",
              "                                                        cc                                                  ",
              "                                                        iiL                                                 ",
              "                                          i                                                                 ",
              "              c           cZ           i               c                                                   ",
              "            bbb           ZZ         i      c i    i   i       i        E                                   ",
              "  c  bbtbbbtbbbbtc   Zt  ZZZZtZt   ZttttttttZttttZ        Z  tt     c   c                                  ",
              "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
              "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
              ]
    x = y = 0
    hero = Robin_hood(screen, game_settings, tiles)
    for row in level1:
        for col in row:
            if col == "Z":
                Tile(x, y, "box.png", tiles)
            elif col == "a":
                Tile(x, y, "barrel.png", tiles)
            elif col == "b":
                Tile(x, y, "block.png", tiles)
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
            elif col == "L":
                Tile(x, y, "lian.png", lian)
            x += 64
        y += 64
        x = 0

    game_settings.bg = game_settings.bg.convert()

    while True:
        g_f.check_events(screen, game_settings, hero, bullets, heroes)
        g_f.update_screen(screen, game_settings, hero, bullets, heroes, enemy1,tiles,trap,coin,cave,lian, bird, arrows)
        #screen.blit(bg, (0 - game_settings.CameraX, 0 - game_settings.CameraY))
        screen.blit(hero.image, (hero.rect.x, hero.rect.y-30))
        pygame.display.flip()
        rel_x = x % game_settings.bg.get_rect().width
        screen.blit(game_settings.bg, (rel_x - game_settings.bg.get_rect().width, 0))
        if rel_x < game_settings.width:
            screen.blit(game_settings.bg, (rel_x, 0))
        x = 0 - hero.rect.x
        clock.tick(60)
        print (hero.rect.x)

init_game()