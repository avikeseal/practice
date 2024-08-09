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
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Circular motion")

#set up the clock for a decent framerate:
clock = pygame.time.Clock()

#define colors:
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#define the object:
ball_radius = 20
#center of the circular path:
center_x, center_y = 400, 300
#radius of the circular path:
orbital_radius = 200
#starting angle:  
angle = 0
#angular speed (radians per frame):
angular_speed = 0.02

#main game loop:
run = True
while run:
    #processes all events that pygame has recieved, 
    #if an event of type 'pygame.QUIT'is detected
    #it sets run to False which will exit the main loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #game state update:
    #this updates the position of the ball to move in circular path
    #calculates the new x and y coordinates using trig functions based on the current 'angle'.
    #angle is then incremented by 'angular speed' to ensure continous motion:
    ball_x = center_x + orbital_radius * math.cos(angle) 
    ball_y = center_y + orbital_radius * math.sin(angle)
    angle += angular_speed

    #fill the screen with black:
    screen.fill(BLACK)

    #draw the ball:
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)


    #inserting the frame rate first and display next seems to run the program

    #cap the frame rate at 60 fps:
    clock.tick(60)

    #updating the display:
    pygame.display.flip()

#quit pygame:
pygame.quit()
sys.exit()



