import pygame
import manager
import sys
import objects.image
import objects.buttons
from pygame import mixer
mixer.init()
def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/lose.png')
    btn_return = objects.buttons.no_background(300,600,"Arial",35,(235, 64, 52),(98, 52, 235),"Return to map")
    btn_exit = objects.buttons.no_background(300,750,"Arial",35,(235, 64, 52),(98, 52, 235),"Click me to Exit")
    

    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        btn_return.draw(window)
        btn_exit.draw(window)   
       
    run = True
    while run: 
        
        display()
        for event in pygame.event.get():
            if btn_return.update(pygame.mouse.get_pos(),event):
                manager.screen = 2
                run = False
            if btn_exit.update(pygame.mouse.get_pos(),event):
                pygame.quit() 
                sys.exit()
    
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw