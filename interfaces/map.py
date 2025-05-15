import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.player


def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/map.png')
    guy= objects.player.Player(410,900,100,100,7,'images/Character.png')



    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        guy.draw(window)
        
    
     
        
    run = True
    while run: 
        guy.move()
        display()
        for event in pygame.event.get():

        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw