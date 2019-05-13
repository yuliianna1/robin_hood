import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,screen, game_settings):
        super().__init__()

        self.screen = screen
        self.g_s = game_settings
        self.image = pygame.image.load("img/_WALK_000.png").convert_alpha()
        self.x = 1000
        self.y = game_settings.height - 330
        self.counter = 0
        self.counterbin = 1
        self.lep = True

        self.moving_img = ['img/1_KNIGHT/_RUN/_RUN_000.png', 'img/1_KNIGHT/_RUN/_RUN_001.png',
                       'img/1_KNIGHT/_RUN/_RUN_002.png', 'img/1_KNIGHT/_RUN/_RUN_003.png',
                       'img/1_KNIGHT/_RUN/_RUN_004.png', 'img/1_KNIGHT/_RUN/_RUN_005.png',
                       'img/1_KNIGHT/_RUN/_RUN_006.png']

        self.img_counter = 0
        self.last_move = 0

    def update(self):
        if self.img_counter > (len(self.moving_img) - 1) * 20:
            self.img_counter = 0
        self.img_counter += 1
        if self.counterbin == 1:
            if self.last_move != self.img_counter // 20:
                self.last_move = self.img_counter // 20
                self.image = pygame.image.load(self.moving_img[self.img_counter // 20]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (225, 200))
            if self.counter < 200:
                self.x += 2
                self.counter += 1
            elif self.counter == 200:
                self.counterbin = 2
                self.counter -= 1
        elif self.counterbin == 2:
            if self.last_move != self.img_counter // 20:
                self.last_move = self.img_counter // 20
                self.image = pygame.image.load(self.moving_img[self.img_counter // 20]).convert_alpha()
                self.image = pygame.transform.scale(self.image, (225, 200))
            if self.counter > 0:
                self.x -= 2
                self.counter -= 1
            elif self.counter == 0:
                self.counter += 1
                self.image = pygame.transform.flip(self.image, True, False)
                self.counterbin = 1
    def draw_enemy(self):
        self.screen.blit(self.image, (self.x, self.y))



