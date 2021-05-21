import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.speed = speed
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((self.life.cols * self.cell_size, self.life.rows * self.cell_size))
        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                x = j * self.cell_size + 1
                y = i * self.cell_size + 1
                a = self.cell_size - 1
                b = self.cell_size - 1
                if self.life.curr_generation[i][j]:
                    pygame.draw.rect(self.screen, pygame.Color("green"), (x, y, a, b))
                else:
                    pygame.draw.rect(self.screen, pygame.Color("white"), (x, y, a, b))

    def run(self) -> None:
        # Copy from previous assignment
        pass
