import pygame
import pickle
import numpy as np
import sys
from genetic import GeneticAlgorithm
from menu import menu_loop
from visualization import show_best_player
from trainer import evaluate_generation
from config import WIDTH, HEIGHT

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background_img = pygame.image.load("img/background2.jpg").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

def main():
    choice = menu_loop()
    try:
        with open("brain/population.pkl", "rb") as f:
            saved_population = pickle.load(f)
            print("Wczytano zapisaną populację.")
    except FileNotFoundError:
        saved_population = None
        print("Brak zapisanej populacji. Tworzymy nową.")

    try:
        with open("brain/best_brain.pkl", "rb") as f:
            best_brain_loaded = pickle.load(f)
            print("Wczytano najlepszego gracza z pliku.")
    except FileNotFoundError:
        best_brain_loaded = None
        print("Brak zapisanego gracza. Trening od zera.")

    if choice == 'best':
        while True:
            show_best_player(screen, clock, font, background_img)
    elif choice == 'exit':
        return

    algo = GeneticAlgorithm(population_size=30)
    if saved_population:
        algo.population = saved_population
    if best_brain_loaded is not None:
        for i in range(len(algo.population)):
            algo.population[i] = best_brain_loaded + np.random.normal(0, 0.05, size=best_brain_loaded.shape)

    generation = 1

    while True:
        scores, pipe_scores, brains = evaluate_generation(
            algo.population, screen, clock, background_img, font, generation
        )

        gen_best = max(scores)
        if gen_best > algo.best_score:
            algo.best_score = gen_best
            algo.best_brain = brains[scores.index(gen_best)]
            algo.save_best()

        algo.evolve(scores, generation)
        algo.save_population()
        generation += 1

        best_pipe_score = max(pipe_scores)
        avg_pipe_score = sum(pipe_scores) / len(pipe_scores)

        print(f"Generacja {generation} | Najlepszy wynik (rury): {best_pipe_score} | Średni: {avg_pipe_score:.2f}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if best_brain is not None:
        algo.best_brain = best_brain
        algo.save_best()

    with open("brain/population.pkl", "wb") as f:
        pickle.dump(algo.population, f)
        print("Zapisano populację do pliku.")

    pygame.quit()

if __name__ == "__main__":
    main()