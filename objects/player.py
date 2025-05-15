import pygame
import sys
import objects.image
import manager

class Player(objects.image.still):
    def __init__(self, x, y,width,height,speed,image_to_use):
        super().__init__(x, y,width,height,image_to_use)  
        self.speed = speed
        
    def move(self):   
        key_input = pygame.key.get_pressed()
        moveX = (key_input[pygame.K_RIGHT] - key_input[pygame.K_LEFT]) * self.speed + (key_input[pygame.K_d] - key_input[pygame.K_a]) * self.speed
        moveY = (key_input[pygame.K_DOWN] - key_input[pygame.K_UP]) * self.speed + (key_input[pygame.K_s] - key_input[pygame.K_w]) * self.speed
        
        self.rect.x += moveX
        self.rect.y += moveY
        # Check for collision with the window boundaries
        if self.rect.top < 0:       
            self.rect.top = 0           
        if self.rect.bottom > manager.WINDOW_HEIGHT:    
            self.rect.bottom = manager.WINDOW_HEIGHT
        if self.rect.bottom > 1000:
            self.rect.bottom = 1000
        if self.rect.top > manager.WINDOW_HEIGHT:
            self.rect.top = manager.WINDOW_HEIGHT
       
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > manager.WINDOW_WIDTH:
            self.rect.right = manager.WINDOW_HEIGHT
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.left > manager.WINDOW_WIDTH:
            self.rect.left = manager.WINDOW_HEIGHT
        