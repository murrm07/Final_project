import pygame
import manager
import sys
import objects.image
import objects.buttons
from pygame import mixer
mixer.init()
def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/title_screen.png')
    btn_start = objects.buttons.no_background(100,850,"Arial",24,(235, 64, 52),(98, 52, 235),"Start Game")
    btn_exit = objects.buttons.no_background(700,850,"Arial",24,(235, 64, 52),(98, 52, 235),"Click me to Exit")
    btn_options = objects.buttons.no_background(425,850,"Arial",24,(235, 64, 52),(98, 52, 235),"options")
    btn_story = objects.buttons.no_background(425,850,"Arial",24,(235, 64, 52),(98, 52, 235),"story plot")
    btn_credits = objects.buttons.no_background(425,850,"Arial",24,(235, 64, 52),(98, 52, 235),"credits")
    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        btn_start.draw(window)
        btn_exit.draw(window)   
        btn_options.draw(window)
        btn_story.draw(window)
    def play_music(file_path, volume=1.0):
        mixer.music.load(file_path)
        mixer.music.set_volume(volume)
        mixer.music.play()
    play_music('music/output.ogg')    
    run = True
    while run: 
        
        display()
        for event in pygame.event.get():
            if btn_start.update(pygame.mouse.get_pos(),event):
                manager.screen = 1
                run = False
            if btn_options.update(pygame.mouse.get_pos(),event):
                manager.screen = 4
                run=False
            if btn_story.update(pygame.mouse.get_pos(),event):
                manager.screen = 4
                run=False
            if btn_exit.update(pygame.mouse.get_pos(),event):
                pygame.quit() 
                sys.exit()
    
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw