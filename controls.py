import pygame as pg
from pygame.locals import *


class Controller:
    def __init__(self):
        self.wait_time = 200
        self.input = ''
        self.button.up = False
        self.button.down = False
        self.button.forward = False
        self.button.backward = False
        self.button.high_punch = False
        self.button.block = False
        self.button.low_punch = False
        self.button.high_kick = False
        self.button.low_kick = False
        self.facing = 'right'
        self.vertical_momentum = 0
        self.air_timer = 0


