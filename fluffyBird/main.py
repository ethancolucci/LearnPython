import pygame
import config
import utils

from state import State
from background import Background
from treeSpawner import TreeSpawner
from bird import Bird

pygame.init()

screen_size = (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Fluffy Bird")

clock = pygame.time.Clock()

state = State()

bg = Background()
treeSpawner = TreeSpawner()
bird = Bird()

pause_overlay = pygame.Surface(
    (config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA
)
pause_overlay.fill((0, 0, 0, 125))

running = True
while running:
    clock.tick(config.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                state.pause = not state.pause
            elif event.key == pygame.K_SPACE:
                bird.jump(state)

    treeSpawner.update(state)
    bird.update(state)

    screen.fill((0, 0, 0))

    bg.draw(screen, state)
    treeSpawner.draw(screen, state)
    bird.draw(screen)

    if state.pause:
        utils.draw(screen, pause_overlay, (0, 0))

    pygame.display.flip()


pygame.quit()
