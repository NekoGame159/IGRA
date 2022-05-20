import pygame
import sys

pygame.init()
background = pygame.image.load("FON.png")
screen = pygame.display.set_mode([1200,595])
clock = pygame.time.Clock()
pygame.display.set_caption("pygame test1")

def draw():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
    pygame.draw.rect(screen, (0,0,0), left_wall, 0)
    pygame.draw.rect(screen, (0,0,0), right_wall, 0)
    pygame.display.update()

x = 300
y = 300
speed = 3
width = 40
height = 80

left_wall = pygame.Rect(-2,0,2,600)
right_wall = pygame.Rect(1201,0,2,600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    character = pygame.Rect(x,y,width, height)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] or pressed[pygame.K_w] or pressed[pygame.K_SPACE]:
        y -= speed
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and not character.colliderect(right_wall):
        x += speed
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        y += speed
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and not character.colliderect(left_wall):
        x -= speed

    draw()
    clock.tick(60)