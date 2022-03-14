import pygame
import math
pygame.init()

WIDTH, HEIGHT =  800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
GREEN = (0, 100, 0)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
	AU = 149.6e6 * 1000 #Distância Astronômica (Multiplicado por 1000 pra fazer a conversão de quilômetros para metros).
	G = 6.67428e-11 #Constante Gravitacional
	SCALE = 250 / AU  # 1AU = 100 px
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
		y = self.y * self.SCALE + HEIGHT / 2 #Similar ao superior a diferença é que o eixo Y (ordenadas) é representado pela altura (X,Y).

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2
				y = y * self.SCALE + HEIGHT / 2
				updated_points.append((x, y))

			pygame.draw.lines(win, self.color, False, updated_points, 2)

		pygame.draw.circle(win, self.color, (x, y), self.radius)
		
		if not self.sun:
			distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
			win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

	def attraction(self, other):
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		if other.sun:
			self.distance_to_sun = distance

		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y

	def update_position(self, planets):
		total_fx = total_fy = 0
		for planet in planets:
			if self == planet: # A instrução continue tem como função saltar o ato de 0 por 0 pois, é impossivel existir uma distância entre você e você. Pois você é seu próprio eixo.
				continue

			fx, fy = self.attraction(planet)
			total_fx += fx
			total_fy += fy

		self.x_vel += total_fx / self.mass * self.TIMESTEP
		self.y_vel += total_fy / self.mass * self.TIMESTEP

		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))


def main():
	run = True
	clock = pygame.time.Clock()

	sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
	sun.sun = True

	earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)  # O sentido do eixo X tem que ter sinal inverso ao sinal da velocidade do eixo em X para que em um eixo de abcissas e coordenadas o movimento seja circular.
	earth.y_vel = 29.783 * 1000 
    
    earth2 = Planet(-1 * Planet.AU, 0, 12, GREEN, 5.9742 * 10**24)
    earth2.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mars2 = Planet(-1.524 * Planet.AU, 0, 9, WHITE, 6.39 * 10**23)
    mars2.y_vel = 24.077 * 1000
    
    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000
    
    planets = [sun, earth, mars, mercury, venus, earth2, mars2]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0)) #Fundo gerado com o intuito de gerar a sobreposição dos planetas em relação a estrutura de fundo.

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Loop infinito com o intuito de observar as mudanças parado via altf4/X.
                run = False

		for planet in planets:
			planet.update_position(planets)
			planet.draw(WIN)

		pygame.display.update()

	pygame.quit()


main()