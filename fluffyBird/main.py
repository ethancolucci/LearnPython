import pygame
import config
import background

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Fluffy Bird")

clock = pygame.time.Clock()

bg = background.Background()
bg.init()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    bg.draw(screen)

    pygame.display.flip()


pygame.quit()
