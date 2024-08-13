#here is an attempt to optimize our program to make it run smoothly
#importing necessary modules:
import os
import pygame
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#setting the window to appear in middle of the screen:
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Initializing pygame:
pygame.init()

#display dimensions:
WIDTH, HEIGHT = 2560, 1080

#colors:
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#gravitational constant:
G = 2

#storage cap on position and velocities:
MAX_PATH_LENGTH = 500
MAX_V_LENGTH = 500

#this class represents each object in the simulation
#includes properties for position, velocity, mass, radius,
#color and path:
class Body:
    def __init__(self, x, y, mass, radius, color):
        self.pos = [x,y]
        self.vel = [0, 0]
        self.mass = mass
        self.radius = radius
        self.color = color 
        self.path = []

    #apply_gravity method calculates gravity
    def apply_gravity(self, other):
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        distance = math.sqrt( (dx**2) + (dy**2) )

        if distance > 0:
            force = (G * self.mass * other.mass)/(distance**2)
            angle = math.atan2(dy, dx)
            force_x = force * math.cos(angle)
            force_y = force * math.sin(angle)

            self.vel[0] += force_x / self.mass
            self.vel[1] += force_y / self.mass

    #update_position method updates the position based on velocity:
    def update_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.path.append((int(self.pos[0]), int(self.pos[1])))

        #remove old path data to free up memory:
        if len(self.path) > MAX_PATH_LENGTH:
            self.path.pop(0)
    
    #draw method handles drawing the object:
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(int(self.pos[0]), int(self.pos[1])), self.radius)
        if len(self.path) > 1:
            pygame.draw.lines(screen, self.color, False, self.path, 2)

#this function creates a graph that displays velocities over time:
def create_graph(velocities, figsize=(4, 2)):
    fig, ax = plt.subplots()
    ax.plot(velocities, label='Velocity')
    ax.axhline(y=np.min(velocities), color='r', linestyle='--', label='Min Velocity')
    ax.axhline(y=np.max(velocities), color='g', linestyle='--', label='Max Velocity')
    ax.legend()

    canvas = FigureCanvas(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    #close the figure to free up memory:
    plt.close(fig)
    return raw_data, size

#the main function initializes the Pygame screen, 
#creates the bodies and runs the main loop:
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Gravity Simulation')
    clock = pygame.time.Clock()

    #initializing bodies:
    central_body = Body(WIDTH//2, HEIGHT//2, 1000, 20, RED)
    moving_body = Body((WIDTH//2 + 200), HEIGHT//2, 1, 10, BLUE)
    #initial velocity:
    moving_body.vel = [0, -2]

    bodies = [central_body, moving_body]
    velocities = []

    #main loop:
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #calculates gravity and updates position:
        for body in bodies:
            if body != central_body:
                body.apply_gravity(central_body)
            if body != moving_body:
                body.apply_gravity(moving_body)
            body.update_position()

        #calculate and store velocity for the moving body:
        velocity = math.sqrt((moving_body.vel[0]**2) + (moving_body.vel[1]**2))
        velocities.append(velocity)
        #removing old velocity data to free up memory:
        if len(velocities) > MAX_V_LENGTH:
            velocities.pop(0)
        
        #creating the graph:
        raw_data, size = create_graph(velocities)
        graph_surface = pygame.image.fromstring(raw_data, size, 'RGB')

        #drawing eveything:
        screen.fill(BLACK)
        for body in bodies:
            body.draw(screen)

        #displaying the graph:
        #adjusted position:
        screen.blit(graph_surface, (50, 40))

        #cap the frame rate to 60 fps:
        clock.tick(60)

        #update the display:
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()



    
