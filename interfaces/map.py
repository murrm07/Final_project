import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.player


def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/map.png')
    guy= objects.player.Player(410,900,100,100,7,'images/Character.png')
    level1 = objects.image.still(0,0,1000,1000,'images/level_1.png')
    level2 = objects.image.still(0,0,1000,1000,'images/level_2.png')
    level3 = objects.image.still(0,0,1000,1000,'images/level_3.png')
    
    



    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        guy.draw(window)
        
        
    def collision():
        if  pygame.sprite.collide_mask(guy, level1):
            manager.screen = 3
            print   ("level 1")
            return False
        elif  pygame.sprite.collide_mask(guy, level2):
            manager.screen = 4
            return False
        elif  pygame.sprite.collide_mask(guy, level3):
            manager.screen = 5
            return False
        else:
            return True
            
    run = True
    while run:
        run = collision()
        guy.move()
        display()
        for event in pygame.event.get():

        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw