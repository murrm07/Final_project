#Ryan Jeans
#march 3d 2025
#to create space invaders game

import pygame
import manager
import interfaces.title_screen
import interfaces.password
import interfaces.map   
pygame.init()

window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Rockstar")

while True:
    if manager.screen == 0:
        interfaces.title_screen.output(window)
    if manager.screen == 1:
        interfaces.password.output(window)
    if manager.screen == 2:
        interfaces.map.output(window)
   
        
