import pygame
import config
import utils

from state import State
from dataclasses import dataclass


@dataclass
class Background:

    def __init__(self):
        self.clouds = pygame.image.load("assets/images/Clouds.png").convert_alpha()
        self.grass = pygame.image.load("assets/images/Grass.png").convert_alpha()

        self.sky_rect = (0, 0, config.SCREEN_WIDTH, self.clouds.get_height())
        self.sea_rect = (
            0,
            self.sky_rect[3],
            config.SCREEN_WIDTH,
            config.SCREEN_HEIGHT - self.sky_rect[3],
        )

        self.clouds_arr = []
        self.grass_arr = []

        self._initSprites(self.clouds, self.clouds_arr, 0)
        self._initSprites(
            self.grass, self.grass_arr, config.SCREEN_HEIGHT - self.grass.get_height()
        )

    def _initSprites(
        self, image: pygame.Surface, images_arr: list[pygame.Rect], y: int
    ):
        for i in range(0, config.BG_REPEAT):
            rect = image.get_rect()
            rect.topleft = (i * rect.width, y)
            images_arr.append(rect)

    def _drawSprites(
        self,
        screen: pygame.Surface,
        state: State,
        image: pygame.Surface,
        images_arr: list[pygame.Rect],
    ):
        if not state.pause:
            if images_arr[0].right <= 0:
                first_rect = images_arr.pop(0)

                new_rect = image.get_rect()
                new_rect.topleft = (config.SCREEN_WIDTH, first_rect.y)

                images_arr.append(new_rect)

        for rect in images_arr:
            if not state.pause:
                rect.x -= config.BG_SPEED
            utils.draw(screen, image, rect)

    def draw(self, screen: pygame.Surface, state: State):

        pygame.draw.rect(screen, (30, 140, 184), self.sky_rect)
        pygame.draw.rect(screen, (4, 112, 236), self.sea_rect)

        self._drawSprites(screen, state, self.clouds, self.clouds_arr)
        self._drawSprites(screen, state, self.grass, self.grass_arr)
