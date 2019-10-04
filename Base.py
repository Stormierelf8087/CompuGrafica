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
    def __init__(self,punto,color):
        #Constructor
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,50])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=punto[0]
        self.rect.y=punto[1]
        self.velx=0
        self.vely=0

    def update(self):
        '''Actualizar jugador'''
        self.rect.x +=self.velx
        self.rect.y +=self.vely


if __name__ == '__main__':
    pygame.init()
    #Declaracion de variables
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    jugadores=pygame.sprite.Group()

    puntoinicial=[100,50]
    #Agregar jugador 1
    j=Jugador(puntoinicial,VERDE)
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
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-5
                if event.key == pygame.K_DOWN:
                    j.velx=0
                    j.vely=5
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
