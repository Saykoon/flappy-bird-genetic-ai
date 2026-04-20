import pygame
import sys
from player import Player
from pipe import Pipe
from config import WIDTH, FPS, PIPE_WIDTH

def evaluate_generation(brains, screen, clock, background_img, font, generation):
    players = [Player(brain=brain) for brain in brains]
    pipes = [Pipe()]
    generation_score = [0] * len(players)
    control_type = "auto"
    bg_x = 0
    bg_speed = 3

    while any(player.alive for player in players):
        # TŁO
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
                    print(f"Switched to {control_type} mode.")

        for i, player in enumerate(players):
            if player.alive:
                player.update(pipes, control_type=control_type)
                if any(pipe.collide(player) for pipe in pipes):
                    player.alive = False
                else:
                    player.draw(screen)

                    for pipe in pipes:
                        if not pipe.passed and player.x > pipe.x + PIPE_WIDTH:
                            player.score += 1
                            pipe.passed = True

        text = font.render(f"Alive: {sum(p.alive for p in players)} | Mode: {control_type}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        gen_text = font.render(f"Generacja: {generation}", True, (0, 0, 0))
        screen.blit(gen_text, (10, 30))

        if players:
            best_score = max(p.score for p in players)
            score_text = font.render(f"Najlepszy wynik: {best_score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)

    generation_score = [0] * len(players)  # <- do uczenia (age)
    generation_pipe_score = [0] * len(players)

    for idx, player in enumerate(players):
        generation_score[idx] = player.age
        generation_pipe_score[idx] = player.score

    return generation_score, generation_pipe_score, brains