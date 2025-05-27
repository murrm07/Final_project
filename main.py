#Ryan Jeans
#march 3d 2025
#to create space invaders game

import pygame
import mixer
import interfaces.level_1
import manager
import interfaces.title_screen
import interfaces.password
import interfaces.map   
import interfaces.options
pygame.init()
mixer.init()

window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Rockstar")
def play_music(file_path, volume=1.0):
    mixer.music.load(file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()

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
        interfaces.level_1.output(window)
    if manager.screen == 6:
        interfaces.level_1.output(window)
   
        
