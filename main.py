#Ryan Jeans
#march 3d 2025
#to create space invaders game

import pygame
import interfaces.boss
import interfaces.level_1
import interfaces.lose
import interfaces.win
import manager
import interfaces.title_screen
import interfaces.password
import interfaces.map   
import interfaces.options
import interfaces.level_2
import interfaces.level_3
import interfaces.story
import interfaces.boss
import interfaces.c1
import interfaces.c2
import interfaces.c3
import interfaces.c4
import interfaces.gc
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
    if manager.screen == 3:
        interfaces.level_1.output(window)
    if manager.screen == 4:
        interfaces.options.output(window)
    if manager.screen == 5:
        interfaces.win.output(window)
    if manager.screen == 6:
        interfaces.lose.output(window)
    if manager.screen == 7:
        interfaces.level_2.output(window)   
    if manager.screen == 8:
        interfaces.level_3.output(window)
    if manager.screen == 9:
        interfaces.story.output(window)
    if manager.screen == 10:
        interfaces.boss.output(window)
    if manager.screen == 11:
        interfaces.c1.output(window)
    if manager.screen == 12:
        interfaces.c2.output(window)
    if manager.screen == 13:
        interfaces.c3.output(window)
    if manager.screen == 14:
        interfaces.c4.output(window)
    if manager.screen == 15:
        interfaces.gc.output(window)

