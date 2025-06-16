import pygame
import manager
import sys
import objects.image
import objects.buttons



def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/options_screen.png')
    btn_return = objects.buttons.no_background(650,350,"Arial",40,(235, 64, 52),(98, 52, 235),"Click to Return")
    btn_story =  objects.buttons.no_background(650,300,"Arial",40,(235, 64, 52),(98, 52, 235),"Story Plot")
    btn_credit = objects.buttons.no_background(650,250,"Arial",40,(235, 64, 52),(98, 52, 235),"Credits")
    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window) 
        btn_return.draw(window)
        btn_story.draw(window)
        btn_credit.draw(window)
    run = True
    while run: 
        display()
        for event in pygame.event.get():
            if btn_return.update(pygame.mouse.get_pos(),event):
                manager.screen = 0
                run = False
            if btn_story.update(pygame.mouse.get_pos(),event):
                manager.screen = 9
                run = False
            if  btn_credit.update(pygame.mouse.get_pos(),event):
                manager.screen = 16
                run = False
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw