import pygame, sys

class Settings():


    def __init__(self):
        self.width =1600
        self.height=900
        self.bg_color=(0, 31, 40)
        #self.bg_img = "img/_12_backgrund"
        self.tile_size = 64
        #self.light_grey = (100, 100, 100)
        #self.grid_width = self.width / self.tile_size
        #self.grid_height = self.height / self.tile_size

        self.CameraX = 10
        self.CameraY = 10

        self.bullet_width = 30
        self.bullet_height = 3
        self.bullet_color = (123, 43, 12)

        screen = pygame.display.set_mode((0,0))
        self.bg = pygame.image.load("img/_12_background.png").convert()
        self.bg = pygame.transform.scale(self.bg, (1600, 900))

