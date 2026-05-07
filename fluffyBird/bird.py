import pygame
import config
import utils

from state import State
from dataclasses import dataclass


@dataclass
class Bird:

    def __init__(self):
        image = pygame.image.load("assets/images/Bird.png").convert_alpha()

        self.frame_width = image.get_width() // 2
        self.frame_height = image.get_height() // 2

        self.min_height = -self.frame_height // 1.5

        self.image = image.subsurface((0, 0, self.frame_width, self.frame_height))

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

        self.velocity_y = 0

    def update(self, state: State):
        if state.pause:
            return

        self.velocity_y += config.GRAVITY

        self.rect.y += self.velocity_y
        if self.rect.y <= self.min_height:
            self.rect.y = self.min_height

    def jump(self, state: State):
        if state.pause:
            return

        self.velocity_y += config.JUMP_STRENGHT

        if self.velocity_y < config.MIN_VELOCITY:
            self.velocity_y = config.MIN_VELOCITY
        elif self.velocity_y > config.MAX_VELOCITY:
            self.velocity_y = config.MAX_VELOCITY

    def draw(self, screen: pygame.Surface):
        utils.draw(screen, self.image, self.rect)
