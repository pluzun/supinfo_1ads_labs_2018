import pygame, sys
from pygame.locals import *
pygame.init()

FPS = 1
fpsClock = pygame.time.Clock()

fond = pygame.image.load("fond.jpg")
ariane = pygame.image.load('avion.png')

pygame.display.set_caption('Hello SUPINFO')
maSurface = pygame.display.set_mode((640, 480))
maSurface.blit(fond,(0,0))
maSurface.blit(ariane,(500,300))

inProgress = True
while inProgress:
    for event in pygame.event.get():
        print('hello world!')
        if event.type == QUIT:
            inProgress = False
        if event.type == MOUSEBUTTONUP:
            x,y = event.pos
            maSurface.blit(fond,(0,0))
            maSurface.blit(ariane,(x,y))
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
