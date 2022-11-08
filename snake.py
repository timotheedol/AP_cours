import random
import sys
import pygame

snake = [[10, 15], [11, 15], [12, 15]]
direction = [1, 0]
fruit = [10, 10]

score = 0

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
                print("→")
                direction = [1, 0]

            elif event.key == pygame.K_LEFT:
                print("←")
                direction = [-1, 0]

            elif event.key == pygame.K_UP:
                print("↑")
                direction = [0, -1]

            elif event.key == pygame.K_DOWN:
                print("↓")
                direction = [0, 1]

    screen.fill([0, 0, 0])

    def is_white(i, j):
        if (i + j) % 2 == 0:
            return True
        else:
            return False

    for i in range(30):
        for j in range(30):
            x = i * 20
            y = j * 20
            width = 20
            height = 20
            rect = [x, y, width, height]
            if is_white(i, j):
                color = [255, 255, 255]
                pygame.draw.rect(screen, color, rect)

    head = snake[-1]
    new_head = [head[0] + direction[0], head[1] + direction[1]]

    if new_head == fruit:
        snake.append(new_head)
        fruit = [random.randint(0, 29), random.randint(0, 29)]
        score += 1

    else:
        snake = snake[1:] + [new_head]

    blue = [0, 0, 255]
    rect_ = [fruit[0] * 20, fruit[1] * 20, 20, 20]
    pygame.draw.rect(screen, blue, rect_)

    for x, y in snake:
        rect = [20 * x, 20 * y, 20, 20]
        pygame.draw.rect(screen, [255, 0, 0], rect)

    if snake[-1] in snake[:-1]:
        pygame.quit()
        sys.exit()

    L = [k for k in range(30)]

    if snake[-1][0] not in L or snake[-1][1] not in L:
        pygame.quit()
        sys.exit()

    pygame.display.set_caption(f"🐍 Score: {score}")

    pygame.display.update()
    clock.tick(3)
