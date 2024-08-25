from src.classes.Cell import Cell
from src.classes.Line import Line
from src.classes.Maze import Maze
from src.classes.Point import Point
from src.classes.Window import Window


def main():
    win = Window(800, 600, 'Main Window')
    maze = Maze(300, 300, 3, 3, 100, 100, win)
    maze._create_cells()
    maze._break_entrance_and_exit()
    # win.draw_line(Line(Point(10, 20), Point(10, 30)), 'red')
    # win.draw_line(Line(Point(100, 200), Point(50, 600)), 'red')
    # win.draw_line(Line(Point(60, 20), Point(5, 30)), 'red')
    # cell_1 = Cell(_x1=30, _x2=150, _y1=40, _y2=250, _win=win)
    # cell_2 = Cell(_x1=50, _x2=180, _y1=60, _y2=300, _win=win)
    #
    # cell_1.draw('white')
    # cell_2.draw('red')
    # cell_1.draw_move(cell_2, True)
    # cell_3 = Cell(
    #     has_top_wall=False, _x1=70, _x2=200, _y1=80, _y2=350, _win=win
    # )
    # cell_4 = Cell(
    #     has_bottom_wall=False, _x1=700, _x2=200, _y1=80, _y2=350, _win=win
    # )

    # cell_3.draw('blue')
    # cell_4.draw('orange')
    win.wait_for_close()


if __name__ == '__main__':
    main()
