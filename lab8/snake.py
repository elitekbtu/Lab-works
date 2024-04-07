import pygame
import random

pygame.init()

apple_size = 20
width = 800
height = 600
snake_speed = 5

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

background = pygame.image.load(r"snake\background.png")

font = pygame.font.SysFont(None, 25)

def display_message(msg, color):
    text = font.render(msg, True, color)
    game_display.blit(text, (200, 250))

def game_loop():
    global snake_speed 
    gamex = False
    gamov = False
    snake_x = 400
    snake_y = 300
    dx = 0
    dy = 0
    snake_length = 1
    snake_list = []
    score = 0
    level = 1

    food_x = random.randrange(0, width - apple_size, apple_size)
    food_y = random.randrange(0, height - apple_size, apple_size)

    while not gamex:
        while gamov == True:
            game_display.fill(color="white")
            display_message("Game Over! Press C to play again or Q to quit", color="black")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gamex = True
                        gamov = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamex = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -apple_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = apple_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -apple_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = apple_size
                    dx = 0

        snake_x += dx
        snake_y += dy

        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            gamov = True

        game_display.blit(background, (0,0))
        pygame.draw.rect(game_display, "red", [food_x, food_y, apple_size, apple_size])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                gamov = True

        for block in snake_list:
            pygame.draw.rect(game_display, "black", [block[0], block[1], apple_size, apple_size])
        scores = font.render(f"SCORE: {len(snake_list)}", True, "black")
        game_display.blit(scores, (5, 5))
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = random.randrange(0, width - apple_size, apple_size)
            food_y = random.randrange(0, height - apple_size, apple_size)
            snake_length += 1
            score += 1

        if score in [3, 4] and level == 1:
            snake_speed += 3
            level += 1
        
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
