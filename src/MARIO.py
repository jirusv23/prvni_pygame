import sys, pygame

pygame.init()
###=- Variables -=###

#definice okna
rozliseni_okna = (1024,576)
barva_okna = (0,255,255)

rychlost_gravitace = 0.25
#definice čtverce
barva_ctverce = (50,50,50)
velikost_ctverce_x, velikost_ctverce_y = 100,100
rychlost_ctverce = 0.5

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
    def zkouškaHorizontalníhoPohybu():    
        global pozice_ctverce_x
        if stiknute_klavesy[pygame.K_LEFT]:
            pozice_ctverce_x -= rychlost_ctverce
        if stiknute_klavesy[pygame.K_RIGHT]:
            pozice_ctverce_x += rychlost_ctverce
    zkouškaHorizontalníhoPohybu()
    if stiknute_klavesy[pygame.K_UP] and pozice_ctverce_y + velikost_ctverce_y == rozliseni_okna[1]: #posune nahoru když je pozice ctverce dole
        i = 400
        while i > 0:
            i -= 1
            pozice_ctverce_y -= 0.25
            zkouškaHorizontalníhoPohybu()
            kontrolaZdi()
            update()


    if pozice_ctverce_x < 0: #LEVA STRANA
        pozice_ctverce_x = 0
    if pozice_ctverce_y < 0: #HORNÍ STRANA
        pozice_ctverce_y = 0
    
    def kontrolaZdi():
        global pozice_ctverce_x, pozice_ctverce_y
        if pozice_ctverce_x >= rozliseni_okna[0] - velikost_ctverce_x: #PRAVA
            pozice_ctverce_x = rozliseni_okna[0] - velikost_ctverce_x
        if pozice_ctverce_y >= rozliseni_okna[1] - velikost_ctverce_y: #DOLNI STRANA
            pozice_ctverce_y = rozliseni_okna[1] - velikost_ctverce_y
    kontrolaZdi()

    '''try: okno.fill(barva_okna) #barva okna
    except pygame.error: #prevents error
        break'''


    if (pozice_ctverce_y + velikost_ctverce_y) < rozliseni_okna[1]: #každej frame posune čtverec dolu kdyz je ve vzduchu
        pozice_ctverce_y += rychlost_gravitace 
    

    def update():
        okno.fill(barva_okna)  
        pygame.draw.rect(okno, barva_ctverce,(pozice_ctverce_x, pozice_ctverce_y,velikost_ctverce_x,velikost_ctverce_y))                                    
        
        #print("Čtverec x: " + str(pozice_ctverce_x) +"čtverec y:" + str(pozice_ctverce_y))
        pygame.display.update() 
        

    update()