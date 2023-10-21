import heapq

#Make sure to use GRID_SIZE_DEF+2 for the size parameter
def BestFirstSearch(WallTable, size):
    # Tuple Format: (h(n), row, col, parent_row, parent_col)
    priority_heap = [((size - 3) * 2, 1, 1, None, None)]
    heapq.heapify(priority_heap)

    #List Format: [Parent Row, Parent Col]
    cell_info = [[None, None] * (size + 2) for _ in range(size + 2)]

    #Ordered pairs (row, col)
    visited = {(1, 1)}

    while priority_heap:
        current = heapq.heappop(priority_heap)
        row_index, col_index = current[1], current[2]
        parent_row, parent_col = current[3], current[4]
        cell_info[row_index][col_index] = [parent_row, parent_col]


        #Backtrack using the parent indices
        if row_index == size-2 and col_index == size-2:
            shortest_path = []
            node =  [size-2, size-2]
            while node[0] != None:
                shortest_path.append(node)
                node = cell_info[node[0]][node[1]]
            return shortest_path

        # Check each adjacent cell if they are walls, if not push to heap alongside h(n)
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row_index + i, col_index + j
            if (WallTable[new_row][new_col] == 0) and ((new_row, new_col) not in visited):
                manhattan = (size - new_row - 2) + (size - new_col - 2)
                heapq.heappush(priority_heap, (manhattan, new_row, new_col, row_index, col_index))
                visited.add((new_row, new_col))
    
    return None

#Make sure to use GRID_SIZE_DEF+2 for the size parameter
def AStar(WallTable, size):
    # Tuple Format: (f(n), row, col, parent_row, parent_col)
    priority_heap = [((size - 3) * 2, 1, 1)]
    heapq.heapify(priority_heap)

    #List Format: [Parent Row, Parent Col, g(n) value]
    cell_info = [[[None, None, 5000000] for _ in range(size + 2)] for _ in range(size + 2)]
    cell_info[1][1][2] = 0

    while priority_heap:
        current = heapq.heappop(priority_heap)
        row_index, col_index = current[1], current[2]

        #Backtrack using the parent indices
        if row_index == size-2 and col_index == size-2:
            shortest_path = []
            node =  [size-2, size-2]
            while node[0] != None:
                shortest_path.append(node)
                node = cell_info[node[0]][node[1]]
            return shortest_path

        # Check each adjacent cell if they are walls, if not push to heap alongside h(n)
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row_index + i, col_index + j
            if WallTable[new_row][new_col] == 0:
                g_n = cell_info[row_index][col_index][2] + 1
                if g_n < cell_info[new_row][new_col][2]:
                    cell_info[new_row][new_col] = [row_index, col_index, g_n]
                    heuristic = (size - new_row - 2) + (size - new_col - 2) + g_n
                    heapq.heappush(priority_heap, (heuristic, new_row, new_col))

    return None