import sys, pygame, util
from pygame.locals import *
from heroe import *
from portales import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Portales 2.0" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    pygame.mouse.set_visible(False)
    heroe = Heroe()
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

        heroe.update()
		
        if heroe.rect.colliderect(portales[4].rect):
			heroe.puntos = heroe.puntos + 1
			heroe.portal = randint (0,3)
			heroe.rect.x = portales[heroe.portal].rect.x
			heroe.rect.y = portales[heroe.portal].rect.y
        
        if heroe.rect.colliderect(portales[0].rect):
			heroe.puntos = heroe.puntos + 1
			heroe.portal = randint (1,2)
			heroe.rect.x = portales[heroe.portal].rect.x
			heroe.rect.y = portales[heroe.portal].rect.y
        
        if heroe.rect.colliderect(portales[3].rect):
			heroe.puntos = heroe.puntos + 1
			heroe.portal = randint (1,2)
			heroe.rect.x = portales[heroe.portal].rect.x
			heroe.rect.y = portales[heroe.portal].rect.y
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_puntos,(260,455))

        for n in portales:
            screen.blit(n.image, n.rect)
         
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
