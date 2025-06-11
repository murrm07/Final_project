import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.player
import objects.database



def output(window):
    stage = objects.player.stage(0,0,1000,1000)
    guy= objects.player.Player(100,600,100,100,7,'images/Character.png')
    drums = objects.player.enemy(750,600,100,100,3,'images/drumms.png')
    notes = pygame.sprite.Group()
    enemy_notes = pygame.sprite.Group()
    powernotes = pygame.sprite.Group()
    db_connection = objects.database.create_connection("database.db")
    shoot_timer = 25
    enemy_timer = 40
    power_shoot_timer = 100


    def display():
        window.fill((0,0,0)) #White background
        stage.draw(window)
        guy.draw(window)
        drums.draw(window)
        notes.draw(window)
        enemy_notes.draw(window)
        powernotes.draw(window)

    run = True
    while run: 
        guy.fight()
        drums.update()
        notes.update()
        enemy_notes.update()
        powernotes.update()
        shoot_timer -= 1
        enemy_timer -= 1
        power_shoot_timer -= 1
        
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_1] and shoot_timer <= 0:
            shoot_timer = 25
            notes.add(objects.player.shooter(guy.rect.x,guy.rect.y,50,50, 10,'images/note.png'))
            
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE] and power_shoot_timer <= 0:
            print("power")
            power_shoot_timer = 100
            powernotes.add(objects.player.power(guy.rect.x,guy.rect.y,50,50, 10,'images/note_2.png'))


        if notes:
            for note in notes:
                remove = False
                if note.rect.x > manager.WINDOW_WIDTH:
                    remove = True
                if pygame.sprite.collide_rect(drums,note):
                    remove = True
                    stage.lives()
                    print(stage.live)
                if remove:
                    notes.remove(note)
                    
        if powernotes:
            for note in powernotes:
                remove = False
                if note.rect.x > manager.WINDOW_WIDTH:
                    remove = True
                if pygame.sprite.collide_rect(drums,note):
                    remove = True
                    stage.lives()
                    stage.lives()
                    print(stage.live)
                if remove:
                    powernotes.remove(note)
        if stage.live <= 0:
            manager.screen = 5
            run = False
            db_connection = objects.database.create_connection("database.db")
            objects.database.update_db(db_connection,"Password",["level=2"],f"id={manager.id}")
            

        if enemy_timer <= 0:
            enemy_notes.add(objects.player.enemy_shooter(drums.rect.x,drums.rect.y,50,50, 10,'images/note.png'))
            enemy_timer = 50
        if enemy_notes:
            for note in enemy_notes:
                remove = False
                if note.rect.x < 0:
                    remove = True
                if pygame.sprite.collide_rect(guy,note):
                    remove = True
                    guy.alive = False
                if remove:
                    enemy_notes.remove(note)
        if not guy.alive:
            manager.screen = 6
            run = False
        
     
        display()
        for event in pygame.event.get():

        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw
