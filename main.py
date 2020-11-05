import pygame
import sys 

W, H = 1000, 800
collide = False
n = 0

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# ЦВЕТА
RED = (255, 165, 0, 180)
BLUE = (0, 250, 154, 180)
YELLOW = (138, 43, 226, 180)
BG = (0, 255, 255)


pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((W, H))
font = pygame.font.Font(None, 32)
# создаем поверхность размером в  2-а раза больше радиуса круга и вкл. альфа-канал
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
# на созданной поверхности рисуем круг желтого цвета 
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

clock = pygame.time.Clock()
FPS = 100
speed_x, speed_y = 5, 1


ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()

while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos  

    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > W:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > H:
        speed_y = -speed_y

    screen.fill(BG)
    COLOR = RED if collide else BLUE
    # rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    screen.blit(surface, rect1)

    if rect1.colliderect(rect2):
        collide = True
        if COLOR == BLUE:
            n += 1
    else:
        collide = False

    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(n), 1, RED), (10, 10))
    pygame.display.update()
