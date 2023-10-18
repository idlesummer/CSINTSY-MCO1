from tkinter import *
from tkinter import ttk

from Cellbutton import *


class Mazeframe(ttk.LabelFrame):
    MAZE_HEIGHT = 900
    MAZE_WIDTH = 900
    GRID_SIZE_MIN = 8
    GRID_SIZE_DEF = 12
    GRID_SIZE_MAX = 64
    CELL_SIZE = 100
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent        
        self.cellTable = [[None] * (Mazeframe.GRID_SIZE_MAX+2) for _ in range(Mazeframe.GRID_SIZE_MAX+2)]
        self.wallTable = [[0] * (Mazeframe.GRID_SIZE_MAX+2) for _ in range(Mazeframe.GRID_SIZE_MAX+2)]
        self.tableSize = 0
    
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(*args, **kwargs)
    
    def setup_frame(self):
        self.config(text="", height=Mazeframe.MAZE_HEIGHT, width=Mazeframe.MAZE_WIDTH)
        self.columnconfigure(tuple(range(Mazeframe.GRID_SIZE_MAX+2)), weight=1) 
        self.rowconfigure(tuple(range(Mazeframe.GRID_SIZE_MAX+2)), weight=1)
        self.grid_propagate(False)
                
        self.create_maze()
        self.generate_maze(Mazeframe.GRID_SIZE_DEF)
        
    def create_maze(self):        
        for i in range(Mazeframe.GRID_SIZE_MAX+2):
            for j in range(Mazeframe.GRID_SIZE_MAX+2):
                cell = Cellbutton(self, row=i, column=j, text=f"({i},{j})")
                cell.config(command=lambda c=cell: self.on_toggle(c))
                cell.config(side=Mazeframe.CELL_SIZE)
                self.cellTable[i][j] = cell
                                
    def generate_maze(self, size):        
        if size < Mazeframe.GRID_SIZE_MIN or size > Mazeframe.GRID_SIZE_MAX:
            return False
        if self.tableSize == size:
            return False

        #  Undraws old maze cells
        self.remove_cells([(i, j) for i in range(self.tableSize+2) for j in range(self.tableSize+2)])
       
        #  Draws maze cells
        self.update_cells([(i, j) for i in range(size+2) for j in range(size+2)], select=False)

        # Draws the border
        self.tableSize = size
        cells = []
        for i in range(self.tableSize+2):
            cells.append((0, i))
            cells.append((i, 0))
            cells.append((self.tableSize+1, i))
            cells.append((i, self.tableSize+1))
        self.update_cells(cells, state="disabled", select=True)
        
        # Updates the source and target cell
        self.update_cells([(1, 1)], state="disabled", bg="red")
        self.update_cells([(self.tableSize, self.tableSize)], state="disabled", bg="green")
    
    def remove_cells(self, pos):
        for row, column in pos:
            self.wallTable[row][column] = 0
            cell = self.cellTable[row][column]
            cell.grid_remove()

    def update_cells(self, pos, state="normal", bg="white", select=False):
        for row, column in pos:       
            cell = self.cellTable[row][column]
            cell.config(state=state, bg=bg)
            cell.grid(row=row, column=column, sticky="nsew")
            
            if select:
                cell.select()
                self.wallTable[row][column] = 1
            else:
                cell.deselect()
                self.wallTable[row][column] = 0
                
    def on_toggle(self, cell):
        self.wallTable[cell.row][cell.column] = int(cell.value)
