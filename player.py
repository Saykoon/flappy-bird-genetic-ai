import numpy as np
import pygame
from config import GRAVITY, JUMP_STRENGTH, HEIGHT, PIPE_WIDTH, WIDTH

class Player:
    def __init__(self, brain=None):
        self.x = 50
        self.y = HEIGHT // 2
        self.vel = 0
        self.width = 50
        self.height = 50
        self.score = 0
        self.brain = np.array(brain) if brain is not None else np.random.uniform(-1, 1, 4)
        self.alive = True
        self.image = pygame.image.load("img/uwb50x50.png").convert_alpha()
        self.age = 0

    def update(self, pipes, control_type="manual"):
        if control_type == "auto":
            self.ai_control(pipes)
        self.vel += GRAVITY
        self.y += self.vel
        if self.y > HEIGHT or self.y < 0:
            self.alive = False
        self.age += 1

    def jump(self):
        self.vel = JUMP_STRENGTH

    def ai_control(self, pipes):
        pipe = next((p for p in pipes if p.x + PIPE_WIDTH > self.x), pipes[0])

        vertical_diff = (self.y - pipe.gap_y) / HEIGHT
        horizontal_dist = (pipe.x - self.x) / WIDTH
        velocity_norm = self.vel / 10.0
        bias = 1.0

        inputs = np.array([vertical_diff, horizontal_dist, velocity_norm, bias])
        total = np.dot(self.brain, inputs)

        if total > 0.5:
            self.jump()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))