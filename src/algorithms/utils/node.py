class Node():
    def __init__(self, state, parent, action=None, value=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.value = value
        
    def __lt__(self, other):
        return self.action < other.action
