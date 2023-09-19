import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Snake settings
snake_block_size = 20
snake_speed = 15

# Font settings
font = pygame.font.SysFont(None, 36)

# Function to display text on screen
def display_text(text, color, x, y):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to display the score
def display_score(score):
    display_text("Score: " + str(score), white, 10, 10)

# Function to display the top 10 scores
def display_ranking(ranking):
    display_text("Top 10 Scores", white, screen_width // 2 - 100, 100)

    for i, score in enumerate(ranking, start=1):
        display_text(f"{i}. {score}", white, screen_width // 2 - 50, 100 + i * 30)

# Function to draw the snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block_size, snake_block_size])

# Function to run the game
def run_game():
    game_over = False
    game_end = False

    # Initial position and movement of the snake
    x1 = screen_width // 2
    y1 = screen_height // 2
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_body = []
    length_of_snake = 1

    # Position of the food
    food_x = round(random.randrange(0, screen_width - snake_block_size) / 20) * 20
    food_y = round(random.randrange(0, screen_height - snake_block_size) / 20) * 20

    while not game_over:
        while game_end:
            screen.fill(black)
            display_text("Press Q-Quit or C-Play Again", white, screen_width // 2 - 180, screen_height // 2 - 18)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block_size:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block_size:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block_size:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block_size:
                    y1_change = snake_block_size
                    x1_change = 0

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Check if the snake hits the boundaries
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_end = True

        # Create snake head and body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check if the snake hits itself
        for block in snake_body[:-1]:
            if block == snake_head:
                game_end = True

        # Draw the snake
        screen.fill(black)
        draw_snake(snake_body)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block_size, snake_block_size])
        display_score(length_of_snake - 1)
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block_size) / 20) * 20
            food_y = round(random.randrange(0, screen_height - snake_block_size) / 20) * 20
            length_of_snake += 1

        # Set the game speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

# Run the game
run_game()
