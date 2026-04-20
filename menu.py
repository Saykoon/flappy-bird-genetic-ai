import pygame
import pygame.event
import pickle
import os
from config import WIDTH, HEIGHT, WHITE, BLUE
import sys

def draw_menu(screen, font_large, font_small):
    screen.fill(WHITE)
    title = font_large.render("Flappy UWB", True, BLUE)
    option1 = font_small.render("1 - Training AI", True, (0, 0, 0))
    option2 = font_small.render("2 - Play", True, (0, 0, 0))
    option3 = font_small.render("Esc - Exit", True, (0, 0, 0))

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(option1, (WIDTH // 2 - option1.get_width() // 2, 200))
    screen.blit(option2, (WIDTH // 2 - option2.get_width() // 2, 250))
    screen.blit(option3, (WIDTH // 2 - option3.get_width() // 2, 300))
    pygame.display.flip()

def menu_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy UWB")
    font_large = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 32)
    clock = pygame.time.Clock()

    while True:
        draw_menu(screen, font_large, font_small)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    if os.path.exists("brain/population.pkl"):
                        with open("brain/population.pkl", "rb") as f:
                            current_pop = pickle.load(f)
                        with open("population_backup.pkl", "wb") as f2:
                            pickle.dump(current_pop, f2)
                        print("Zapisano kopię zapasową populacji.")
                except Exception as e:
                    print(f"Błąd zapisu populacji: {e}")
                pygame.quit()
                return 'exit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 'train'
                if event.key == pygame.K_2:
                    return 'best'
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return 'exit'
        clock.tick(15)

def game_over_screen(screen, clock, FPS, WIDTH, HEIGHT, WHITE):
    waiting = True
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    while waiting:
        screen.fill(WHITE)
        game_over_text = font_big.render("GAME OVER", True, (255, 0, 0))
        restart_text = font_small.render("Press R to Restart or Esc to Exit", True, (0, 0, 0))

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

pygame.display.set_caption("Flappy UWB")
