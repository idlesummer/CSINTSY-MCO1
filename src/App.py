from ctypes import windll
from tkinter import *
from tkinter import ttk

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
    I = 0
    FOO = [8, 16, 24, 32]

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
        self.update_cells([(1, 1)], state="disabled", bg="red")
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

        #  Undraws old maze cells
        self.remove_cells([(i, j) for i in range(self.tableSize+2) for j in range(self.tableSize+2)])

        # Enables the buttons to stretch or shrink depending on maze size
        self.tableSize = size
        self.mazeFrame.columnconfigure(tuple(range(self.tableSize+2)), weight=1) 
        self.mazeFrame.rowconfigure(tuple(range(self.tableSize+2)), weight=1)
        
        #  Draws maze cells
        self.update_cells([(i, j) for i in range(size+2) for j in range(size+2)], select=False)
        
        # Draws the border
        cells = []
        for i in range(self.tableSize+2):
            cells.append((0, i))
            cells.append((i, 0))
            cells.append((self.tableSize+1, i))
            cells.append((i, self.tableSize+1))
        self.update_cells(cells, state="disabled", select=True)
        
        # Updates the target cell
        self.update_cells([(self.tableSize, self.tableSize)], state="disabled", bg="green")
    
    def remove_cells(self, pos):
        for row, column in pos:
            cell = self.cellTable[row][column]
            self.wallTable[row][column] = 0
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

    def display_menu(self):
        self.menuFrame = LabelFrame(self, text="User Menu")
        self.menuFrame.grid(row = 0, column = 1)
        
        #spinbox to pick maze size 
        label1 = Label(self.menuFrame, text="Choose maze size:")
        label1.grid(row = 0, column = 1, padx = 10, pady = 5)
        
        spinbox = ttk.Spinbox(self.menuFrame, from_=App.GRID_SIZE_MIN, to=App.GRID_SIZE_MAX, width=20)
        spinbox.grid(row = 1, column = 1, padx = 10, pady = 5)
        
        mazeButton = Button(self.menuFrame, text="Generate Maze")
        mazeButton.grid(row = 1, column = 2, padx = 10, pady = 5)
        
        
        #code for the disappearing labelframe
        '''
        
        self.showButton= Button(self.menuFrame, text="Generate Existing Maze", command=self.show_existing_maze)
        self.showButton.grid(row=2, column=2, columnspan=2, padx=10, pady=5)
        
        self.container1 = LabelFrame(self.menuFrame)
        self.container1.grid(row=3, column=2, columnspan=2, padx=10, pady=5)
        self.container1.grid_forget()
        
        chooseExistingMaze = Label(self.container1, text="Choose an existing maze:")
        chooseExistingMaze.grid(row=0, column=1, padx=10, pady=5, sticky="e")
        
        existingOptions = [ 
            "insert existing maze"
        ]
        
        self.selectedEOption = StringVar(self)
        self.selectedEOption.set(existingOptions[0])
        
        optionBox = ttk.Combobox(self.container1, textvariable=self.selectedEOption, values=existingOptions)
        optionBox.grid(row=1, column=1, padx=10, pady=5)
        
        pathButton = Button(self.container1, text="Generate Maze")
        pathButton.grid(row=2, column=1, padx=10, pady=5)
        
        '''
        label2 = Label(self.menuFrame, text="Choose existing maze:")
        label2.grid(row = 2, column = 1, padx = 10, pady = 5)
        
        pathButton = Button(self.menuFrame, text="Generate Existing Maze")
        pathButton.grid(row = 3, column = 2, columnspan = 2, padx = 10, pady = 5)
        
        existingOptions = [ 
            "insert existing maze"
        ]
        
        self.selectedEOption = StringVar(self)
        self.selectedEOption.set(existingOptions[0])
        
        optionEBox = ttk.Combobox(self.menuFrame, textvariable=self.selectedEOption, values=existingOptions)
        optionEBox.grid(row = 3, column = 1, padx = 10, pady = 5)
        
        spacer = Label(self.menuFrame, text="", width=1, height=1)
        spacer.grid(row = 4, column = 1)
        
        # options for the dropdown menu
        options = [ 
            "Breadth First Search",
            "A* Search"
        ]
        
        self.selectedOption = StringVar(self)
        self.selectedOption.set(options[0])
        
        label2 = Label(self.menuFrame, text="Choose Algorithm:")
        label2.grid(row = 5, column = 1, padx = 10, pady = 5)

        optionBox = ttk.Combobox(self.menuFrame, textvariable=self.selectedOption, values=options)
        optionBox.grid(row = 6, column = 1, padx = 10, pady = 5)
        
        pathButton = Button(self.menuFrame, text="Generate Path")
        pathButton.grid(row = 6, column = 2, padx = 10, pady = 5)
        
        spacer = Label(self.menuFrame, text="", width=1, height=1)
        spacer.grid(row = 7, column = 1)
        
        # widget for the steps taken display
        container1 = LabelFrame(self.menuFrame)
        container1.grid(row = 8, column = 1, columnspan = 2, padx = 10, pady = 5)
        
        stepsLabel = Label(container1, text="Steps Taken:")
        stepsLabel.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "e")

        #not an entry box, content inside can be changed once
        self.stepsBox = Label(container1, text="", relief="solid", borderwidth=1, width = 20, height = 1)  
        self.stepsBox.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = "w")
        
        # ff, rewind buttons
        button_frame = Frame(container1)
        button_frame.grid(row = 1, column = 2, columnspan = 2, padx = 10, pady = 5)

        button1 = Button(button_frame, text = "⏮")
        button2 = Button(button_frame, text = "⏴")
        button3 = Button(button_frame, text = "⏵")
        button4 = Button(button_frame, text = "⏭")

        button1.pack(side="left", padx = 5)
        button2.pack(side="left", padx = 5)
        button3.pack(side="left", padx = 5)
        button4.pack(side="left", padx = 5)
    
    #code for the disappearing labelframe
    '''
    def show_existing_maze(self): #iyah
        if self.container1.winfo_viewable():
            self.container1.grid_forget()
        else:
            self.container1.grid()
    ''' 
        
    def foo(self):
        x = self.parent.winfo_width()
        y = self.parent.winfo_height()
        print("Parent Width:", x)
        print("Parent Height:", y)
        
        self.show_maze(App.FOO[App.I % 4])
        App.I += 1
