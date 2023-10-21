from tkinter import ttk, IntVar

from gui.maze_frame import *


class MazeSizeframe(ttk.Frame):
    TEXTS = ["Choose maze size:", "Generate New Maze"]
    
    def __init__(self, parent, command, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.command = command
        self.label = None
        self.spinbox = None
        self.button = None
        self.var = IntVar()
        self.var.set(Mazeframe.GRID_SIZE_DEF)
    
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(*args, **kwargs)
     
    def setup_frame(self):
        self.label = ttk.Label(self, text=MazeSizeframe.TEXTS[0])
        self.spinbox = ttk.Spinbox(self, from_=Mazeframe.GRID_SIZE_MIN, to=Mazeframe.GRID_SIZE_MAX, width=20, textvariable=self.var)
        self.button = ttk.Button(self, text=MazeSizeframe.TEXTS[1], command=self.run_command)
        self.label.grid(row=0, column=0, padx=10, pady=5)
        self.spinbox.grid(row=1, column=0, padx=10, pady=5)
        self.button.grid(row=1, column=1, padx=10, pady=5)

    def run_command(self):
        self.command(self.maze_size)

    @property
    def maze_size(self):
        return self.var.get()
