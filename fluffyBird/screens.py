import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, PAUSE_OVERLAY_COLOR

from state import State
from background import Background
from treeSpawner import TreeSpawner
from bird import Bird

from utils import Button


class StartScreen:

    def __init__(self):
        self.overlay = createOverlay()

        title_font = pygame.font.Font(None, 150)
        self.title_surface = title_font.render("Fluffy Bird", True, (255, 255, 255))
        self.title_rect = self.title_surface.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
        )

        self.start_btn = Button("Start")

    def play(
        self,
        screen: pygame.Surface,
        events: list[pygame.event.Event],
        state: State,
        entities: tuple[Background, TreeSpawner, Bird],
    ):
        bg = entities[0]

        bg.draw(screen)

        screen.blit(self.overlay[0], self.overlay[1])
        screen.blit(self.title_surface, self.title_rect)

        self.start_btn.draw(screen, (300, 300), hover=True)


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
        self.overlay = createOverlay()

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

        screen.blit(self.overlay[0], self.overlay[1])
        screen.blit(self.pause_surface, self.pause_rect)


def createOverlay():
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    surface.fill(PAUSE_OVERLAY_COLOR)
    rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    return surface, rect
