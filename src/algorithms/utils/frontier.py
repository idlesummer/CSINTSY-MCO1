import heapq


class HeapFrontier:
    def __init__(self):
        self.frontier = []
        self.states = set()
        
    def add(self, node):
        totalCost, actualCost = node.value
        heapq.heappush(self.frontier, (totalCost, node))
        self.states.add(node.state)

    def contains(self, state):
        return state in self.states

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            return None
        _, node = heapq.heappop(self.frontier)       
        self.states.remove(node.state)
        return node
