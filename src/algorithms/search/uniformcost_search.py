from algorithms.utils.node import *
from algorithms.utils.frontier import *
from gui.maze_frame import *

class Algorithm:
    NAME = "Uniform-Cost Search"       
    
    @staticmethod
    def evaluation_function(node):
        actualCost, _ = node.value
        return actualCost + 1
    
    @staticmethod
    def solve(source, target, wallTable):
        start = Node(state=source, parent=None, value=(0, None))
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
                    actualCost = Algorithm.evaluation_function(node)
                    child = Node(state=state, parent=node, value=(actualCost, None))
                    frontier.add(child)
                    
        return None, None
