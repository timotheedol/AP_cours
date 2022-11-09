#Modules
import random
import sys
import pygame

#Constants
WIDTH = 30      # number of cells
HEIGHT = 30     # number of cells
CELL_SIZE = 20  # number of pixels
FPS = 3  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {"background": WHITE, "snake": BLACK, "fruit": RED}

#Helper Function
def exit():
    pygame.quit()
    sys.exit()

def setup():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH*CELL_SIZE, HEIGHT*CELL_SIZE])
    clock = pygame.time.Clock()
    return screen, clock

def wait_for_next_frame(clock):
    clock.tick(FPS)

def draw_frame(screen):
    screen.fill(COLORS['background'])
    rect_ = [fruit[0] * CELL_SIZE, fruit[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, COLORS['fruit'], rect_)

    for x, y in snake:
        rect = [CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE, CELL_SIZE]
        pygame.draw.rect(screen, COLORS['snake'], rect)

    pygame.display.update()

def handle_events():
    global direction
    direction = [0,1]
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            elif event.key == pygame.K_RIGHT:
                print("→")
                direction = RIGHT
            elif event.key == pygame.K_LEFT:
                print("←")
                direction = LEFT
            elif event.key == pygame.K_UP:
                print("↑")
                direction = UP
            elif event.key == pygame.K_DOWN:
                print("↓")
                direction = DOWN

def move_snake():
    global snake
    global fruit
    snake = [[10, 15], [11, 15], [12, 15]]
    fruit = [10, 10]
    score = 0
        
    head = snake[-1]
    new_head = [head[0] + direction[0], head[1] + direction[1]]

    if new_head == fruit:
        snake.append(new_head)
        fruit = [random.randint(0, 29), random.randint(0, 29)]
        score += 1

    else:
        snake = snake[1:] + [new_head]

   #Conditions d'arrêt
    if snake[-1] in snake[:-1]:
        exit()
    
    L = [k for k in range(30)]
    if snake[-1][0] not in L or snake[-1][1] not in L:
        exit()

    #score
    pygame.display.set_caption(f"🐍 Score: {score}")


screen, clock = setup()
while True:
    handle_events()
    move_snake()
    draw_frame(screen)
    wait_for_next_frame(clock)



   #Damier
    '''screen.fill([0, 0, 0])
    def is_white(i, j):
        if (i + j) % 2 == 0:
            return True
        else:
            return False
    for i in range(WIDTH):
        for j in range(HEIGHT):
            x = i * CELL_SIZE
            y = j * CELL_SIZE
            rect = [x, y, CELL_SIZE, CELL_SIZE]
            if is_white(i, j):
                color = [255, 255, 255]
                pygame.draw.rect(screen, color, rect)'''
