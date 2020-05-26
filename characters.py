#! python 3.6

from itertools import cycle

import pygame as pg
pg.init()

spritesheets = {
    'blood': "SNES_MK2_blood.png",
    'jade': "SNES_MK2_jade.png",
    'jax': "SNES_MK2_jax.png",
    'kintaro': "SNES_MK2_kintaro.png",
    'kitana': "SNES_MK2_kitana.png",
    'kunglao': "SNES_MK2_kunglao.png",
    'liukang': "SNES_MK2_liuKang.png",
    'mileena': "SNES_MK2_mileena.png",
    'reptile': "SNES_MK2_reptile.png",
    'scorpion': "SNES_MK2_scorp.png",
    'shang': "SNES_MK2_shang.png",
    'subzero': "SNES_MK2_subz.png"
}


class Character:
    def __init__(self, spritesheet):
        self.spritesheet = spritesheet
        self.images = [[],[],[]]
        self.image = load_image(self.images[0][0])
        self.rect = self.image.get_rect()
        self.position = self.rect.x 
        self.facing = 'right'
    def walk(self):
        self.image = cycle(self.images[0][0])
        if self.facing == 'left':
            self.image 
    @staticmethod        
    def load_image(image):
        return pg.image.load(image).convert_alpha()
    