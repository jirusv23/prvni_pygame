import sys

import pygame
pygame.init()

okno = pygame.display.set_mode((800, 600))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    okno.fill((0, 255, 255))
    
    pygame.draw.rect(okno, (0, 0, 0), (300, 200, 50, 50))
    pygame.draw.ellipse(okno, (255, 255, 255), (400, 300, 50, 50))
    
    pygame.display.update()
