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


class Button:

    def __init__(
        self,
        text: str,
        fontSize: int = 40,
        bgSize: tuple[int, int] = (250, 80),
        bgColor: pygame.Color = (255, 255, 255),
        bgHoverColor: pygame.Color = (0, 0, 0),
        textColor: pygame.Color = (0, 0, 0),
        textHoverColor: pygame.Color = (255, 255, 255),
    ):
        self.text = text
        self.font = pygame.font.Font(None, fontSize)

        self.bgSize = bgSize

        self.bgColor = bgColor
        self.bgHoverColor = bgHoverColor
        self.textColor = textColor
        self.textHoverColor = textHoverColor

    def draw(self, screen: pygame.Surface, pos: tuple[int, int], hover: bool = False):
        bg_color = self.bgHoverColor if hover else self.bgColor
        text_color = self.textHoverColor if hover else self.textColor

        bg_rect = pygame.Rect(
            pos[0] - self.bgSize[0] // 2,
            pos[1] - self.bgSize[1] // 2,
            self.bgSize[0],
            self.bgSize[1],
        )

        text = self.font.render(self.text, True, text_color)
        text_rect = text.get_rect(center=pos)

        pygame.draw.rect(
            screen,
            bg_color,
            bg_rect,
            border_radius=10,
        )
        screen.blit(text, text_rect)
