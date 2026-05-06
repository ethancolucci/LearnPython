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
        self.image = pygame.image.load(
            "fluffyBird/assets/images/Logs.png"
        ).convert_alpha()

        self.frame_width = self.image.get_width() // 6
        self.frame_height = self.image.get_height()

        self.trees = []
        self.last_spawn_time = 0

    def _createTree(self, frame: int):
        if frame < 0 or frame > 3:
            raise Exception("Frame must be [0, 3]")

        img = self.image.subsurface(
            (frame * self.frame_width, 0, self.frame_width, self.frame_height)
        )
        rect = img.get_rect()

        return img, rect

    def _spawnTrees(self):
        image, rect = self._createTree(0)
        rect.left = config.SCREEN_WIDTH + 50
        rect.top = -50

        self.trees.append((image, rect))
        # choose to spawn 1 or 2 trees ?
        # create tree-s - self._createTree()
        # choose tree-s size-s (small, average or high) - rect.y
        # place tree-s (rect.x and rect.y)
        # push image and rect into self.images and self.rects

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

        # do we have to spawn a new tree? (or two)
        r = randint(0, config.TREE_SPAWN_PROB)
        if r == 0:
            now = time()
            if now - self.last_spawn_time > 1:
                self._spawnTrees()
                self.last_spawn_time = now

        # do we have to remove old trees?
        self._removeOldTrees()

        # move actual trees on the screen (as bg clouds/grass)
        self._moveTrees()

        print(len(self.trees))

    def draw(self, screen: pygame.Surface, state: State):
        for image, rect in self.trees:
            utils.draw(screen, image, rect)
