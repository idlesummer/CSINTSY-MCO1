from tkinter import *
from tkinter import ttk

from gui.cell_button import *


class Mazeframe(ttk.LabelFrame):
    MAZE_HEIGHT = 900
    MAZE_WIDTH = 900
    GRID_SIZE_MIN = 8
    GRID_SIZE_DEF = 12
    GRID_SIZE_MAX = 64
    CELL_SIZE = 100
    EMPTY_MAZE = [[0] * (GRID_SIZE_MAX+2)] * (GRID_SIZE_MAX+2)
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent        
        self.cellTable = [[None] * (Mazeframe.GRID_SIZE_MAX+2) for _ in range(Mazeframe.GRID_SIZE_MAX+2)]
        self.wallTable = [[0] * (Mazeframe.GRID_SIZE_MAX+2) for _ in range(Mazeframe.GRID_SIZE_MAX+2)]
        self.playableSize = 0
    
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(*args, **kwargs)
    
    def setup_frame(self):
        self.config(text="", height=Mazeframe.MAZE_HEIGHT, width=Mazeframe.MAZE_WIDTH)
        self.columnconfigure(tuple(range(Mazeframe.GRID_SIZE_MAX+2)), weight=1) 
        self.rowconfigure(tuple(range(Mazeframe.GRID_SIZE_MAX+2)), weight=1)
        self.grid_propagate(False)
        self.create_cells()
        self.generate_maze(Mazeframe.GRID_SIZE_DEF)
        
    def create_cells(self):        
        for i in range(Mazeframe.GRID_SIZE_MAX+2):
            for j in range(Mazeframe.GRID_SIZE_MAX+2):
                cell = Cellbutton(self, row=i, column=j, text=f"({i},{j})")
                cell.config(side=Mazeframe.CELL_SIZE)
                cell.config(command=lambda c=cell: self.on_toggle(c))
                self.cellTable[i][j] = cell
                                
    def generate_maze(self, wallTable):      
        if isinstance(wallTable, int):
            playableSize = wallTable
            wallTable = Mazeframe.EMPTY_MAZE
        else:
            playableSize = len(wallTable)-2
        
        if playableSize < Mazeframe.GRID_SIZE_MIN or playableSize > Mazeframe.GRID_SIZE_MAX:
            return False

        #  Undraws old maze cells
        self.remove_cells([(i, j) for i in range(self.playableSize+2) for j in range(self.playableSize+2)])
       
        #  Draws maze cells
        self.update_cells([(i, j, wallTable[i][j]) for i in range(playableSize+2) for j in range(playableSize+2)])
        
        # Draws the border, source, and target
        self.playableSize = playableSize
        cells = []
        for i in range(self.playableSize+2):
            cells.append((0, i, True))
            cells.append((i, 0, True))
            cells.append((self.playableSize+1, i, True))
            cells.append((i, self.playableSize+1, True))
        self.update_cells(cells, state="disabled")
        self.update_source_target()
    
    def remove_cells(self, pos):
        for row, column in pos:
            self.wallTable[row][column] = 0
            cell = self.cellTable[row][column]
            cell.grid_remove()

    def update_cells(self, pos, state="normal", bg="white"):
        for row, column, selected in pos:       
            cell = self.cellTable[row][column]
            cell.config(state=state, bg=bg)
            cell.grid(row=row, column=column, sticky="news")
            
            if selected:
                cell.select()
                self.wallTable[row][column] = 1
            else:
                cell.deselect()
                self.wallTable[row][column] = 0
    
    def clear_paths(self):
        playableSize = self.playableSize
        wallTable = self.wallTable
        self.update_cells([(i, j, wallTable[i][j]) for i in range(playableSize+2) for j in range(playableSize+2)])
        self.mazeFrame.update_source_target()
    
    def update_source_target(self):
        # Updates the source and target cell
        self.update_cells([(1, 1, False)], state="disabled", bg="red")
        self.update_cells([(self.playableSize, self.playableSize, False)], state="disabled", bg="green")
        
    def on_toggle(self, cell):
        self.wallTable[cell.row][cell.column] = cell.value
        
    @staticmethod
    def get_neighbors(pos, wallTable):
        row, column = pos
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        return [(None, (row+y, column+x)) for y, x in directions if wallTable[row + y][column + x] == 0]
        
