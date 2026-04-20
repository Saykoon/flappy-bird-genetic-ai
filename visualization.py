import pygame
import pickle
import sys
from config import WIDTH, HEIGHT, FPS, PIPE_WIDTH
from player import Player
from pipe import Pipe
from menu import game_over_screen

def show_best_player(screen, clock, font, background_img):
    try:
        with open("brain/best_brain.pkl", "rb") as f:
            best_brain = pickle.load(f)
    except FileNotFoundError:
        print("Brak zapisanego najlepszego gracza.")
        return

    control_type = "auto"
    bg_x = 0
    bg_speed = 3
    player = Player(brain=best_brain)
    pipes = [Pipe()]

    while player.alive:
        bg_x -= bg_speed
        if bg_x <= -WIDTH:
            bg_x = 0
        screen.blit(background_img, (bg_x, 0))
        screen.blit(background_img, (bg_x + WIDTH, 0))

        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)

        if pipes[-1].x < WIDTH - 200:
            pipes.append(Pipe())
        if pipes[0].x + PIPE_WIDTH < 0:
            pipes.pop(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    control_type = "manual" if control_type == "auto" else "auto"
                if control_type == "manual" and event.key == pygame.K_SPACE:
                    player.jump()

        player.update(pipes, control_type=control_type)
        if any(pipe.collide(player) for pipe in pipes):
            player.alive = False

        player.draw(screen)

        for pipe in pipes:
            if not pipe.passed and player.x > pipe.x + PIPE_WIDTH:
                player.score += 1
                pipe.passed = True

        score_text = font.render(f"Score: {player.score} | Mode: {control_type}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    game_over_screen(screen, clock, FPS, WIDTH, HEIGHT, (255, 255, 255))
