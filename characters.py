from controls import Controller
from game_map import *
from itertools import cycle
import pygame as pg

pg.init()

kitana_img =dict(
    stand = ['kitana/SNES_MK2_kitana_stand1.png', 'kitana/SNES_MK2_kitana_stand2.png',
             'kitana/SNES_MK2_kitana_stand3.png', 'kitana/SNES_MK2_kitana_stand4.png',
             'kitana/SNES_MK2_kitana_stand5.png']
          )
mileena_img = ['./mileena/SNES_MK2_mileena.png'],
liukang_img = ['./liukang/SNES_MK2_liukang.png'],
kintaro_img = ['./kintaro/SNES_MK2_kintaro.png']
# scorpion_img = [],
# subzero_img = [],
# reptile_img = [],
# jade_img = [],
# jax_img = []


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

class Character(pg.sprite.Sprite):
    """
    possible_status:
    default (standing)
    walking
    up-punch
    downpunch
    forwardpunch
    upkick
    downkick
    forwardkick
    special
    dizzy
    hit
    finished
    winner
    """
    def __init__(self, images_dict:dict):
        super().__init__(self)
        self.action = 'stand'
        self.images = images_dict
        self.image = self.images[self.action]
        self.rect = self.image.get_rect()
        self.x_pos = self.rect.x
        self.index = 0
        # self.controller = Controller()
        self.movement = (0, 0)
        self.collision_types = {
            'top': False,
            'bottom': False,
            'right': False,
            'left': False
        }
        self.health = 100
        self.cycler = cycle(self.images[self.action])

    @staticmethod        
    def load_image(image):
        return pg.image.load(image).convert_alpha()

    # def move(self, rect, movement, tiles):
    #     rect.x += movement[0]
    #     hit_list = collision_test(self.rect, )

    def update(self):
        self.rect
        self.index += 1
    def next_image(self):
        self.image = self.cycler.
    def walk(self, forward=True):
        if forward:
            self.rect.x += 10
            self.image = self.next_image()



