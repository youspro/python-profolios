import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Snake settings
SNAKE_SIZE = 20
SNAKE_SPEED = 20

# Food settings
FOOD_SIZE = 20

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fun Snake Game')

clock = pygame.time.Clock()

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE])

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over", True, BLUE)
    screen.blit(text, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3])
    pygame.display.update()
    pygame.time.wait(2000)

def game():
    snake_list = []
    snake_length = 1

    # Initial snake position
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2

    # Initial snake movement
    snake_dx = 0
    snake_dy = 0

    # Food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - FOOD_SIZE) / FOOD_SIZE) * FOOD_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - FOOD_SIZE) / FOOD_SIZE) * FOOD_SIZE

    running = True
    game_over_flag = False

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_dx = -SNAKE_SPEED
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake_dx = SNAKE_SPEED
                    snake_dy = 0
                elif event.key == pygame.K_UP:
                    snake_dy = -SNAKE_SPEED
                    snake_dx = 0
                elif event.key == pygame.K_DOWN:
                    snake_dy = SNAKE_SPEED
                    snake_dx = 0

        snake_x += snake_dx
        snake_y += snake_dy

        if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
            game_over_flag = True

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over_flag = True

        if game_over_flag:
            game_over()
            break

        draw_snake(snake_list)
        draw_food([food_x, food_y])

        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            food_x = round(random.randrange(0, SCREEN_WIDTH - FOOD_SIZE) / FOOD_SIZE) * FOOD_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - FOOD_SIZE) / FOOD_SIZE) * FOOD_SIZE

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    quit()

if __name__ == '__main__':
    game()