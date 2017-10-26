import sys, pygame, util
from pygame.locals import *
from heroe import *
from portales import *
from villano import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Portales 3.0" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    pygame.mouse.set_visible(False)
    heroe = Heroe()
    villanos = [Villano((10,200),(3)),
               Villano((100,350),(3)),
               Villano((400,400),(3)),
               Villano((400,250),(3)),
               Villano((400,20),(3))]
               
    portales = [Portales((25,20),(1)),
                Portales((25,400),(2)),
                Portales((550,20),(3)),
                Portales((550,400),(4)),
                Portales((270,200),(5)),
                ]

    while True:
        fuente = pygame.font.Font(None,25)
        cont = 0
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(255,255,255))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(255,255,255))

        heroe.update()
        
        for n in villanos:
			n.update(heroe)
		
        if heroe.rect.colliderect(portales[4].rect):
			heroe.puntos = heroe.puntos + 1
			heroe.portal = randint (0,3)
			heroe.rect.x = portales[heroe.portal].rect.x
			heroe.rect.y = portales[heroe.portal].rect.y
			
	for n in villanos:
		if heroe.rect.colliderect(n.rect):
			if heroe.vida > 0:
				heroe.vida = heroe.vida - 1
			n.rect.x = randint(20,440)
			n.rect.y = randint(20,640)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.blit(background_image, (0,0))
        for n in villanos:
			screen.blit (n.image, n.rect)
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_puntos,(320,455))
        screen.blit(texto_vida,(200,455))

        for n in portales:
            screen.blit(n.image, n.rect)
         
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
