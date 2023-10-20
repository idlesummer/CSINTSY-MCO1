import os
import importlib


class MazeSolver:
    ALGO_FILE_PATH = "src/algorithms/search"
    
    def __init__(self):
        self.algorithms = {}
    
    def load_files(self):
        files = [file for file in os.listdir(MazeSolver.ALGO_FILE_PATH) if file.endswith(".py") ]
        
        for file in files:
            package = MazeSolver.ALGO_FILE_PATH.replace("/", ".")[4:]
            name = file[:-3]
            module = importlib.import_module(f"{package}.{name}")
            self.algorithms[module.Algorithm.NAME] = module.Algorithm.solve
        
    def solve(self, algoName, wallTable):
        solve = self.algorithms[algoName]
        solve(wallTable)
        
    @property
    def algonames(self):
        algonames = list(self.algorithms.keys())
        return algonames
