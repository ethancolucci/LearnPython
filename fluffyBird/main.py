import pygame

pygame.init()

NB_GRASS_REPEAT = 5
NB_CLOUDS_REPEAT = 6


WIDTH = 256 * NB_GRASS_REPEAT
HEIGHT = 800

CLOUDS_SPEED = 0.7


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fluffy Bird")

clock = pygame.time.Clock()

clouds = pygame.image.load("fluffyBird/assets/images/Clouds.png").convert_alpha()
grass = pygame.image.load("fluffyBird/assets/images/Grass.png").convert_alpha()

sky_rect = (0, 0, WIDTH, clouds.get_height())
sea_rect = (0, sky_rect[3], WIDTH, HEIGHT - sky_rect[3])

clouds_arr = []


def createClouds():
    for i in range(0, NB_CLOUDS_REPEAT):
        clouds_rect = clouds.get_rect()
        clouds_rect.topleft = (i * clouds_rect.width, 0)
        clouds_arr.append(clouds_rect)


def drawClouds():
    if clouds_arr[0].right <= 0:
        clouds_arr.pop(0)

        new_cloud_rect = clouds.get_rect()
        new_cloud_rect.topleft = (WIDTH, 0)

        clouds_arr.append(new_cloud_rect)

    for clouds_rect in clouds_arr:
        clouds_rect.x -= CLOUDS_SPEED
        screen.blit(clouds, clouds_rect)


def drawGrass():
    for i in range(0, NB_GRASS_REPEAT):
        grass_rect = grass.get_rect()
        grass_rect.bottomleft = (i * grass_rect.width, HEIGHT)
        screen.blit(grass, grass_rect)


createClouds()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (30, 140, 184), sky_rect)
    pygame.draw.rect(screen, (4, 112, 236), sea_rect)

    drawClouds()
    drawGrass()

    pygame.display.flip()


pygame.quit()
