from ctypes import windll
from tkinter import *

from Cellbutton import *


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
        self.menuFrame = None
        self.cellTable = [[None] * (App.GRID_SIZE_MAX+2) for _ in range(App.GRID_SIZE_MAX+2)]
        self.wallTable = [[0] * (App.GRID_SIZE_MAX+2) for _ in range(App.GRID_SIZE_MAX+2)]
        self.tableSize = 0
        self.setup_window()
        
    def setup_window(self):
        self.parent.title(App.TITLE)
        self.parent.geometry(App.WINDOW_SIZE)
        self.parent.resizable(False, False)
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
        self.mazeFrame.grid_propagate(False)
        self.create_maze()
        self.show_maze(App.GRID_SIZE_DEF)
        
    def create_maze(self):        
        for i in range(App.GRID_SIZE_MAX+2):
            for j in range(App.GRID_SIZE_MAX+2):
                cell = Cellbutton(self.mazeFrame, text=f"({i},{j})")
                var = BooleanVar()
                cell.config(side=App.CELL_SIZE, variable=var)
                self.cellTable[i][j] = cell
                                
    def show_maze(self, size):        
        if size < App.GRID_SIZE_MIN or size > App.GRID_SIZE_MAX:
            return False
        if self.tableSize == size:
            return False

        #  Undraws maze cells
        for i in range(self.tableSize+2):
            for j in range(self.tableSize+2):
                cell = self.cellTable[i][j]
                cell.grid_remove()
                self.wallTable[i][j] = 0

        self.tableSize = size
        self.mazeFrame.columnconfigure(tuple(range(self.tableSize+2)), weight=1) 
        self.mazeFrame.rowconfigure(tuple(range(self.tableSize+2)), weight=1)
        
        #  Draws maze cells
        for i in range(size+2):
            for j in range(size+2):
                cell = self.cellTable[i][j]
                cell.config(state="normal", bg="White")
                cell.deselect()
                cell.grid(row=i, column=j, sticky="nsew")
        
        # Draws the border
        for i in range(self.tableSize+2):
            self.cellTable[0][i].config(state="disabled").select()           
            self.cellTable[i][0].config(state="disabled").select()
            self.cellTable[self.tableSize+1][i].config(state="disabled").select()
            self.cellTable[i][self.tableSize+1].config(state="disabled").select()
            self.wallTable[0][i] = 1
            self.wallTable[i][0] = 1
            self.wallTable[self.tableSize+1][i] = 1
            self.wallTable[i][self.tableSize+1] = 1
            
        self.cellTable[1][1].config(state="disabled", bg="Red")
        self.cellTable[self.tableSize][self.tableSize].config(state="disabled", bg="Green")
    
    def display_menu(self):
        self.menuFrame = LabelFrame(self, text="User Menu")
        self.menuFrame.grid(row=0, column=1)
               
        cell2 = Button(self.menuFrame, text="B", command=self.foo)
        cell2.pack(padx=10, pady=10)
        
    def foo(self):
        x = self.parent.winfo_width()
        y = self.parent.winfo_height()
        print("Parent Width:", x)
        print("Parent Height:", y)
        self.show_maze(30)
