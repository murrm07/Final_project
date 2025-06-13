import pygame
import manager
import sys
import objects.image
import objects.buttons
from pygame import mixer
mixer.init()
def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/boss_warning.png')
    btn_except = objects.buttons.no_background(100,850,"Arial",35,(235, 64, 52),(98, 52, 235),"Accept Challenge")
    btn_return = objects.buttons.no_background(700,850,"Arial",35,(235, 64, 52),(98, 52, 235),"Return to Map")
   
    
 
 
    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        btn_except.draw(window)
        btn_return.draw(window)
        
    
    run = True
    while run:    
        
        display()
        for event in pygame.event.get():
            if btn_except.update(pygame.mouse.get_pos(),event):
                manager.screen = 10
                run = False
            if btn_return.update(pygame.mouse.get_pos(),event):
                manager.screen = 2
                run = False
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw   