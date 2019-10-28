#!/usr/bin/python3

#Simple Screensaver in Python3
#2019 Python Learning Repo
#written by rwx-777

import pygame, sys
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
cover = pygame.image.load("venice.jpg") #Path to picture you want as a Screensaver 

window = pygame.display.set_mode((1500, 1000)) #length , height (y,x) / Screensaver Size
running = True #keeps programm in memory

x = 0
y = 0
sx = 100 #pixels per second / speed for x axis
sy = 100 #you can make the pciture move faster

while running:
    for event in pygame.event.get(): #keep it running until player quits
        if event.type == QUIT:
            running = False

    delta = clock.tick(30) / 1000 #Makes image move smoothly
    x = x + sx * delta #These are the clacluations 
    y = y + sy * delta

    #Height
    if y + 450 > window.get_height() or y < 0: #change the number depending on the size of your picture
        sy = sy * -1 #makes image bounce at bottom of screen

    #Width
    if x + 300 > window.get_width() or x < 0: #okay i figured it out type the width and height of your image for the values
        sx = sx * -1

    window.fill((0,0,0))
    window.blit(cover, (x,y)) #selects the image and sets position
    pygame.display.update()

pygame.quit()
