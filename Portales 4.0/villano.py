import pygame
from pygame.sprite import Sprite
from pygame import *
from heroe import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.imagenes = [util.cargar_imagen('imagenes/caza_arr.png'),
						util.cargar_imagen('imagenes/caza_aba.png'),
						util.cargar_imagen('imagenes/caza_izq.png'),
						util.cargar_imagen('imagenes/caza_der.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.vida = 100
		self.rect.move_ip(coord[0],coord[1])
		self.velocidad = vel
		
	def update(self,heroe):
		if self.vida > 0:
			if self.rect.x < heroe.rect.x:
				self.rect.x = self.rect.x + 1
				self.image = self.imagenes[3]
			if self.rect.y < heroe.rect.y:
				self.rect.y = self.rect.y + 1
				self.image = self.imagenes[1]
			if self.rect.x > heroe.rect.x:
				self.rect.x = self.rect.x - 1
				self.image = self.imagenes[2]
			if self.rect.y > heroe.rect.y:
				self.rect.y = self.rect.y - 1
				self.image = self.imagenes[0]
		
