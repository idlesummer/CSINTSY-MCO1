from tkinter import ttk


class MazeStepframe(ttk.LabelFrame):
    def __init__(self, parent, command, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.command = command
        
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(columnspan=2, padx=10, pady=5, *args, **kwargs)
        
    def setup_frame(self):       
        stepsLabel = ttk.Label(self, text="Steps Taken:")
        stepsLabel.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        #not an entry box, content inside can be changed once
        self.stepsBox = ttk.Label(self, text="", relief="solid", borderwidth=1, width = 20)  
        self.stepsBox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # ff, rewind buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="w")

        button1 = ttk.Button(self.button_frame, text="⏮", width=3)
        button2 = ttk.Button(self.button_frame, text="⏴", width=3)
        button3 = ttk.Button(self.button_frame, text="⏵", width=3)
        button4 = ttk.Button(self.button_frame, text="⏭", width=3)

        button1.grid(row=0, column=0, padx=(0,5))
        button2.grid(row=0, column=1, padx=(0,5))
        button3.grid(row=0, column=2, padx=(0,5))
        button4.grid(row=0, column=3, padx=(0,5))
