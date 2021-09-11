import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.clear()

        height, width = screen.getmaxyx()
        line = ""

        for row in range(height):
            for col in range(width):
                if row == 0 or row == height - 1:
                    if col == 0 or col == width - 1:
                        line += "+"
                    else:
                        line += "-"
                elif row > 0 & row < (height - 1):
                    if col == 0 or col == width - 1:
                        line += "|"
                    else:
                        line += " "
            try:
                screen.addstr(line)
            except curses.error:
                pass
            line = ""

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        height, width = screen.getmaxyx()
        x = (width - self.life.cols) // 2
        y = (height - self.life.rows) // 2

        for row_num, row in enumerate(self.life.curr_generation):
            for col_num, col in enumerate(row):
                if col:
                    try:
                        screen.addstr(row_num + y, col_num + x, "*")
                    except curses.error:
                        pass

    def run(self) -> None:
        screen = curses.initscr()
        curses.wrapper(self.draw_borders)
        while self.life.is_changing and not self.life.is_max_generations_exceeded:
            self.life.step()
            self.draw_borders(screen)
        curses.endwin()
