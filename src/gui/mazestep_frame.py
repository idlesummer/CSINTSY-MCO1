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
        self.step = 0
        self.mazeFrame.clear_paths(state="disabled")
        self.stepsBox.config(text=f"0")
    
    def button2_command(self): 
        visited = self.mazeAlgoFrame.visited
        if self.step > 1:
            self.step -= 1
            self.mazeFrame.clear_paths(state="disabled")
            self.mazeFrame.update_cells([(row, col, False) for row, col in visited[1:self.step+1]], bg="orange", state="disabled")
            self.mazeFrame.update_cells([(*current_step[self.step-1], False)], bg="yellow", state="disabled")
            self.stepsBox.config(text=self.step)
   
    def button3_command(self):
        visited = self.mazeAlgoFrame.visited
        if self.step < len(visited) - 1:
            self.step += 1
            self.mazeFrame.clear_paths(state="disabled")
            self.mazeFrame.update_cells([(row, col, False) for row, col in visited[1:self.step+1]], bg="orange", state="disabled")
            self.mazeFrame.update_cells([(*visited[self.step], False)], bg="yellow", state="disabled")
            self.stepsBox.config(text=self.step)

    def button4_command(self):
        visited = self.mazeAlgoFrame.visited
        self.step = len(visited) - 2
        self.mazeAlgoFrame.display_path(state="disabled")
        self.stepsBox.config(text=len(self.mazeAlgoFrame.solution))

    def clear_step(self):
        self.stepsBox.config(text=f"")

