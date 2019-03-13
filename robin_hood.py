import pygame, sys

class Robin_hood():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("img/aliens.png")
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_bottom = False
        self.moving_up = False
        self.jump = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x = self.rect.x + 1

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 1

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

        if self.moving_up and self.rect.top > self.screen_rect.top:
            # self.moving_up += 50
            # if self.moving_up <= 50:
            #     print("YES")
            #     self.moving_up = False

            if self.jump == True:
                self.rect.y -= 1
            else:
                self.rect.y += 1
            if self.rect.y < 400:
                self.jump = False
            if self.rect.y > 519 and self.jump == False:
                self.moving_up = False

                # if self.rect.y < 0:
                #      self.rect.y == False
