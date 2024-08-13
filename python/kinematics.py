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

