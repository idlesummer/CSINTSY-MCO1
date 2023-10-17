from ctypes import windll
from tkinter import *

from Cellbutton import *


class App(Frame):
    TITLE = "Maze Search"
    WINDOW_SIZE = "1300x900"
    MAZE_HEIGHT = 800
    MAZE_WIDTH = 800
    CELL_FRAME_WIDTH = 800
    CELL_FRAME_HEIGHT = 800
    CELL_SIZE = 100
    MAZE_SIZE = 12
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent 
        self.mazeFrame = None
        self.cellFrame = None
        self.mazeSize = 12
        self.cells = None
        self.menuFrame = None        
        self.setup_window()
        
    def setup_window(self):
        self.parent.geometry(App.WINDOW_SIZE)
        self.parent.title(App.TITLE)
        self.pack(side="top", fill="both", expand=True)
        windll.shcore.SetProcessDpiAwareness(1)
        
    def run(self):
        self.display_maze_grid()
        self.display_user_menu()
        return self
        
    def display_maze_grid(self):            
        self.mazeFrame = LabelFrame(self, text="")
        self.mazeFrame.config(height=App.MAZE_HEIGHT, width=App.MAZE_WIDTH)
        self.mazeFrame.grid(row=0, column=0, padx=20, pady=20)
        self.mazeFrame.grid_propagate(False)
        self.generate_maze(size=App.MAZE_SIZE)
                
    def generate_maze(self, size):
        if size < 8 or size > 64:
            return False
               
        if self.cells:
            for row in self.cells:
                for cell in row:
                    cell.grid_forget()
                    cell.destroy()
                    
        self.size = size
        self.mazeFrame.columnconfigure(tuple(range(self.size+2)), weight=1) 
        self.mazeFrame.rowconfigure(tuple(range(self.size+2)),weight=1)
        
        self.cells = [[None] * (size+2) for _ in range(size+2)] 
        for i in range(size+2):
            for j in range(size+2):
                cell = Cellbutton(self.mazeFrame, text=f"({i},{j})")
                cell.config(side=App.CELL_SIZE)
                cell.grid(row=i, column=j, sticky="nsew")
                self.cells[i][j] = cell
        
        for i in range(size+2):
            self.cells[0][i].config(state="disabled").select()            
            self.cells[-1][i].config(state="disabled").select()
            self.cells[i][0].config(state="disabled").select()
            self.cells[i][-1].config(state="disabled").select()
            
        self.cells[1][1].config(state="disabled", bg="Red")
        self.cells[size][size].config(state="disabled", bg="Green")
            
        
    def display_user_menu(self):
        self.menuFrame = LabelFrame(self, text="User Menu")
        self.menuFrame.grid(row=0, column=1)
        
        cell2 = Button(self.menuFrame, text="B", command=self.foo)
        cell2.pack(padx=10, pady=10)

    def foo(self):
        x = self.mazeFrame.winfo_width()
        y = self.mazeFrame.winfo_height()
        print("mazeFrame Width:", x)
        print("MazeFrame Height:", y)
        print(self.cells[0][0].winfo_width(), self.cells[0][0].winfo_height())
        
        self.generate_maze(size=30)
