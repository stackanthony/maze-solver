from tkinter import Tk, Canvas

from src.classes.Line import Line


class Window:
    def __init__(
        self, width: float = 0.0, height: float = 0.0, title: str = 'Window'
    ) -> None:
        self.root = Tk()
        self.root.title(title)
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False
        self.root.destroy()
