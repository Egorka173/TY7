import pygame
import sys 

W, H = 400, 400

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# ЦВЕТА
RED = (250, 0, 0)
BLUE = (0, 0, 250)
YELLOW = (250, 250, 0)
BG = (128, 128, 128)


pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((W, H))


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION
            circle_pos = e.pos

screen.fill(BG)

rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
rect2 = 
pygame.display.update()
