import heapq

#Make sure to use GRID_SIZE_DEF+2 for the size parameter
def BestFirstSearch(WallTable, size):
    # Tuple Format: (h(n), x, y, parent_x, parent_y)
    priority_heap = [((size - 3) * 2, 1, 1, None, None)]
    heapq.heapify(priority_heap)
    parent = [[None, None] * (size + 2) for _ in range(size + 2)]
    visited = {(1, 1)}

    while priority_heap:
        current = heapq.heappop(priority_heap)
        row_index, col_index = current[1], current[2]
        parent_row, parent_col = current[3], current[4]
        parent[row_index][col_index] = [parent_row, parent_col]

        if row_index == size-2 and col_index == size-2:
            shortest_path = []
            node =  [size-2, size-2]
            while node[0] != None:
                shortest_path.append(node)
                node = parent[node[0]][node[1]]
            return shortest_path

        # Check each adjacent cell if they are walls, if not push to heap alongside h(n)
        valid_moves = []
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row_index + i, col_index + j
            if (WallTable[new_row][new_col] == 0) and ((new_row, new_col) not in visited):
                manhattan = (size - new_row - 2) + (size - new_col - 2)
                heapq.heappush(priority_heap, (manhattan, new_row, new_col, row_index, col_index))
                visited.add((new_row, new_col))
    
    return None

WallTable = [
    #0 1 2 3 4 5 6 7 8 9 0 1 2 3
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,1,1,0,1],
    [1,1,1,1,1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,0,0,1],
    [1,0,1,0,0,0,1,0,1,0,1,0,1,1],
    [1,0,1,0,1,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,1,1,1,0,1,1,0,1],
    [1,0,1,1,1,0,1,0,0,0,1,0,0,1],
    [1,0,0,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,0,0,1,1,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


result = BestFirstSearch(WallTable, 14)
if result is not None:
    for i in result:
        print(i[0], i[1])
else:
    print("Error")