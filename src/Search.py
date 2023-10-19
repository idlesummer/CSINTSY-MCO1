import heapq

def BestFirstSearch(WallTable, size):
    # Tuple Format: (h(n), x, y, parent_x, parent_y)
    priority_heap = [((size - 1) * 2, 1, 1, None, None)]
    heapq.heapify(priority_heap)
    shortest_path = []
    visited = {(1, 1)}

    while priority_heap:
        current = heapq.heappop(priority_heap)
        row_index, col_index = current[1], current[2]
        parent_row, parent_col = current[3], current[4]
        shortest_path.append((row_index, col_index, parent_row, parent_col))

        if row_index == size-2 and col_index == size-2:
            return shortest_path

        # Check each adjacent cell if they are walls, if not push to heap alongside h(n)
        valid_moves = []
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row_index + i, col_index + j
            if (WallTable[new_row][new_col] == 0) and ((new_row, new_col) not in visited):
                manhattan = (size - new_row) + (size - new_col)
                valid_moves.append((manhattan, new_row, new_col, row_index, col_index))
                visited.add((new_row, new_col))

        if not valid_moves:
            parent_row, parent_col = shortest_path[-1][2], shortest_path[-1][3]
            shortest_path.pop()
        else:
            for element in valid_moves:
                heapq.heappush(priority_heap, element)

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