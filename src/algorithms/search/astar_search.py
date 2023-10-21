from algorithms.utils.node import *
from algorithms.utils.frontier import *
from gui.maze_frame import *

class Algorithm:
    NAME = "A-Star Search"
    
    @staticmethod
    def actual_cost(node):
        return node.value + 1
    
    @staticmethod
    def heuristic(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    @staticmethod
    def evaluation_function(node, state, target):
        actualCost = Algorithm.actual_cost(node)
        print(f"state: {state}, g(n): {actualCost}, h(n): {Algorithm.heuristic(*state, *target)}, f(n): {actualCost + Algorithm.heuristic(*state, *target)}")
        return actualCost, actualCost + Algorithm.heuristic(*state, *target)
    
    @staticmethod
    def solve(source, target, wallTable):
        action = Algorithm.heuristic(*source, *target)
        start = Node(state=source, parent=None, action=action, value=0)
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
                    value, action = Algorithm.evaluation_function(node, state, target)
                    child = Node(state=state, parent=node, action=action, value=value)
                    frontier.add(child)
                    
        return None, None
            
            
        