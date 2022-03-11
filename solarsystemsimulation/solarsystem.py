import pygame
import math
pygame.init()
#Dimensões da Tela
WIDTH, HEIGHT = 1440, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System Simulation')

GRAY = (79, 79, 79)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GOLDEN = (205,149,12)
CORN_SILK = (255,248,220)
GREEN = (127,255,0)
WHITE = (255,255,255)


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

    def attraction(self,other):
        other_x, other_y =other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y

def master():
    acerto = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)

    earth2 = Planet(-1 * Planet.AU, 0, 12, GREEN, 5.9742 * 10**24)

    mars = Planet(-1.524 * Planet.AU, 0, 9, RED, 6.39 * 10**23)

    mars2 = Planet(-1.524 * Planet.AU, 0, 12, CORN_SILK, 6.39 * 10**23)

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GOLDEN, 3.30 * 10**23)

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)

    planets = [sun, earth, mars2, mercury, mars, earth2, venus]

    while acerto:
        clock.tick(100)
        #WIN.fill(GRAY)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:#Loop infinito com o intuito de observar as mudanças parado via altf4/X
                acerto = False
        
        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()    

    pygame.quit()

master()
