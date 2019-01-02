import pygame
from pygame.locals import *
pygame.init()

running=True

while running:
    gamewindow=pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Adventure Game")
    black=(0, 0, 0)
    white=(255, 255, 255)
    img=pygame.image.load("/Users/denism/Downloads/ninja.png")

    def sprite(x, y):
        gamewindow.blit(img, (x, y))

    x=(800*0.45)
    y=(600*0.8)

    gamewindow.fill(white)
    sprite(x,y)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==QUIT:            
            running=False
            pygame.quit()
