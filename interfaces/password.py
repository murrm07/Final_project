import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.database
import objects.text


def output(window):
    bg = objects.image.still(0,0,1000,1000,'images/password.png')
    db_connection = objects.database.create_connection("database.db")
    objects.database.create_table(db_connection,"Password",["username TEXT", "password INTEGER"])
    txt_movie = objects.text.input(250,200,500,100,'Consolas',30,(0,0,0),(255,255,255))
    txt_movie_year = objects.text.input(250,450,500,100,'Consolas',30,(0,0,0),(255,255,255))
    txt_group = pygame.sprite.Group()
    txt_group.add(txt_movie, txt_movie_year)


    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        txt_group.draw(window)
        
       
    
     
        
    run = True
    while run: 
        display()
        for event in pygame.event.get():
            txt_group.update(pygame.mouse.get_pos(), event)
    
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw