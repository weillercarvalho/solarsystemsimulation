import pygame
import math
pygame.init()
#Dimensões da Tela
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')

#Loop infinito com o intuito de observar as mudanças via coding
def master():
    acerto = True

    while acerto:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                acerto = False

    pygame.quit()

master()