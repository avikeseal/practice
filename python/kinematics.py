#here is an attempt to optimize our program to make it run smoothly
#importing necessary modules:
import pygame
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#Initializing pygame:
pygame.init()

#display dimensions:
WIDTH, HEIGHT = 1200, 1700

#colors:
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#gravitational constant:
G = 0.01

#storage cap on position and velocities:
MAX_PATH_LENGTH = 500
MAX_V_LENGTH = 500

#this class represents each object in the simulation
#includes properties for position, velocity, mass, radius,
#color and path
#draw method handles drawing the object:
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


    
