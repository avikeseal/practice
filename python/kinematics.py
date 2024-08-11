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
pygame.display.set_caption("Circular motion")

#set up the clock for a decent framerate:
clock = pygame.time.Clock()

#define colors:
GREEN = (0,128,0)
YELLOW = (255,255,0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#define the object:

#radius of first object:
ball_radius = 20
#position of first object:
ball_pos = [WIDTH // 2, HEIGHT // 2]

#center of the circular path:
#center_x, center_y = 400, 300

#radius of the circular path:
orbital_radius = 100
#starting angle:  
angle = 0
#angular speed (radians per frame):
angular_speed = 0.04
#mass of the ball:
ball_mass = 1000
#velocity:
ball_v = [-1, -3]
#force-components in x and y direction:
#force1 = 

#defining another object:
ball2_radius = 20
#position of second object:
ball2_pos = [WIDTH // 2 + 200, HEIGHT // 2]
#radius of the circular path:
orbital_radius2 = 200
#angular speed:
angular_speed2 = 0.02
#mass for second object:
ball2_mass = 2000
#velocity:
ball2_v = [0, -2]



#list to store path:
orbital_path = []
orbital_path2 = []

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
    dx = ball_pos[0] - ball_pos[0]
    dy = ball2_pos[1] - ball2_pos[1]
    distance = math.sqrt( (dx**2) + (dy**2) )

    #calculating gravity:




    #game state update:
    #this updates the position of the ball to move in circular path
    #calculates the new x and y coordinates using trig functions based on the current 'angle'.
    #angle is then incremented by 'angular speed' to ensure continous motion:
    #ball_x = center_x + orbital_radius * math.cos(angle) 
    #ball_y = center_y + orbital_radius * math.sin(angle)
    #ball2_x = center_x + orbital_radius2 * math.cos(angle)
    #ball2_y = center_y + orbital_radius2 * math.sin(angle)
    angle += angular_speed

    #store the position in the path list:
    orbital_path.append((ball_pos, ball_pos))
    orbital_path2.append((ball2_pos,ball2_pos))

    #fill the screen with black:
    screen.fill(BLACK)

    #draw the orbital path:
    if len(orbital_path) > 1:
        pygame.draw.lines(screen, YELLOW, False, orbital_path, 1)
        pygame.draw.lines(screen, YELLOW, False, orbital_path2, 1)

    #draw the ball:
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.draw.circle(screen, GREEN,(int(ball2_pos[0]), int(ball2_pos[1])), ball2_radius)    
    
    #inserting the frame rate first and display next seems to run the program

    #cap the frame rate at 60 fps:
    clock.tick(60)

    #updating the display:
    pygame.display.flip()

#quit pygame:
pygame.quit()
sys.exit()



