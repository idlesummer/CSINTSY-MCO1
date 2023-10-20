from ctypes import windll
from tkinter import ttk

from gui.maze_frame import *
from gui.menu_frame import *


class App(ttk.Frame):
    TITLE = "Maze Search"
    WINDOW_SIZE = "1400x940"

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setup_window()
        
        self.mazeFrame = Mazeframe(self)
        self.menuFrame = Menuframe(self, self.mazeFrame)
        
        self.mazeFrame.grid(row=0, column=0, padx=20, pady=20)
        self.menuFrame.grid(row=0, column=1, padx=20, pady=20)

    def setup_window(self):
        self.parent.title(App.TITLE)
        self.parent.geometry(App.WINDOW_SIZE)
        self.parent.resizable(False, False)
        windll.shcore.SetProcessDpiAwareness(True)
