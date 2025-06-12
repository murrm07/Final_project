import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.player
import objects.database


def output(window):
    bg= objects.image.still(0,0,1000,1000,'images/map.png')
    guy= objects.player.Player(410,900,100,100,7,'images/Character.png')
    level1 = objects.image.still(0,0,1000,1000,'images/level_1.png')
    level2 = objects.image.still(0,0,1000,1000,'images/level_2.png')
    level3 = objects.image.still(0,0,1000,1000,'images/level_3.png')
    level4 = objects.image.still(0,0,1000,1000,'images/level_4.png')
    
    



    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        guy.draw(window)
        
        
    def collision():
        if  pygame.sprite.collide_mask(guy, level1):
            manager.screen = 11
            print   ("level 1")
            return False
        elif  pygame.sprite.collide_mask(guy, level2):
            if db_connection := objects.database.create_connection("database.db"):
                data = objects.database.select_db(db_connection, "Password", [f"username='{manager.username}'", f"password='{manager.password}'"]).fetchall()
                if data[0][2] >=1:
                    manager.screen = 12
                    print("level 2")
                else:
                    manager.screen = 4
                    print("You need to complete level 1 first!")

            return False
        elif  pygame.sprite.collide_mask(guy, level3):
            if db_connection := objects.database.create_connection("database.db"):
                data = objects.database.select_db(db_connection, "Password", [f"username='{manager.username}'", f"password='{manager.password}'"]).fetchall()
                if data[0][2] >= 2:
                    manager.screen = 13
                    print("level 3")
                else:
                    manager.screen = 4
                    print("You need to complete level 2 first!")
            return False
        elif  pygame.sprite.collide_mask(guy, level4):
            if db_connection := objects.database.create_connection("database.db"):
                data = objects.database.select_db(db_connection, "Password", [f"username='{manager.username}'", f"password='{manager.password}'"]).fetchall()
                if data[0][2] >= 3:
                    manager.screen = 10
                    print("level 4")
                else:
                    manager.screen = 4
                    print("You need to complete level 3 first!")
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