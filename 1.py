import pygame

pygame.init()

SCREEN=pygame.display.set_mode((400,600))
working=True
print('hello')
while working:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            working=False
         if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_r:
                 SCREEN.fill((255,0,0))
            if event.key== pygame.K_g:
                 SCREEN.fill((0,255,0))
            if event.key== pygame.K_b:
                 SCREEN.fill((0,0,255))
    pygame.display.update()