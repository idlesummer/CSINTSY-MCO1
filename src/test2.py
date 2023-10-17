from ctypes import windll
from tkinter import *


from tkinter import Checkbutton, PhotoImage

class Cellbutton(Checkbutton):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, indicatoron=False, *args, **kwargs)
        self.image = PhotoImage()
        self.config(image=self.image, compound="center")
        self.config(selectcolor="#404040")
        
    def config(self, side=None, *args, **kwargs):
        if side:
            kwargs['width'] = side
            kwargs['height'] = side
        super().config(*args, **kwargs)
        return self


class App(Frame):
    TITLE = "Maze Search"
    WINDOW_SIZE = "1400x940"
    MAZE_HEIGHT = 900
    MAZE_WIDTH = 900
    GRID_SIZE_MIN = 8
    GRID_SIZE_DEF = 12
    GRID_SIZE_MAX = 64
    CELL_SIZE = 100

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.mazeFrame = None
        self.cellTable = None
        self.menuFrame = None
        self.setup_window()
        
    def setup_window(self):
        self.parent.geometry(App.WINDOW_SIZE)
        self.parent.resizable(False, False)
        self.parent.title(App.TITLE)
        self.pack(side="top", fill="both", expand=True)
        windll.shcore.SetProcessDpiAwareness(1)
        
    def run(self):
        self.display_maze()
        self.display_menu()
        return self
        
    def display_maze(self):
        self.mazeFrame = LabelFrame(self, text="")
        self.mazeFrame.config(height=App.MAZE_HEIGHT, width=App.MAZE_WIDTH)
        self.mazeFrame.grid(row=0, column=0, padx=20, pady=20)
        self.generate_maze(App.GRID_SIZE_DEF)
        
    def generate_maze(self, size):
        pass
    
    def display_menu(self):
        self.menuFrame = LabelFrame(self, text="User Menu")
        self.menuFrame.grid(row=0, column=1)
     
        button = Button(self.menuFrame, text="B", command=self.foo)
        button.pack(padx=10, pady=10)
        
    def foo(self):
        x = self.parent.winfo_width()
        y = self.parent.winfo_height()
        print("Parent Width:", x)
        print("Parent Height:", y)


def main():
    root = Tk()
    app = App(root).run()
    root.mainloop()


if __name__ == "__main__":
    main()
