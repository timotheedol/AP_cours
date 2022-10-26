import random
import sys
import pygame

snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]

direction = [1, 0]

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        
            elif event.key == pygame.K_RIGHT:
                
        
            elif event.key == pygame.K_LEFT:
                print('<-')
        
            elif event.key == pygame.K_UP:
                print('haut')
                
            elif event.key == pygame.K_DOWN:
                print('bas')
    
    screen.fill([0,0,0])
    

    def is_white(i,j):
        if (i+j) % 2==0:
            return True
        else:
            return False

    for i in range(30):
        for j in range(30):
            x = i*20
            y = j*20
            width = 20
            height = 20
            rect = [x, y, width, height]
            if is_white(i,j):
                color = [255,255,255]
                pygame.draw.rect(screen, color, rect)

    for x,y in snake:
        rect = [20*x,20*y,20,20]
        pygame.draw.rect(screen, [255,0,0], rect)

           
    pygame.display.update()
    clock.tick(1)
    
