from algorithms.utils.node import *
from algorithms.utils.frontier import *
from gui.maze_frame import *

class Algorithm:
    NAME = "A-Star Search"
    
    @staticmethod
    def actual_cost(node):
        totalCost, actualCost = node.value
        return actualCost + 1
    
    @staticmethod
    def heuristic(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    @staticmethod
    def evaluation_function(node, state, target):
        actualCost = Algorithm.actual_cost(node)
        return actualCost + Algorithm.heuristic(*state, *target), actualCost
    
    @staticmethod
    def solve(source, target, wallTable):
        heuristic = Algorithm.heuristic(*source, *target)
        start = Node(state=source, parent=None, value=(heuristic, 0))
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
                    totalCost, actualCost = Algorithm.evaluation_function(node, state, target)
                    child = Node(state=state, parent=node, value=(totalCost, actualCost))
                    frontier.add(child)
                    
        return None, None
            
            
        