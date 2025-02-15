import pygame
import random
import sys

def start(path):
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Block Blast")

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Block properties
    block_width, block_height = 50, 30
    blocks = []

    # Generate random blocks
    for i in range(10):
        x = random.randint(0, WIDTH - block_width)
        y = random.randint(0, HEIGHT // 2)
        blocks.append(pygame.Rect(x, y, block_width, block_height))

    # Player properties
    player = pygame.Rect(WIDTH // 2, HEIGHT - 60, 80, 20)
    player_speed = 5

    # Ball properties
    ball = pygame.Rect(WIDTH // 2, HEIGHT - 80, 20, 20)
    ball_speed = [4, -4]

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Ball movement
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Ball collision with walls
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball.colliderect(player):
            ball_speed[1] = -ball_speed[1]

        # Ball collision with blocks
        for block in blocks[:]:
            if ball.colliderect(block):
                blocks.remove(block)
                ball_speed[1] = -ball_speed[1]

        # Check for game over
        if ball.bottom >= HEIGHT:
            print("Game Over!")
            running = False

        # Draw blocks
        for block in blocks:
            pygame.draw.rect(screen, RED, block)

        # Draw player
        pygame.draw.rect(screen, BLUE, player)

        # Draw ball
        pygame.draw.ellipse(screen, BLACK, ball)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()
