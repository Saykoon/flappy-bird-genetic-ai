# Flappy Bird – Genetic AI

Flappy Bird where the bird is controlled by a genetic algorithm. A population of birds learns to play across generations — no neural network, just simple evolution of a decision weight vector.

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.x-green)

## How it works

Each bird has a "brain" — a vector of 4 weights. Every frame, the bird evaluates:
- vertical distance from the center of the pipe gap
- horizontal distance to the nearest pipe
- current vertical velocity
- bias (constant value 1.0)

The dot product of these inputs with the brain weights decides whether the bird jumps (`> 0.5` → jump).

After each generation ends, the best individuals are crossed over and mutated to form a new population.

## Genetic Algorithm

| Parameter | Value |
|---|---|
| Population size | 30 |
| Selection | Top 6 individuals |
| Crossover | Arithmetic mean of two parents |
| Mutation | Gaussian noise (σ = 0.5 early on, 0.15 after learning) |
| Elitism | Top 2 individuals pass unchanged |

## Fitness Function

Fitness = bird's age (number of frames survived). The number of pipes cleared is tracked separately as the visual score.

## Running

```bash
pip install pygame numpy
python main.py
```

## Menu

- **Train** – starts training a new or loaded population
- **Best** – replays the best bird trained so far
- **Exit** – quit

During training, press `M` to toggle between AI and manual control.

## Saving Progress

| File | Contents |
|---|---|
| `brain/best_brain.pkl` | Weights of the best bird |
| `brain/population.pkl` | Full population from the last generation |
| `brain/statistics.csv` | Score history (generation, best, avg) |

## Project Structure

```
├── main.py          # Main program loop
├── genetic.py       # Genetic algorithm
├── trainer.py       # Single generation simulation
├── player.py        # Bird logic and AI
├── pipe.py          # Pipes
├── menu.py          # Start menu
├── visualization.py # Best bird playback mode
├── config.py        # Constants (screen size, gravity, etc.)
├── brain/           # Saved models
└── img/             # Assets
```

## Requirements

- Python 3.10+
- pygame
- numpy