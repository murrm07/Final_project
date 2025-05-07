#By: Ryan Jeans, Noel clarke
#Date: 2025-05-05
#Program Details: Our final project is to make a battling rockstar game.
#This is the main file that will run the game.

import pygame,sys
import interfaces.password
import manager
import interfaces.title_screen
pygame.init()


#Setup of Starting objects

window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Welcome to the Rockstar Battle")

while True:
    if manager.screen == 0:
        interfaces.title_screen.output(window)
    if manager.screen == 1:
        interfaces.password.output(window)
    