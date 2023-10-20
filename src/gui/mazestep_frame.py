from tkinter import ttk


class MazeStepframe(ttk.LabelFrame):
    def __init__(self, parent, command, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.command = command
        self.stepsLabel = None
        self.stepsBox = None
        self.buttonFrame = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
              
    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(columnspan=2, padx=10, pady=5, *args, **kwargs)
        
    def setup_frame(self):       
        self.stepsLabel = ttk.Label(self, text="Steps Taken:")
        self.stepsLabel.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        #not an entry box, content inside can be changed once
        self.stepsBox = ttk.Label(self, text="", relief="solid", borderwidth=1, width = 20)  
        self.stepsBox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # ff, rewind buttons
        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="w")

        self.button1 = ttk.Button(self.buttonFrame, text="⏮", width=3)
        self.button2 = ttk.Button(self.buttonFrame, text="⏴", width=3)
        self.button3 = ttk.Button(self.buttonFrame, text="⏵", width=3)
        self.button4 = ttk.Button(self.buttonFrame, text="⏭", width=3)

        self.button1.grid(row=0, column=0, padx=(0,5))
        self.button2.grid(row=0, column=1, padx=(0,5))
        self.button3.grid(row=0, column=2, padx=(0,5))
        self.button4.grid(row=0, column=3, padx=(0,5))
