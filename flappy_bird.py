import pygame
from pygame.locals import *
from pygame.sprite import Group

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 620
screen_height = 620

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bird')

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')

#game variables
ground_scroll = 0
scroll_speed = 4

#animates bird
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bird1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)


run = True
while run:
    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,0))

    bird_group.draw(screen)

    #draw and scroll the ground
    screen.blit(ground, (ground_scroll,500))
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 35:
        ground_scroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
