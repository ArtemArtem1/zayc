import pygame
from pygame.draw import ellipse, circle

pygame.init()

FPS = 30
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_ellipse_centered(surface, color, x, y, width, height):
    """Рисует эллипс по центру."""
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_circle_centered(surface, color, x, y, radius):
    """Рисует круг по центру."""
    circle(surface, color, (x, y), radius)


def draw_hare(surface, x, y, width, height, color):
    """
    Рисует зайца.
    x, y — верхняя опорная точка фигуры.
    width, height — общий размер зайца.
    """

    body_width = width // 2
    body_height = height // 2
    body_x = x
    body_y = y + body_height // 2

    head_diameter = height // 4
    head_x = x
    head_y = y - head_diameter // 2

    ear_width = width // 8
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    ear_positions = [
        x - head_diameter // 4,
        x + head_diameter // 4
    ]

    leg_width = width // 4
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    leg_positions = [
        x - width // 4,
        x + width // 4
    ]

    draw_ellipse_centered(surface, color, body_x, body_y, body_width, body_height)
    draw_circle_centered(surface, color, head_x, head_y, head_diameter // 2)

    for ear_x in ear_positions:
        draw_ellipse_centered(surface, color, ear_x, ear_y, ear_width, ear_height)

    for leg_x in leg_positions:
        draw_ellipse_centered(surface, color, leg_x, leg_y, leg_width, leg_height)


hares = [
    {"x": 200, "y": 200, "width": 200, "height": 400, "color": (200, 200, 200)},
    # Можно быстро добавлять новых зайцев:
    # {"x": 100, "y": 220, "width": 120, "height": 240, "color": (180, 180, 180)},
    # {"x": 300, "y": 220, "width": 100, "height": 200, "color": (150, 150, 150)},
]

screen.fill(BACKGROUND_COLOR)

for hare in hares:
    draw_hare(
        screen,
        hare["x"],
        hare["y"],
        hare["width"],
        hare["height"],
        hare["color"]
    )

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()