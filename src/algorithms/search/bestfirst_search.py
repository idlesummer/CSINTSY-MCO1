from algorithms.utils.node import *
from algorithms.utils.frontier import *
from gui.maze_frame import *

class Algorithm:
    NAME = "Greedy Best-First Search"
        
    @staticmethod
    def evaluation_function(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    @staticmethod    
    def solve(source, target, wallTable):        
        action = Algorithm.evaluation_function(*source, *target)
        start = Node(state=source, parent=None, action=action)
        frontier = HeapFrontier()
        frontier.add(start)
        
        explored = set()
        visited = []
        solution = []
        
        while not frontier.empty():            
            node = frontier.remove()
            
            if node.state == target:
                solution = []
                while node.parent is not None:
                    solution.append(node.state)
                    node = node.parent
                solution.reverse()
                return visited, solution
            
            explored.add(node.state)
            visited.append(node.state)
            
            for action, state in Mazeframe.get_neighbors(node.state, wallTable):
                if not frontier.contains(state) and state not in explored:
                    action = Algorithm.evaluation_function(*state, *target)
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
                    
        return None, None
