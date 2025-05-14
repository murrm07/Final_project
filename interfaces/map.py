import pygame
import manager
import sys
import objects.image
import objects.buttons


def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/map.png')



    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
    
     
        
    run = True
    while run: 
        display()
        for event in pygame.event.get():
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw