import sys, pygame
pygame.init()
###=- Variables -=###

#definice okna
rozliseni_okna = (1920,1080)
barva_okna = (0,255,255)

#definice čtverce
barva_ctverce = (50,50,50)
velikost_ctverce_x,velikost_ctverce_y = 50,50


#Začátek programu

okno = pygame.display.set_mode(rozliseni_okna, pygame.FULLSCREEN) #vydefinuje okno

while True: #ZAKLAD
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #definice INPUTU
    stiknute_klavesy = pygame.key.get_pressed()
    
    if stiknute_klavesy[pygame.K_ESCAPE]: #pokuď escape tak quit
        pygame.quit()


    okno.fill(barva_okna) #barva okna
    
    pygame.draw.rect(okno, barva_ctverce, (velikost_ctverce_x,velikost_ctverce_y,50,50))
    
    pygame.display.update() 

