import pygame, sys
from settings import Settings
from robin_hood import Robin_hood
import game_functions as g_f



def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    hero = Robin_hood(screen)
    bg_color = (0, 31, 40)
    pygame.display.set_caption("The best game in the world")

    while True:
        g_f.check_events(hero)
        g_f.update_screen(screen, game_settings, hero)

init_game()
