import pygame
import random
from config import WIDTH, HEIGHT, PIPE_GAP, PIPE_WIDTH

class Pipe:
    def __init__(self):
        self.x = WIDTH + 200
        self.gap_y = random.randint(200, HEIGHT - 200)
        self.speed = 3
        self.passed = False
        self.image_top = pygame.image.load("img/pipe_top.png").convert_alpha()
        self.image_bottom = pygame.image.load("img/pipe_bottom.png").convert_alpha()
        self.image_top = pygame.transform.scale(self.image_top, (PIPE_WIDTH, self.gap_y - PIPE_GAP // 2))
        self.image_bottom = pygame.transform.scale(self.image_bottom,(PIPE_WIDTH, HEIGHT - (self.gap_y + PIPE_GAP // 2)))

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image_top, (self.x, 0))
        screen.blit(self.image_bottom, (self.x, self.gap_y + PIPE_GAP // 2))

    def collide(self, player):
        if player.x + player.width > self.x and player.x < self.x + PIPE_WIDTH:
            if player.y < self.gap_y - PIPE_GAP // 2 or player.y + player.height > self.gap_y + PIPE_GAP // 2:
                return True
        return False