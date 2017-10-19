import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
from heroe import *
import util

class Portales(Sprite):
	def __init__(self,coord,cod):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/portal.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[0])
		
	def transportar(heroe):
		if heroe.portal == 1:
			heroe.rect.move_ip(100,100)
		if heroe.portal == 2:
			heroe.rect.move_ip(200,200)
		if heroe.portal == 3:
			heroe.rect.move_ip(300,300)
		if heroe.portal == 4:
			heroe.rect.move_ip(400,400)
