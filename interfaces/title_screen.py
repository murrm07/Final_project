import pygame
import manager
import sys
import objects.image
import objects.buttons


def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/title_screen.png')
    btn_start = objects.buttons.no_background(100,850,"Arial",24,(235, 64, 52),(98, 52, 235),"Start Game")
    btn_exit = objects.buttons.no_background(100,700,"Arial",24,(235, 64, 52),(98, 52, 235),"Click me to Exit")


    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        btn_start.draw(window)
        btn_exit.draw(window)   
    
     
        
    run = True
    while run: 
        display()
        for event in pygame.event.get():
            if btn_start.update(pygame.mouse.get_pos(),event):
                manager.screen = 1
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