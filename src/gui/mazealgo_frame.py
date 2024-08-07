from tkinter import ttk, StringVar

from algorithms.maze_solver import *


class MazeAlgoframe(ttk.Frame):
    TEXTS = ["Choose algorithm:", "Generate Path Solution"]
    
    def __init__(self, parent, mazeFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.mazeFrame = mazeFrame
        self.command = None
        self.mazeSolver = None
        self.label = None
        self.combobox = None
        self.button = None
        self.var = StringVar()
        self.algonames = []
        self.visited = []
        self.solution = []
    
    def config(self, command=None, *args, **kwargs):
        self.command = command
        super().grid(*args, **kwargs)
    
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
        if self.command:
            self.command()
        self.mazeFrame.clear_paths()
        source = (1, 1)
        target = (self.mazeFrame.playableSize, self.mazeFrame.playableSize)
        wallTable = self.mazeFrame.wallTable
        self.visited, self.solution = self.mazeSolver.solve(self.algoname, source, target, wallTable)
        self.display_path()
        
    def display_path(self, state="normal"):
        if self.solution:
            self.mazeFrame.update_cells([(*pos, False) for pos in self.visited[1:-1]], bg="orange", state=state)
            self.mazeFrame.update_cells([(*pos, False) for pos in self.solution[:-1]], bg="brown", state=state)
    
    def clear_solution(self):
        self.visited = []
        self.solution = []
    
    @property
    def algoname(self):
        return self.var.get()
