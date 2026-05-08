import pygame

from config import DEBUG, DEBUG_COLOR, DEBUG_FONT, DEBUG_FONT_SIZE, DEBUG_WIDTH


def createCollisionRect(rect_parent: pygame.Rect, padding: int) -> pygame.Rect:
    return pygame.Rect(
        rect_parent.left + padding,
        rect_parent.top + padding,
        rect_parent.width - 2 * padding,
        rect_parent.height - 2 * padding,
    )


class Debug:
    def __init__(self):
        self.font = pygame.font.SysFont(DEBUG_FONT, DEBUG_FONT_SIZE)

    def draw(self, screen: pygame.Surface, surface: pygame.Surface, rect: pygame.Rect):
        screen.blit(surface, rect)

        if DEBUG:
            pygame.draw.rect(screen, DEBUG_COLOR, rect, DEBUG_WIDTH)

            coord_surface = self.font.render(
                f"x={rect.x}, y={rect.y}", False, DEBUG_COLOR
            )
            screen.blit(coord_surface, (rect.x, rect.y - DEBUG_FONT_SIZE))


d = None


def draw(screen: pygame.Surface, surface: pygame.Surface, rect: pygame.Rect):
    global d

    if not d:
        d = Debug()
    d.draw(screen, surface, rect)
