import pygame
import random

# Initialisiere pygame
pygame.init()

# Bildschirmgröße
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Spielgeschwindigkeit
clock = pygame.time.Clock()

# Spieler-Einstellungen
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size
player_speed = 5

# Block-Einstellungen
block_size = 50
block_list = []

# Punkte
score = 0

# Erstelle Blöcke an zufälligen Positionen
def create_blocks():
    for i in range(5):
        x = random.randint(0, SCREEN_WIDTH - block_size)
        y = random.randint(-500, -50)
        block_list.append([x, y])

# Zeichne den Spieler
def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_size, player_size))

# Zeichne die Blöcke
def draw_blocks(block_list):
    for block in block_list:
        pygame.draw.rect(screen, BLUE, (block[0], block[1], block_size, block_size))

# Überprüfe Kollision zwischen Spieler und Blöcken
def check_collision(player_x, player_y, block_list):
    global score
    for block in block_list:
        if (player_x < block[0] + block_size and
            player_x + player_size > block[0] and
            player_y < block[1] + block_size and
            player_y + player_size > block[1]):
            block_list.remove(block)
            score += 1

# Spielhauptschleife
def game_loop():
    global player_x, player_y
    game_over = False

    # Blöcke erstellen
    create_blocks()

    # Hauptschleife
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Spielerbewegung
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
            player_y += player_speed

        # Aktualisiere Blockpositionen
        for block in block_list:
            block[1] += 3
            if block[1] > SCREEN_HEIGHT:
                block_list.remove(block)
                new_x = random.randint(0, SCREEN_WIDTH - block_size)
                new_y = random.randint(-500, -50)
                block_list.append([new_x, new_y])

        # Kollisionsprüfung
        check_collision(player_x, player_y, block_list)

        # Bildschirm füllen
        screen.fill(WHITE)

        # Zeichne Spieler und Blöcke
        draw_player(player_x, player_y)
        draw_blocks(block_list)

        # Punkte anzeigen
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Aktualisiere Bildschirm
        pygame.display.update()

        # Frame-Geschwindigkeit
        clock.tick(60)

    pygame.quit()

# Starte das Spiel
game_loop()
