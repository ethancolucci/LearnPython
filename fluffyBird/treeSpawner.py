import pygame
import config
import utils

from state import State
from time import time
from random import randint
from dataclasses import dataclass


@dataclass
class TreeSpawner:
    trees: list[tuple[pygame.Surface, pygame.Rect]]

    def __init__(self):
        self.image = pygame.image.load(config.TREE_IMAGE_PATH).convert_alpha()

        self.frame_width = self.image.get_width() // 4
        self.frame_height = self.image.get_height()

        self.trees = []
        self.last_spawn_time = 0

    def _createTree(self, frame: int):
        if frame < 0 or frame > 3:
            raise Exception("Frame must be [0, 3]")

        img = self.image.subsurface(
            (
                frame * self.frame_width,
                0,
                self.frame_width,
                self.frame_height,
            )
        )
        rect = img.get_rect()

        return img, rect

    def _get_random_tree_y(self) -> int:
        height = randint(0, 3)
        if height == 0:
            return 200
        elif height == 1:
            return 120
        else:
            return 60

    def _spawnTrees(self):

        start_x = config.SCREEN_WIDTH + 50

        # upper tree
        r1 = randint(0, 4)
        if r1 != 3:
            image, rect = self._createTree(randint(0, 3))
            rect.left = start_x
            rect.top = self._get_random_tree_y() * -1
            self.trees.append((image, rect))

        # bottom tree
        r2 = randint(0, 4)
        if r2 != 3:
            image, rect = self._createTree(randint(0, 3))
            rect.left = start_x
            rect.bottom = config.SCREEN_HEIGHT + self._get_random_tree_y()
            self.trees.append((image, rect))

    def _removeOldTrees(self):
        new_trees: list[tuple[pygame.Surface, pygame.Rect]] = []
        for image, rect in self.trees:
            if rect.right > -100:
                new_trees.append((image, rect))
        self.trees = new_trees

    def _moveTrees(self):
        for _, rect in self.trees:
            rect.x -= config.TREE_VELOCITY

    def update(self, state: State):
        if state.pause:
            return

        # do we have to spawn a new trees?
        now = time()
        last_spawn_time_diff = now - self.last_spawn_time
        if last_spawn_time_diff >= 1.5:
            self._spawnTrees()
            self.last_spawn_time = now
        else:
            r = randint(0, config.TREE_SPAWN_PROB)
            if r == 0 and last_spawn_time_diff >= 1:
                self._spawnTrees()
                self.last_spawn_time = now

        # do we have to remove old trees?
        self._removeOldTrees()

        # move actual trees on the screen (as bg clouds/grass)
        self._moveTrees()

    def draw(self, screen: pygame.Surface, state: State):
        for image, rect in self.trees:
            utils.draw(screen, image, rect)

            # debug draw collision rect
            if config.DEBUG:
                collision_rect = utils.createCollisionRect(
                    rect, config.TREE_COLLISION_PADDING
                )
                pygame.draw.rect(screen, (255, 0, 0), collision_rect, 2)
