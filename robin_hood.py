import pygame, sys
from pygame.sprite import Sprite
from bullet import Bullet

class Robin_hood():


    def __init__(self, screen, game_settings, tiles):
        self.screen = screen
        self.g_s = game_settings

        self.image = pygame.image.load("img/idle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 120))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.counter = 0
        self.left_img = ["img/run/run1.png", "img/run/run2.png", "img/run/run3.png", "img/run/run4.png",
                         "img/run/run5.png", "img/run/run6.png"]
        self.jump_up_img = ["img/jump_up/jump_up1.png", "img/jump_up/jump_up2.png", "img/jump_up/jump_up3.png",
                            "img/jump_up/down1.png", "img/jump_up/down2.png", "img/jump_up/down3.png",
                            "img/jump_up/down4.png"]
        self.shoot_img = ["img/shoot/shoot11.png", "img/shoot/shoot22.png", "img/shoot/shoot33.png",
                          "img/shoot/shoot44.png",
                          "img/shoot/shoot55.png", "img/shoot/shoot66.png"]

        self.img_counter = 0

        self.rect.x = 0

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_up = False
        self.shoot = False
        self.shoot_counter = 0

        self.make_jump = False
        self.jump_counter = 30
        self.rect.y = game_settings.height - 250
        self.tiles = tiles
        self.colided = False
        self.jump_y = 0



    def blitme(self, bg):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):
        self.image = pygame.image.load("img/idle.png").convert_alpha()
        self.colided = False
        self.rect.y += 1
        if pygame.sprite.spritecollideany(self, self.tiles):
            self.jump_y = 30
            self.rect.y -= 1
        else:
            if not self.make_jump:
                self.rect.y += self.jump_y//3
                self.jump_y += 1
        if self.moving_right:
            if self.rect.right > self.screen_rect.right:
                self.rect.x = 0
            self.rect.x  += 2
            if self.img_counter > (len(self.left_img) - 1) * 15:
                self.img_counter = 0
            self.image = pygame.image.load(self.left_img[self.img_counter // 15]).convert_alpha()
            self.img_counter += 1
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 3
            if self.img_counter > (len(self.left_img) - 1) * 15:
                self.img_counter = 0
            self.image = pygame.image.load(self.left_img[self.img_counter // 15]).convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
            self.img_counter += 1

        if (self.moving_left or self.moving_right):
            collided_objects = pygame.sprite.spritecollide(self, self.tiles, False)
            for object in collided_objects:
                self.colided = True
                if self.moving_right:
                    self.rect.right = object.rect.left
                elif self.moving_left:
                    self.rect.left = object.rect.right
        else:
            if not self.colided:
                collided_objects = pygame.sprite.spritecollide(self, self.tiles, False)
                for object in collided_objects:
                    if self.rect.top < object.rect.top:
                        self.rect.bottom = object.rect.top

        if self.shoot:
            if self.shoot_counter > (len(self.shoot_img) - 1) * 8:
                self.shoot_counter = 0
                self.shoot = False
            self.image = pygame.image.load(self.shoot_img[self.shoot_counter//8]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.shoot_counter += 1

            #self.g_s.CameraX -= 1

        #if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            #self.rect.y += 3
            #self.g_s.CameraX += 6

    def jump(self, game_settings):

        if self.jump_counter >= -30:
            self.rect.y -= self.jump_counter / 3
            self.jump_counter -= 1

        else:
            self.jump_counter = 30
            self.make_jump = False
            self.rect.y += self.jump_counter


