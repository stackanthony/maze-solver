from src.classes.Window import Window


def main():
    win = Window(800, 600, 'Main Window')
    win.wait_for_close()


if __name__ == '__main__':
    main()
