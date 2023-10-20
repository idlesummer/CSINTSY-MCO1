from algorithms.utils.node import *
from algorithms.utils.frontier import *
from gui.maze_frame import *

class Algorithm:
    NAME = "Best-First Search"
        
    @staticmethod
    def evaluation_function(x1, y1, x2, y2):
        return abs(x1 - x2) + (y1 - y2)
    
    @staticmethod    
    def solve(source, target, wallTable):        
        action = Algorithm.evaluation_function(*source, *target)
        start = Node(state=source, parent=None, action=action)
        frontier = HeapFrontier()
        frontier.add(start)
        
        explored = set()
        solution = []
        
        while True:
            if frontier.empty():
                return None
            
            node = frontier.remove()
            
            if node.state == target:
                solution = []
                while node.parent is not None:
                    solution.append(node.state)
                    node = node.parent
                solution.reverse()
                return solution
            
            explored.add(node.state)
            
            for action, state in Mazeframe.get_neighbors(node.state, wallTable):
                if state not in explored:
                    action = Algorithm.evaluation_function(*source, *target)
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
