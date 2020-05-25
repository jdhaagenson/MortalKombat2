#! python 3.6

from itertools import cycle

import pygame as pg


class Character:
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet
        self.images = [[],[],[]]
        self.image = pg.image.load(self.images[0][0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.position = self.rect.x 
        self.facing = 'right'
    def walk(self):
        self.image = cycle(self.images[0][0])
        if self.facing == 'left':
            self.image 
