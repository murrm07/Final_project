import pygame
import manager
import sys
import objects.image
import objects.buttons
from pygame import mixer
mixer.init()
def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/credit.png')
    btn_return = objects.buttons.no_background(700,850,"Arial",35,(235, 64, 52),(98, 52, 235),"Click to Return")
    
    
 
 
    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        btn_return.draw(window)
         
    
    run = True
    while run:    
        
        display()
        for event in pygame.event.get():
            if btn_return.update(pygame.mouse.get_pos(),event):
                manager.screen = 0
                run = False
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw