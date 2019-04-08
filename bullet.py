import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_settings, screen, hero):
        super().__init__()

        self.screen = screen
        self.settings = game_settings

        self.rect = pygame.image.load("img/arrow.png")
        self.rect = pygame.transform.scale(self.rect, (40, 20))
        self.rect = pygame.transform.rotate(self.rect, 10)
            #pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.x = hero.rect.x + 100
        self.y = hero.rect.y + 100

    def update(self):
        self.x += 6

    def draw_bullet(self):
        self.screen.blit(self.rect, (self.x, self.y))
            #draw.rect(self.screen, self.settings.bullet_color, self.rect)
    #if x > self.screen_rect.right:
     #   def __del__(self):
      #      self.draw_bullet()
