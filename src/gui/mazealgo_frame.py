from tkinter import ttk, StringVar

from algorithms.maze_solver import *


class MazeAlgoframe(ttk.Frame):
    TEXTS = ["Choose algorithm:", "Generate Path Solution"]
    
    def __init__(self, parent, mazeFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.mazeFrame = mazeFrame
        self.mazeSolver = None
        self.label = None
        self.combobox = None
        self.button = None
        self.var = StringVar()
        self.algonames = []
        
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(*args, **kwargs)
        
    def setup_frame(self):
        self.label = ttk.Label(self, text=MazeAlgoframe.TEXTS[0]) 
        self.load_files()    
        self.combobox = ttk.Combobox(self, values=self.algonames, textvariable=self.var)
        self.combobox.set(self.algonames[0])
        self.button = ttk.Button(self, text=MazeAlgoframe.TEXTS[1], command=self.run_command)
        
        self.label.grid(row=0, column=0, padx=10, pady=5)
        self.combobox.grid(row=1, column=0, padx=10, pady=5)
        self.button.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
    
    def load_files(self):
        self.mazeSolver = MazeSolver()
        self.mazeSolver.load_files()
        self.algorithms = self.mazeSolver.algorithms
        self.algonames = self.mazeSolver.algonames
        self.algonames.sort()

    def run_command(self):
        source = (1, 1)
        target = (self.mazeFrame.playableSize, self.mazeFrame.playableSize)
        wallTable = self.mazeFrame.wallTable
        solution = self.mazeSolver.solve(self.algoname, source, target, wallTable)
        print(solution)
        
    @property
    def algoname(self):
        return self.var.get()
