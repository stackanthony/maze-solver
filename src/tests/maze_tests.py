import unittest
from src.classes.Maze import Maze
from src.classes.Cell import Cell
from src.classes.Window import Window


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        """Test that the maze creates the correct number of cells."""
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check that the number of rows in the grid matches num_rows
        self.assertEqual(len(m1._cells), num_rows)

        # Check that the number of columns in the grid matches num_cols
        self.assertEqual(len(m1._cells[0]), num_cols)

        # Check that all cells are instances of Cell
        for row in m1._cells:
            for cell in row:
                self.assertIsInstance(cell, Cell)

    def test_cell_coordinates(self):
        """Test that cells are assigned the correct coordinates."""
        num_cols = 2
        num_rows = 2
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        # Check the coordinates of the top-left cell (0,0)
        self.assertEqual(m1._cells[0][0]._x1, 0)
        self.assertEqual(m1._cells[0][0]._y1, 0)
        self.assertEqual(m1._cells[0][0]._x2, 10)
        self.assertEqual(m1._cells[0][0]._y2, 10)

        # Check the coordinates of the bottom-right cell (1,1)
        self.assertEqual(m1._cells[1][1]._x1, 10)
        self.assertEqual(m1._cells[1][1]._y1, 10)
        self.assertEqual(m1._cells[1][1]._x2, 20)
        self.assertEqual(m1._cells[1][1]._y2, 20)

    def test_maze_with_window(self):
        """Test the maze creation with a Window object."""
        num_cols = 5
        num_rows = 5
        win = Window()
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

        # Check that the window is correctly assigned
        self.assertEqual(m1.win, win)

        # Check that all cells have the same window object
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell._win, win)

    def test_maze_without_window(self):
        """Test the maze creation without a Window object."""
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check that the window is None
        self.assertIsNone(m1.win)


if __name__ == '__main__':
    unittest.main()
