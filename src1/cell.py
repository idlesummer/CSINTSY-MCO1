class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
    
    def __str__(self):
        return "f({x},{y})"
