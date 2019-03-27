import pygame, sys

class Robin_hood():


    def __init__(self, screen, game_settings):
        self.screen = screen

        self.image = pygame.image.load("img/Archer.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_up = False

        self.make_jump = False
        self.jump_counter = 30
        self.usr_y = game_settings.height - 335


    def blitme(self):
        self.screen.blit(self.image, (self.rect.x, self.usr_y))


    def update(self):
        if self.moving_right:
            self.rect.x  += 3

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 3

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 3


    def jump(self):

        if self.jump_counter >= -30:
            self.usr_y -= self.jump_counter / 3
            self.jump_counter -= 1

        else:
            self.jump_counter = 30
            self.make_jump = False


