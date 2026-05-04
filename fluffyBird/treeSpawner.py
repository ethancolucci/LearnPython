import pygame
import time
import config

from state import State
from dataclasses import dataclass


@dataclass
class TreeSpawner:

    def __init__(self):
        self.image = pygame.image.load(
            "fluffyBird/assets/images/Logs.png"
        ).convert_alpha()

        self.frame_width = self.image.get_width() // 6
        self.frame_height = self.image.get_height()

        self.images = []
        self.rects = []

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
        # choose to spawn 1 or 2 trees ?
        # create tree-s - self._createTree()
        # choose tree-s size-s (small, average or high) - rect.y
        # place tree-s (rect.x and rect.y)
        # push image and rect into self.images and self.rects
        pass

    def _removeOldTrees(self):
        # loop into actual trees (self.rects)
        # si rect.x <= (-100px for example) =>
        #     remove image and rect from self.images and self.rects
        #     destroy image and rect
        pass

    def _moveTrees(self):
        # loop into actual trees (self.rects)
        # move each tree on the left
        pass

    def update(self, state: State):
        if state.pause:
            return

        # do we have to spawn a new tree? (or two)
        now = int(time.time())
        if now - self.last_spawn_time >= config.TREE_SPAWN_TIMEOUT:
            self.last_spawn_time = now
            self._spawnTrees()

        # do we have to remove old trees? (x < -100px)
        self._removeOldTrees()

        # move actual trees on the screen (as bg clouds/grass)
        self._moveTrees()

    def draw(self, screen: pygame.Surface, state: State):
        pass
