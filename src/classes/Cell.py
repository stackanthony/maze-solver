from src.classes.Line import Line
from src.classes.Point import Point
from src.classes.Window import Window


class Cell:
    def __init__(
        self,
        has_left_wall: bool = True,
        has_right_wall: bool = True,
        has_top_wall: bool = True,
        has_bottom_wall: bool = True,
        _x1: float = 0.0,
        _x2: float = 0.0,
        _y1: float = 0.0,
        _y2: float = 0.0,
        _win: Window = Window(),
    ) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win

    def __str__(self) -> str:
        return f'Cell({self.has_left_wall}, {self.has_right_wall}, {self.has_top_wall}, {self.has_bottom_wall}, {self._x1}, {self._x2}, {self._y1}, {self._y2})'

    def draw(self, fill_color: str):
        if self.has_left_wall:
            left_wall = Line(
                Point(self._x1, self._y1), Point(self._x1, self._y2)
            )
            self._win.draw_line(left_wall, fill_color)

        if self.has_right_wall:
            right_wall = Line(
                Point(self._x2, self._y1), Point(self._x2, self._y2)
            )
            self._win.draw_line(right_wall, fill_color)

        if self.has_top_wall:
            top_wall = Line(
                Point(self._x1, self._y2), Point(self._x2, self._y2)
            )
            self._win.draw_line(top_wall, fill_color)

        if self.has_bottom_wall:
            bottom_wall = Line(
                Point(self._x1, self._y1), Point(self._x2, self._y1)
            )
            self._win.draw_line(bottom_wall, fill_color)

    def draw_move(self, to_cell: 'Cell', undo=False):
        fill_color: str = 'red' if not undo else 'gray'

        center_from_cell_x: float = (self._x2 + self._x1) / 2
        center_from_cell_y: float = (self._y2 + self._y1) / 2
        center_from_cell_point: Point = Point(
            center_from_cell_x, center_from_cell_y
        )

        center_to_cell_x: float = (to_cell._x2 + to_cell._x1) / 2
        center_to_cell_y: float = (to_cell._y2 + to_cell._y1) / 2
        center_to_cell_point: Point = Point(center_to_cell_x, center_to_cell_y)

        center_line: Line = Line(center_from_cell_point, center_to_cell_point)
        center_line.draw(self._win.canvas, fill_color)
