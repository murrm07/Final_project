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
    objects.database.create_table(db_connection,"Password",["username TEXT", "password INTEGER","level INTEGER"])
    font = pygame.font.SysFont("Arial", 30)
    txt_username = objects.text.input(250,200,500,100,'Consolas',30,(0,0,0),(255,255,255))
    txt_password = objects.text.input(250,450,500,100,'Consolas',30,(0,0,0),(255,255,255))
    btn_create = objects.buttons.no_background(100,700,"Arial",24,(235, 64, 52),(98, 52, 235),"Create Account")
    btn_login = objects.buttons.no_background(600,700,"Arial",24,(235, 64, 52),(98, 52, 235),"Login")
    btn_exit = objects.buttons.no_background(800,950,"Arial",24,(235, 64, 52),(98, 52, 235),"Click me to Exit")
    txt_group = pygame.sprite.Group()
    txt_group.add(txt_username, txt_password)
    
    def display():
        window.fill((0,0,0)) #White background
        bg.draw(window)
        txt_group.draw(window)
        btn_create.draw(window)
        btn_login.draw(window)
        btn_exit.draw(window)
        window.blit(font.render("Username", True, (0, 0, 0)), (txt_username.rect.x, txt_username.rect.y - 30))
        window.blit(font.render("Password", True, (0, 0, 0)), (txt_password.rect.x, txt_password.rect.y - 30))
        
       
    
     
        
    run = True
    while run: 
        display()
        for event in pygame.event.get():
            txt_group.update(pygame.mouse.get_pos(), event)
            if btn_create.update(pygame.mouse.get_pos(),event):
                objects.database.insert_db(db_connection, "Password", ["username","Password"],[txt_username.text,txt_password.text])
                print("Data inserted successfully")
                manager.screen = 2
                run = False
            if btn_login.update(pygame.mouse.get_pos(),event):
                data = objects.database.select_db(db_connection, "Password", [f"username='{txt_username.text}'", f"password='{txt_password.text}'"]).fetchall()
                if data:
                    print("Login successful")
                    manager.screen = 2
                    run = False
                else:
                    print("Login failed")
            if btn_exit.update(pygame.mouse.get_pos(),event):
                pygame.quit() 
                sys.exit()
                
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw