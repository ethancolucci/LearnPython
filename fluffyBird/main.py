import pygame
import config
from background import Background
from bird import Bird
from state import State

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Fluffy Bird")

clock = pygame.time.Clock()

bg = Background()
bird = Bird()
state = State()

pause_overlay = pygame.Surface(
    (config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA
)
pause_overlay.fill((0, 0, 0, 125))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                state.pause = not state.pause
            elif event.key == pygame.K_SPACE:
                bird.jump(state)

    bird.update(state)

    screen.fill((0, 0, 0))

    bg.draw(screen, state)
    bird.draw(screen)

    if state.pause:
        screen.blit(pause_overlay, (0, 0))

    pygame.display.flip()


pygame.quit()
