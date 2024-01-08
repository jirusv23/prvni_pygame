import sys

import pygame
pygame.init()

pozice_micku_x = 400
pozice_micku_y = 300

velikost_micku = 50

rychlost_micku_x = 0.3
rychlost_micku_y = 0.3

pozice_hrace_x = 300
pozice_hrace_y = 200

rychlost_hrace = 0.3

rozliseni_okna = (800, 600)

okno = pygame.display.set_mode(rozliseni_okna)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    stisknute_klavesy = pygame.key.get_pressed()
    
    if stisknute_klavesy[pygame.K_RIGHT]:
        pozice_hrace_x += rychlost_hrace
    if stisknute_klavesy[pygame.K_LEFT]:
        pozice_hrace_x -= rychlost_hrace
    
    pozice_micku_x += rychlost_micku_x
    pozice_micku_y += rychlost_micku_y
    
    if pozice_micku_x > rozliseni_okna[0] - velikost_micku:
        pozice_micku_x = rozliseni_okna[0] - velikost_micku
        rychlost_micku_x *= -1
    if pozice_micku_y > rozliseni_okna[1] - velikost_micku:
        pozice_micku_y = rozliseni_okna[1] - velikost_micku
        rychlost_micku_y *= -1
    if pozice_micku_x < 0:
        pozice_micku_x = 0
        rychlost_micku_x *= -1
    if pozice_micku_y < 0:
        pozice_micku_y = 0
        rychlost_micku_y *= -1
    
    okno.fill((0, 255, 255))
    
    pygame.draw.rect(okno, (0, 0, 0), (pozice_hrace_x, pozice_hrace_y, 50, 50))
    pygame.draw.ellipse(okno, (255, 255, 255), (pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku))
    
    pygame.display.update()
