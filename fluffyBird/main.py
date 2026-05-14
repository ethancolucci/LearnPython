import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

from background import Background
from treeSpawner import TreeSpawner
from bird import Bird

from state import State

from screens import StartScreen, GamingScreen, PauseScreen

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fluffy Bird")

state = State()

bg = Background()
treeSpawner = TreeSpawner()
bird = Bird()

entities = (bg, treeSpawner, bird)

start_screen = StartScreen()
gaming_screen = GamingScreen()
pause_screen = PauseScreen()

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                state.pause = not state.pause

    # if state.pause:
    #     pause_screen.play(screen, events, state, entities)
    # else:
    #     gaming_screen.play(screen, events, state, entities)

    start_screen.play(screen, events, state, entities)

    pygame.display.flip()


pygame.quit()
