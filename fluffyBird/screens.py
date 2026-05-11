import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, PAUSE_OVERLAY_COLOR

from state import State
from background import Background
from treeSpawner import TreeSpawner
from bird import Bird


class GamingScreen:

    def play(
        self,
        screen: pygame.Surface,
        events: list[pygame.event.Event],
        state: State,
        entities: tuple[Background, TreeSpawner, Bird],
    ):
        bg, treeSpawner, bird = entities

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump(state)

        bg.update(state)
        treeSpawner.update(state)
        bird.update(state)

        screen.fill((255, 0, 0))

        bg.draw(screen)
        treeSpawner.draw(screen)
        bird.draw(screen)


class PauseScreen:

    def __init__(self):
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill(PAUSE_OVERLAY_COLOR)
        self.overlay_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        pause_font = pygame.font.Font(None, 48)
        self.pause_surface = pause_font.render("PAUSE", True, (255, 255, 255))
        self.pause_rect = self.pause_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )

    def play(
        self,
        screen: pygame.Surface,
        events: list[pygame.event.Event],
        state: State,
        entities: tuple[Background, TreeSpawner, Bird],
    ):
        bg, treeSpawner, bird = entities

        bg.draw(screen)
        treeSpawner.draw(screen)
        bird.draw(screen)

        screen.blit(self.overlay, self.overlay_rect)
        screen.blit(self.pause_surface, self.pause_rect)
