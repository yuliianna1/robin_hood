class Settings():


    def __init__(self):
        self.width =1024
        self.height=768
        self.bg_color=(0, 31, 40)
        self.bg_img = "img/_12_backgrund"
        self.tile_size = 32
        self.light_grey = (100, 100, 100)
        self.grid_width = self.width / self.tile_size
        self.grid_height = self.height / self.tile_size