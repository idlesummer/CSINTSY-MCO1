import os
from tkinter import ttk, StringVar


class MazeFileframe(ttk.Frame):
    MAZE_FILE_PATH = "src/data"
    TEXTS = ["Choose existing maze:", "Generate Existing Maze"]
    
    def __init__(self, parent, command, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.command = command
        self.label = None
        self.combobox = None
        self.button = None
        self.var = StringVar()
        self.filenames = []
        self.wallTables = {}

    def grid(self, *args, **kwargs):
        self.setup_frame()
        super().grid(*args, **kwargs)
        
    def setup_frame(self):
        self.label = ttk.Label(self, text=MazeFileframe.TEXTS[0])
        self.load_files()
        self.combobox = ttk.Combobox(self, values=self.filenames, textvariable=self.var)
        self.combobox.set(self.filenames[0])
        self.button = ttk.Button(self, text=MazeFileframe.TEXTS[1], command=self.run_command)
        
        self.label.grid(row=0, column=0, padx=10, pady=5)
        self.combobox.grid(row=1, column=0, padx=10, pady=5)
        self.button.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        
    def load_files(self):
        self.filenames = [os.path.splitext(filename)[0] for filename in os.listdir(MazeFileframe.MAZE_FILE_PATH) if filename.endswith(".txt")]
        self.filenames.sort(key=lambda filename: int(filename[4:]))
        
        for filename in self.filenames:
            try:
                with open(f"src/data/{filename}.txt", "r") as file:
                    data = file.read()
                    self.wallTables[filename] = [[int(char) for char in row] for row in data.split("\n")]
                
            except Exception as error:
                print(f"File \"{filename}\" cannot be read: {error}")       
    
    def run_command(self):
        wallTable = self.wallTables[self.file_name]
        self.command(wallTable)

    @property
    def file_name(self):
        return self.var.get()
