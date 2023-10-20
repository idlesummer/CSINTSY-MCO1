from tkinter import ttk

from gui.maze_frame import *
from gui.mazesize_frame import *
from gui.mazefile_frame import *
from gui.mazealgo_frame import *
from gui.mazestep_frame import *
from algorithms.maze_solver import *

class Menuframe(ttk.Labelframe):
    TEXT = "Maze Menu"
    
    def __init__(self, parent, mazeFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent        
        self.mazeFrame = mazeFrame
        self.mazeSizeFrame = None
        self.mazeFileFrame = None
        self.mazeAlgoFrame = None
        self.sizeSpinbox = None
        self.mazeButton = None
        
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(*args, **kwargs)
        
    def setup_frame(self):
        self.config(text=Menuframe.TEXT)
        self.mazeSizeFrame = MazeSizeframe(self, command=self.mazeFrame.generate_maze)
        self.mazeFileFrame = MazeFileframe(self, command=self.mazeFrame.generate_maze)
        self.mazeAlgoFrame = MazeAlgoframe(self, command=None)
        self.mazeStepFrame = MazeStepframe(self, command=None)
                
        self.mazeSizeFrame.grid(row=0, column=0)
        self.mazeFileFrame.grid(row=1, column=0)
        self.mazeAlgoFrame.grid(row=2, column=0)
        self.mazeStepFrame.grid(row=3, column=0)
