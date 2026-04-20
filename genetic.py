import numpy as np
import pickle
import random
import csv
import os

class GeneticAlgorithm:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = [self.create_individual() for _ in range(population_size)]
        self.best_brain = None
        self.best_score = 0
        self.stats_path = "brain/statistics.csv"

        os.makedirs("brain", exist_ok=True)
        with open(self.stats_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Generation", "BestScore", "AverageScore"])

    def create_individual(self):
        return np.random.uniform(-1, 1, 4)

    def mutate(self, individual):
        mutation_strength = 0.5 if self.best_score < 3 else 0.15
        return individual + np.random.normal(0, mutation_strength, size=individual.shape)

    def crossover(self, parent1, parent2):
        return (parent1 + parent2) / 2

    def select_best(self, scores, top_n=6):
        top_indices = np.argsort(scores)[-top_n:]
        best_score = scores[top_indices[-1]]
        if best_score > self.best_score:
            self.best_score = best_score
            self.best_brain = self.population[top_indices[-1]]
            self.save_best()
        return [self.population[i] for i in top_indices]

    def evolve(self, scores, generation):
        best = self.select_best(scores)
        new_population = best[:2]

        while len(new_population) < self.population_size:
            p1, p2 = random.sample(best, 2)
            child = self.crossover(p1, p2)
            child = self.mutate(child)
            new_population.append(child)

        self.population = new_population
        self.save_population()

        avg_score = sum(scores) / len(scores)
        with open(self.stats_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([generation, self.best_score, avg_score])

    def save_best(self):
        with open("brain/best_brain.pkl", "wb") as f:
            pickle.dump(self.best_brain, f)

    def save_population(self):
        with open("brain/population.pkl", "wb") as f:
            pickle.dump(self.population, f)

    def load_best(self):
        try:
            with open("brain/best_brain.pkl", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None