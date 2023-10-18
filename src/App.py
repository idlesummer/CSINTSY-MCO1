from ctypes import windll
from tkinter import *
from tkinter import ttk

from Mazeframe import *
from Cellbutton import *


class App(Frame):
    TITLE = "Maze Search"
    WINDOW_SIZE = "1400x940"

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setup_window()
        
        self.mazeFrame = Mazeframe(self)        
        self.display_menu()
        
        self.mazeFrame.grid(row=0, column=0, padx=20, pady=20)

    def setup_window(self):
        self.parent.title(App.TITLE)
        self.parent.geometry(App.WINDOW_SIZE)
        self.parent.resizable(False, False)
        windll.shcore.SetProcessDpiAwareness(True)

    def display_menu(self):
        self.menuFrame = LabelFrame(self, text="User Menu")
        self.menuFrame.grid(row=0, column=1)
        
        #spinbox to pick maze size 
        label1 = Label(self.menuFrame, text="Choose maze size:")
        label1.grid(row=0, column=1, padx=10, pady=5)
        
        spinbox = ttk.Spinbox(self.menuFrame, from_=Mazeframe.GRID_SIZE_MIN, to=Mazeframe.GRID_SIZE_MAX, width=20)
        spinbox.grid(row=1, column=1, padx=10, pady=5)
        
        mazeButton = Button(self.menuFrame, text="Generate Maze", command=self.foo)
        mazeButton.grid(row=1, column=2, padx=10, pady=5)
    
        label2 = Label(self.menuFrame, text="Choose existing maze:")
        label2.grid(row=2, column=1, padx=10, pady=5)
        
        pathButton = Button(self.menuFrame, text="Generate Existing Maze", command=self.bar)
        pathButton.grid(row=3, column=2, columnspan=2, padx=10, pady=5)
        
        
        # ---------------------------------------
        
        existingOptions = [ 
            "insert existing maze"
        ]
        
        self.selectedEOption = StringVar(self)
        self.selectedEOption.set(existingOptions[0])
        
        optionEBox = ttk.Combobox(self.menuFrame, textvariable=self.selectedEOption, values=existingOptions)
        optionEBox.grid(row=3, column=1, padx=10, pady=5)
        
        spacer = Label(self.menuFrame, text="", width=1, height=1)
        spacer.grid(row=4, column=1)
        
        # options for the dropdown menu
        options = [ 
            "Breadth First Search",
            "A* Search"
        ]
        
        self.selectedOption = StringVar(self)
        self.selectedOption.set(options[0])
        
        label2 = Label(self.menuFrame, text="Choose Algorithm:")
        label2.grid(row=5, column=1, padx=10, pady=5)

        optionBox = ttk.Combobox(self.menuFrame, textvariable=self.selectedOption, values=options)
        optionBox.grid(row=6, column=1, padx=10, pady=5)
        
        pathButton = Button(self.menuFrame, text="Generate Path")
        pathButton.grid(row=6, column=2, padx=10, pady=5)
        
        spacer = Label(self.menuFrame, text="", width=1, height=1)
        spacer.grid(row=7, column=1)
        
        # widget for the steps taken display
        container1 = LabelFrame(self.menuFrame)
        container1.grid(row=8, column=1, columnspan=2, padx=10, pady=5)
        
        stepsLabel = Label(container1, text="Steps Taken:")
        stepsLabel.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        #not an entry box, content inside can be changed once
        self.stepsBox = Label(container1, text="", relief="solid", borderwidth=1, width = 20, height = 1)  
        self.stepsBox.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        # ff, rewind buttons
        button_frame = Frame(container1)
        button_frame.grid(row=1, column=2, columnspan=2, padx=10, pady=5)

        button1 = Button(button_frame, text="⏮")
        button2 = Button(button_frame, text="⏴")
        button3 = Button(button_frame, text="⏵")
        button4 = Button(button_frame, text="⏭")

        button1.pack(side="left", padx=5)
        button2.pack(side="left", padx=5)
        button3.pack(side="left", padx=5)
        button4.pack(side="left", padx=5)
        
    def foo(self):
        self.mazeFrame.generate_maze(30)
        
    def bar(self):
        self.mazeFrame.generate_maze(8)