from tkinter import ttk

from algorithms.maze_solver import *

class MazeStepframe(ttk.LabelFrame):
    def __init__(self, parent, mazeFrame, mazeAlgoFrame, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.mazeFrame = mazeFrame
        self.mazeAlgoFrame = mazeAlgoFrame
        self.stepsLabel = None
        self.stepsBox = None
        self.buttonFrame = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.step = 0
        self.all_cells = []
              
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(columnspan=2, padx=10, pady=5, *args, **kwargs)
        
    def setup_frame(self):       
        self.stepsLabel = ttk.Label(self, text="Steps Taken:")
        self.stepsLabel.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        #not an entry box, content inside can be changed once
        self.stepsBox = ttk.Label(self, text="", relief="solid", borderwidth=1, width = 20, anchor="center", justify="center")  
        self.stepsBox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # ff, rewind buttons
        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="w")

        self.button1 = ttk.Button(self.buttonFrame, text="⏮", width=3, command=self.button1_command)
        self.button2 = ttk.Button(self.buttonFrame, text="⏴", width=3, command=self.button2_command)
        self.button3 = ttk.Button(self.buttonFrame, text="⏵", width=3, command=self.button3_command)
        self.button4 = ttk.Button(self.buttonFrame, text="⏭", width=3, command=self.button4_command)

        self.button1.grid(row=0, column=0, padx=(0,5))
        self.button2.grid(row=0, column=1, padx=(0,5))
        self.button3.grid(row=0, column=2, padx=(0,5))
        self.button4.grid(row=0, column=3, padx=(0,5))
        
    def button1_command(self):
        self.mazeFrame.clear_paths()
        self.stepsBox.config(text=f"0")
        pass
    
    def button2_command(self): 
        visited = self.mazeAlgoFrame.visited
        current_step = visited[1:self.step+1]
        if self.step > 0:
            self.step -= 1
            self.mazeFrame.update_cells([(row, col, False) for row, col in current_step[-1:self.step+1]], bg="white")
            self.stepsBox.config(text=self.step)
        pass
   
    def button3_command(self):
        visited = self.mazeAlgoFrame.visited
        if self.step < len(visited) - 1:
            self.step += 1
            self.mazeFrame.clear_paths()
            self.mazeFrame.update_cells([(row, col, False) for row, col in visited[1:self.step+1]], bg="orange")
            self.stepsBox.config(text=self.step)
        pass
        
    def button4_command(self):
        self.mazeAlgoFrame.display_path()
        self.stepsBox.config(text=len(self.mazeAlgoFrame.solution))
        pass
    
    def clear_step(self):
        self.stepsBox.config(text=f"")
        pass
        
    # for the disable thingy
    def disable_all_cells(self):
        all_cells = [(i, j, self.mazeFrame.wallTable[i][j]) for i in range(self.mazeFrame.playableSize+2) for j in range(self.mazeFrame.playableSize+2)]
        self.mazeFrame.update_cells(all_cells, state="disabled")