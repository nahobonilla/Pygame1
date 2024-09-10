import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 130, 255)


display_surface.fill(BLUE)

CENTER = (450, 300)
RADIUS = 100
pygame.draw.circle(display_surface, MAGENTA, CENTER, RADIUS)

CENTER = (250, 150)
RADIUS = 50
pygame.draw.circle(display_surface, WHITE, CENTER, RADIUS)

CENTER = (150, 500)
RADIUS = 75
pygame.draw.circle(display_surface, WHITE, CENTER, RADIUS)

CENTER = (90, 400)
RADIUS = 51
pygame.draw.circle(display_surface, MAGENTA, CENTER, RADIUS)

CENTER = (150, 500)
RADIUS = 75
pygame.draw.circle(display_surface, WHITE, CENTER, RADIUS)

START = (330, 120)
END = (200, 415)
pygame.draw.line(display_surface, BLACK, START, END, 7)

START = (369, 200)
END = (186, 200)
pygame.draw.line(display_surface, WHITE, START, END, 7)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()