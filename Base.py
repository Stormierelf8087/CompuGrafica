'''
Programa: Juego demostracion
version: b1_2DireccionesPersonaje,  juego de dos direcciones
Autor: Andres Patiño
fecha: Octubre 4 de 2019
'''

import pygame
import math
import random

BLANCO = [255,255,255]
VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL =  [0,0,255]
NEGRO = [0,0,0]

ANCHO = 600
ALTO = 400

class Jugador(pygame.sprite.Sprite):
    def __init__(self,color):
        #Constructor
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,50])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=ALTO-self.rect.height
        self.velx=0
        self.vely=0

    def update(self):
        '''Actualizar jugador'''
        self.rect.x +=self.velx


if __name__ == '__main__':
    pygame.init()
    #Declaracion de variables
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    jugadores=pygame.sprite.Group()

    #Agregar jugador 1
    j=Jugador(VERDE)
    jugadores.add(j)

    #ciclo para la ventana
    fin = False
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            #Gestion de teclas para jugador 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0

            if event.type == pygame.KEYUP:
                j.velx=0
                j.vely=0

        #Gestion de control

        #Gestion de pantalla

        #Actualizar objetos
        jugadores.update()

        pantalla.fill(NEGRO)
        #Dibujar objetos
        jugadores.draw(pantalla)

        pygame.display.flip()
        reloj.tick(60)
