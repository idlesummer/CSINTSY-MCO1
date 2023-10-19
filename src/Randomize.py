import random

#Make sure to use GRID_SIZE_DEF+2 for the size parameter
def randomizeWalls(wallTable, size):
    #All (even,even) cells except for the goal (if applicable), are walls
    #All (odd,odd) cells are not walls
    #(odd,even) and (even,odd) cells have a 30% chance of being walls
    for i in range(1,size):
        for j in range(1,size):
            if (i != 1 and j != 1) or (i != size and j!= size):
                if i%2 == 0 and j%2 == 0:
                    wallTable[i][j] = 1
                elif i%2 ==1 and j%2 == 1:
                    wallTable[i][j] = 0
                else:
                    chance = random.randint(0,9)
                    if chance > 6:
                        wallTable[i][j] = 1

    return wallTable

def updateCells(cellTable, wallTable, size):
    for i in range(1,size-1):
        for j in range(1,size-1):
            if wallTable[i][j] == 1:
                cellTable[i][j].select()
    return cellTable