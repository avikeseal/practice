#trying to make an object move in circular motion:--------------------------------
#we need to update its position based on trig functions (sine and cosine)
#within the game loop.

#install pygame:
import pygame
import sys
import math

#intializing pygame:
pygame.init()



#setting up the screen:
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")

#set up the clock for a decent framerate:
clock = pygame.time.Clock()

#define colors:

GREEN = (0,128,0)
YELLOW = (255,255,0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#define the object:

#radius:
ball_radius = 20
#position of central object:
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_mass = 1000

#defining moving object:

#radius:
ball2_radius = 10
#position of second object:
ball2_pos = [WIDTH // 2 + 200, HEIGHT // 2]
#mass for second object:
ball2_mass = 40
#initial velocity:
ball2_v = [0, -2]

#gravitational constant:
G = 1



#list to store path:
path = []

#main game loop:
run = True
while run:
    #processes all events that pygame has recieved, 
    #if an event of type 'pygame.QUIT'is detected
    #it sets run to False which will exit the main loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #calculates the vector from first to second object:
    dx = ball_pos[0] - ball2_pos[0]
    dy = ball_pos[1] - ball2_pos[1]
    distance = math.sqrt( (dx**2)  + (dy**2) )

    #calculating gravity:
    if distance > 0:
        force = (G * ball_mass * ball2_mass) / (distance**2)
        angle = math.atan2(dy,dx)
        force_x = force * math.cos(angle)
        force_y = force * math.sin(angle)

        #updating object's velocity:
        ball2_v[0] += force_x / ball2_mass
        ball2_v[1] += force_y / ball2_mass

    #updating the object's position:
    ball2_pos[0] += ball2_v[0]
    ball2_pos[1] += ball2_v[1]


    #fill the screen with black:
    screen.fill(BLACK)
    #draw the ball:
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.draw.circle(screen, GREEN, (int(ball2_pos[0]), int(ball2_pos[1])), ball2_radius)    
    
    #inserting the frame rate first and display next seems to run the program

    #cap the frame rate at 60 fps:
    clock.tick(60)

    #updating the display:
    pygame.display.flip()

#quit pygame:
pygame.quit()
sys.exit()



