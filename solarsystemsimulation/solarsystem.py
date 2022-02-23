import pygame
import math
pygame.init()
#Dimensões da Tela
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')

GRAY = (79, 79, 79)
#Loop infinito com o intuito de observar as mudanças via coding

class Planet:
    #Distância Astronômica (Multiplicado por 1000 pra fazer a conversão de quilômetros para metros)
    AU = 149.6e6 * 1000
    #Constante Gravitacional
    G = 6.67428e-11
    SCALE = 250 / AU # 1 AU = 100 px
    TIMESTEP = 3600*24 # 1 dia

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        #Velocidades nos eixos X e Y iguais a 0 com o intuito de gerar uma estrutura com movimento circular uniforme e continuo.
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2 #Como o eixo X (abcissas)(X,Y) representa a largura e nesse caso o ponto 0,0 corresponde a lateral superior esquerda, fazemos a conversao com o intuito do desenho ser representado e utilizado com o centro no local correto.
        y = self.y * self.SCALE + HEIGHT / 2 #Similar ao superior a diferença é que o eixo Y (ordenadas) é representado pela altura (X,Y)
        pygame.draw.circle(win, self.color, (x, y), self.radius)

def master():
    acerto = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0,)

    while acerto:
        clock.tick(100)
        #WIN.fill(GRAY)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                acerto = False

    pygame.quit()

master()
