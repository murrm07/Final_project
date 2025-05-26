import pygame
import manager
import sys
import objects.image
import objects.buttons
import objects.player
import objects.database



def output(window):
    stage = objects.player.background(0,0,1000,1000)
    guy= objects.player.Player(100,600,100,100,7,'images/Character.png')
    drums = objects.player.enemy(750,600,100,100,3,'images/drumms.png')
    note = objects.player.shooter(750,600,10,10,10,'images/note.png')
    notes = pygame.sprite.Group()
    shoot_timer = 25
    enemy_timer = 50
    
    




    def display():
        window.fill((0,0,0)) #White background
        stage.draw(window)
        guy.draw(window)
        drums.draw(window)
        notes.draw(window)

       
    run = True
    while run: 
        guy.fight()
        drums.update()
        notes.update()
        shoot_timer -= 1
        enemy_timer -= 1
        
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_1] and shoot_timer <= 0:
                shoot_timer = 25
                notes.add(objects.player.shooter(guy.rect.x,guy.rect.y,50,50, 10,'images/note.png'))
        if notes:
            for note in notes:
                if note.rect.x > manager.WINDOW_WIDTH:
                    notes.remove(note)
                    
        if enemy_timer <= 0:
            notes.add(objects.player.enemy_shooter(drums.rect.x,drums.rect.y,50,50, 10,'images/note.png'))
            enemy_timer = 50
            if notes:
                for note in notes:
                    if note.rect.x < 0:
                        notes.remove(note)
    
        if pygame.sprite.collide_rect(drums,note):
            print("You hit the drums!")
            notes.remove(note)
            stage.lives()
                
                
                
        display()
        for event in pygame.event.get():

        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
  
       
        pygame.display.flip() #update the display
        manager.fpsClock.tick(manager.fps) #speed of redraw