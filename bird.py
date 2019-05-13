import pygame, sys
from pygame.sprite import Sprite

class Bird(Sprite):
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("img/bird/1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.counter = 0
        self.bird_img = ["img/bird/1.png","img/bird/2.png","img/bird/3.png","img/bird/4.png","img/bird/5.png","img/bird/6.png","img/bird/7.png","img/bird/8.png","img/bird/9.png","img/bird/10.png","img/bird/11.png","img/bird/12.png","img/bird/13.png"]

        self.img_counter = 0
        self.rect_counter = 0
        self.n = 1
        self.attack = False
        self.fly = False
        self.rect.y = 10

    def blitme(self):
        if self.rect.x == 500:
            self.attack = True
        self.rect.x -= 1
        if self.attack == False:
            self.rect.y += self.n
            self.rect_counter += 1
            if self.rect_counter > 135:
                self.rect_counter = 0
                self.n *= -1
        else:
            self.rect.y += 3
            if self.rect.y >= 500:
                self.attack = False

        self.image = pygame.image.load(self.bird_img[self.counter//15]).convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)
        self.counter = self.counter+1
        if self.counter == len(self.bird_img) * 6:
            self.counter = 0
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
