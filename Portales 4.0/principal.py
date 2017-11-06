import sys, pygame, util
from pygame.locals import *
from heroe import *
from portales import *
from villano import *
from random import *
import copy

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def ordenar(lista):
    for x in range(0,len(lista)):
        for y in range(0,len(lista)):
            if int(lista[x]) > int(lista[y]):
                temp = lista[x]
                lista[x] = lista[y]
                lista[y] = temp

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Portales 4.0" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    inicio_image = util.cargar_imagen('imagenes/inicio.jpg')
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
    jugando = False

       
    while True:
        teclas = pygame.key.get_pressed()
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()    
        if teclas[K_SPACE]:
                jugando = True
                heroe.vida = 100
                heroe.puntos = 0
                
        if jugando:
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

                
                
                
                screen.blit(background_image, (0,0))
                for n in villanos:
                                screen.blit (n.image, n.rect)
                screen.blit(heroe.image, heroe.rect)
                screen.blit(texto_puntos,(320,455))
                screen.blit(texto_vida,(200,455))

                for n in portales:
                    screen.blit(n.image, n.rect)
                
                if heroe.vida <= 0:
                        puntos = open('puntaje.txt', 'r')
                        pts = [x[:-1] for x in puntos.readlines()]
                        puntos.close()
                        pts.append(heroe.puntos)
                        jugando = False
                        puntos = open('puntaje.txt', 'w')
                        for x in pts:
                            puntos.write(str(x)+'\n')
                        puntos.close()    
                 
        else:
                screen.blit(inicio_image, (0, 0))
                puntos = open('puntaje.txt', 'r')
                pts = [x[:-1] for x in puntos.readlines()]
                puntos.close()
                ordenar(pts)
                linea = 120
                fuente = pygame.font.Font(None, 25)
                texto_puntos = fuente.render("Mejores puntajes: ", 1, (1, 1, 1))
                screen.blit(texto_puntos, (20, linea))
                fuente = pygame.font.Font(None, 23)
                for x in pts[:10]:
                    texto_puntos = fuente.render(str(x), 1, (1,1,1))
                    screen.blit(texto_puntos, (80, linea + 25))
                    linea += 25
                    
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game()
