import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Coin Collector")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Coin settings
coin_size = 20
coin_pos = [random.randint(0, WIDTH - coin_size), random.randint(0, HEIGHT - coin_size)]

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player_pos[1] += player_speed

    # Draw player
    pygame.draw.rect(
        screen, RED, (player_pos[0], player_pos[1], player_size, player_size)
    )

    # Draw coin
    pygame.draw.circle(
        screen,
        GOLD,
        (coin_pos[0] + coin_size // 2, coin_pos[1] + coin_size // 2),
        coin_size // 2,
    )

    # Collision detection
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    coin_rect = pygame.Rect(coin_pos[0], coin_pos[1], coin_size, coin_size)

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_pos = [
            random.randint(0, WIDTH - coin_size),
            random.randint(0, HEIGHT - coin_size),
        ]

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
