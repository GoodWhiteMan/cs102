import pathlib
import random
import typing as tp
from copy import deepcopy

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        if randomize:
            for i in range(self.rows):
                for j in range(self.cols):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        r, w = cell
        a = self.rows - 1
        b = self.cols - 1
        for i in range(r - 1, r + 2):
            for j in range(w - 1, w + 2):
                if not (0 <= i <= a and 0 <= j <= b) or (i == r and j == w):
                    continue
                neighbours.append(self.curr_generation[i][j])
        return neighbours

    def get_next_generation(self) -> Grid:
        next_grid = self.create_grid(randomize=False)

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                n_neighbours = sum(self.get_neighbours((i, j)))
                is_alive = self.curr_generation[i][j] == 1
                if 2 <= n_neighbours <= 3 and is_alive:
                    next_grid[i][j] = 1
                elif n_neighbours == 3 and not is_alive:
                    next_grid[i][j] = 1
        return next_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations is not None:
            return self.generations <= self.max_generations
        return True

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return not self.curr_generation == self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r") as f:
            grid = [[int(col) for col in row.strip()] for row in f]
        game = GameOfLife((len(grid), len(grid[0])))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            for row in self.curr_generation:
                for col in row:
                    f.write(str(col))
                f.write("\n")
