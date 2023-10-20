class Algorithm:
    NAME = "Best-First Search"
    
    @staticmethod
    def f(x1, y1, x2, y2):
        return abs(x1 - x2) + (y1 - y2)
    
    @staticmethod    
    def solve(source, target, wallTable):
        pass