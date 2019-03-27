import pygame, sys
from settings import Settings
from robin_hood import Robin_hood
import game_functions as g_f

clock = pygame.time.Clock()


def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    hero = Robin_hood(screen, game_settings)
    pygame.display.set_caption("The best game in the world")
    bg = pygame.image.load("img/_12_background.png").convert()
    bg = pygame.transform.scale(bg, (1024, 768))

    while True:
        screen.blit(bg, [0, 0])
        g_f.check_events(hero)
        g_f.update_screen(screen, game_settings, hero)
        pygame.display.flip()
        clock.tick(60)

init_game()