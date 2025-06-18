import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.player
import objects.database



def output(window):
    back = objects.player.back(0,0,1000,1000)
    guy= objects.player.Player(100,600,100,100,7,'images/Character.png')
    drums = objects.player.enemy(750,600,100,100,9,'images/boombox.png')
    notes = pygame.sprite.Group()
    enemy_notes = pygame.sprite.Group()
    powernotes = pygame.sprite.Group()
    db_connection = objects.database.create_connection("database.db")
    multishot = pygame.sprite.Group()
    heavy_notes = pygame.sprite.Group()
    shoot_timer = 25
    enemy_timer = 25
    power_shoot_timer = 80
    multishot_timer = 15
    heavy_timer = 100
    note_counter = 0

    def display():
        window.fill((0,0,0)) #White background
        back.draw(window)
        guy.draw(window)
        drums.draw(window)
        notes.draw(window)
        enemy_notes.draw(window)
        powernotes.draw(window)
        multishot.draw(window)
        heavy_notes.draw(window)

    run = True
    while run: 
        guy.fight()
        drums.update()
        notes.update()
        enemy_notes.update()
        powernotes.update()
        multishot.update()
        heavy_notes.update()
        shoot_timer -= 1
        enemy_timer -= 1
        power_shoot_timer -= 1
        multishot_timer -= 1
        heavy_timer -= 1

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_1] and shoot_timer <= 0:
            shoot_timer = 25
            notes.add(objects.player.shooter(guy.rect.x,guy.rect.y,50,50, 10,'images/note.png'))

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE] and power_shoot_timer <= 0:
            print("power")
            power_shoot_timer = 80
            powernotes.add(objects.player.power(guy.rect.x,guy.rect.y,50,50, 10,'images/note_2.png'))
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_2] and multishot_timer <= 0 and len(multishot) < 3:
            multishot_timer = 15
            multishot.add(objects.player.multishooter(guy.rect.x,guy.rect.y,50,50, 10,'images/note_3.png'))
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_3] and heavy_timer <= 0:
            heavy_timer = 100
            heavy_notes = pygame.sprite.Group()
            heavy_notes.add(objects.player.heavy(guy.rect.x,guy.rect.y,50,50, 10,'images/note_4.png'))


        if notes:
            for note in notes:
                remove = False
                if note.rect.x > manager.WINDOW_WIDTH:
                    remove = True
                if pygame.sprite.collide_rect(drums,note):
                    remove = True
                    back.lives()
                    print(back.live)
                if remove:
                    notes.remove(note)
                    
        if powernotes:
            for note in powernotes:
                remove = False
                if note.rect.x > manager.WINDOW_WIDTH:
                    remove = True
                if pygame.sprite.collide_rect(drums,note):
                    remove = True
                    back.lives()
                    back.lives()
                    print(back.live)
                if remove:
                    powernotes.remove(note)
        
        if multishot:
            for note in multishot:
                remove = False
                if note.rect.x > manager.WINDOW_WIDTH:
                    remove = True
                if pygame.sprite.collide_rect(drums,note):
                    remove = True
                    back.lives()
                    print(back.live)
                if remove:
                    multishot.remove(note)
                note_counter += 1
                    
        if heavy_notes:
            for note in heavy_notes:
                remove = False
                if note.rect.x > manager.WINDOW_WIDTH:
                    remove = True
                if pygame.sprite.collide_rect(drums,note):
                    remove = True
                    back.lives()
                    back.lives()
                    back.lives()
                    back.lives()
                    print(back.live)
                if remove:
                    heavy_notes.remove(note)
        if back.live <= 0:
            manager.screen = 17
            run = False
            db_connection = objects.database.create_connection("database.db")
            manager.level = 4
            objects.database.update_db(db_connection,"Password",[f"level={manager.level}"], f"id={manager.id}")
            

        if enemy_timer <= 0:
            enemy_notes.add(objects.player.enemy_shooter(drums.rect.x,drums.rect.y,50,50, 15,'images/note.png'))
            enemy_timer = 25
        if enemy_notes:
            for note in enemy_notes:
                remove = False
                if note.rect.x < 0:
                    remove = True
               # if pygame.sprite.collide_rect(guy,note):
                   # remove = True
                   # guy.alive = False
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
