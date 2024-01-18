import sys, pygame
pygame.init()
###=- Variables -=###

#definice okna
rozliseni_okna = (1920,1080)
barva_okna = (0,255,255)

rychlost_gravitace = 0.5
#definice čtverce
barva_ctverce = (50,50,50)
velikost_ctverce_x, velikost_ctverce_y = 100,100
rychlost_ctverce = 1

pozice_ctverce_x = (rozliseni_okna[0]/2) #začne uprostřed
pozice_ctverce_y = rozliseni_okna[1] #začne dole

#Začátek programu

okno = pygame.display.set_mode(rozliseni_okna, ) #vydefinuje okno

while True: #ZAKLAD
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #definice INPUTU
    stiknute_klavesy = pygame.key.get_pressed()
    
    if stiknute_klavesy[pygame.K_ESCAPE]: #pokuď escape tak quit
        pygame.quit()

# POHYB
    if stiknute_klavesy[pygame.K_LEFT]:
        pozice_ctverce_x -= rychlost_ctverce
    if stiknute_klavesy[pygame.K_RIGHT]:
        pozice_ctverce_x += rychlost_ctverce
    if stiknute_klavesy[pygame.K_UP]:
        pozice_ctverce_y -= rychlost_ctverce*2
    if stiknute_klavesy[pygame.K_DOWN]:
        pozice_ctverce_y += rychlost_ctverce

    if pozice_ctverce_x < 0: #LEVA STRANA
        pozice_ctverce_x = 0
    if pozice_ctverce_y < 0: #HORNÍ STRANA
        pozice_ctverce_y = 0
    
    if pozice_ctverce_x >= rozliseni_okna[0] - velikost_ctverce_x: #PRAVA
        pozice_ctverce_x = rozliseni_okna[0] - velikost_ctverce_x
    if pozice_ctverce_y >= rozliseni_okna[1] - velikost_ctverce_y: #DOLNI STRANA
        pozice_ctverce_y = rozliseni_okna[1] - velikost_ctverce_y


    try: okno.fill(barva_okna) #barva okna
    except pygame.error: #prevents error
        break

    if (pozice_ctverce_y + velikost_ctverce_y) < rozliseni_okna[1]: #každej frame posune čtverec dolu kdyz je ve vzduchu
        pozice_ctverce_y += rychlost_gravitace 

    pygame.draw.rect(okno, barva_ctverce,(pozice_ctverce_x, pozice_ctverce_y,
                                          velikost_ctverce_x,velikost_ctverce_y))
    
    print("Čtverec x: " + str(pozice_ctverce_x) +"čtverec y:" + str(pozice_ctverce_y))
    pygame.display.update() 

