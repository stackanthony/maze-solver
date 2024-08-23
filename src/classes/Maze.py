from src.classes.Cell import Cell
from src.classes.Window import Window
from typing import Optional
import time


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Optional[Window] = None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

    def _create_cells(self):
        cells: list[list[Cell]] = []

        for _ in range(self.num_rows):
            col_cells: list[Cell] = []
            for _ in range(self.num_cols):
                if self.win:
                    col_cells.append(Cell(_win=self.win))
                    continue

                col_cells.append(Cell())
            cells.append(col_cells)

        self._cells = cells

        for i in range(len(cells)):
            for j in range(len(cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        cur_cell: Cell = self._cells[i][j]

        cur_cell._x1 = self.x1 + (i * self.cell_size_x)
        cur_cell._x2 = self.x1 + self.cell_size_x + (i * self.cell_size_x)

        cur_cell._y1 = self.y1 + (j * self.cell_size_y)
        cur_cell._y2 = self.y1 + self.cell_size_y + (j * self.cell_size_y)

        cur_cell.draw('red')
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.1)
