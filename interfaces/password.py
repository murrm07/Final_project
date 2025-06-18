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
        window.blit(font.render("Please create an account or login", True, (0, 0, 0)), (250, 100))
        
       
    
     
        
    run = True
    while run: 
        display()
        for event in pygame.event.get():
            txt_group.update(pygame.mouse.get_pos(), event)
            if btn_create.update(pygame.mouse.get_pos(),event):
                if objects.database.select_db(db_connection, "Password", [f"username='{txt_username.text}'"]).fetchall():
                    window.blit(font.render("Username already exists", True, (255, 0, 0)), (250, 600))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    break
                    
                if not txt_username.text or not txt_password.text:
                    window.blit(font.render("Please fill in all fields", True, (255, 0, 0)), (250, 600))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    break
                objects.database.insert_db(db_connection, "Password", ["username","Password","level"],[txt_username.text,txt_password.text,0])
                window.blit(font.render("Account created successfully", True, (0, 255, 0)), (250, 600))
                pygame.display.update()
                data = objects.database.select_db(db_connection, "Password", [f"username='{txt_username.text}'", f"password='{txt_password.text}'"]).fetchall()
                manager.screen = 2
                manager.username = txt_username.text
                manager.password = txt_password.text
                manager.level = data[0][3]
                manager.id = data[0][0] 
                run = False
            if btn_login.update(pygame.mouse.get_pos(),event):
                data = objects.database.select_db(db_connection, "Password", [f"username='{txt_username.text}'", f"password='{txt_password.text}'"]).fetchall()
                if data:
                    window.blit(font.render("Login successful", True, (0, 255, 0)), (250, 600))
                    manager.screen = 2
                    manager.username = txt_username.text
                    manager.password = txt_password.text
                    manager.level = data[0][3]
                    manager.id = data[0][0] 
                    run = False
                else:
                    window.blit(font.render("Login failed", True, (255, 0, 0)), (250, 600))
                    pygame.display.update()
                    pygame.time.delay(3000)
            if btn_exit.update(pygame.mouse.get_pos(),event):
                pygame.quit() 
                sys.exit()
            
                
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw