import pygame, sys
from pygame.sprite import Sprite

class Arrow(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("img/arrow.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.bottom = self.screen_rect.bottom
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))