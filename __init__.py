import pygame, sys
from settings import Settings
from ship import Ship

def init_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    bg_color = (0, 31, 40)
    pygame.display.set_caption("The best game in the world")

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit() #full complete
        pygame.display.flip()
        screen.fill(bg_color)

init_game()
