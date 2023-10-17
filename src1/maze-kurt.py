import random


def generate_maze(size):
    #Generate an initial grid with all cells having four "walls"
    #Walls:   North  West   South  East  || Visited or Not
    maze = [[[False, False, False, False,   False] for _ in range(size)] for _ in range(size)]

    #Generate Connected Maze using DFS
    stack = [[0,0]]
    current = [0,0] #(y,x)
    while stack:
        #mark current node as visited
        maze[current[0]][current[1]][4] = True

        #choose a valid node that was not visited randomly
        direction = random.randint(0, 3)
        isValidDirection = False
        takes = 0
        while isValidDirection == False and takes < 4:
            #Go North
            if direction == 0:
                if current[0] - 1 >= 0:
                    if maze[current[0]-1][current[1]][4] == False:
                        isValidDirection = True
                        maze[current[0]][current[1]][0] = True
                        current[0] -= 1
                        maze[current[0]][current[1]][2] = True

            #Go West
            elif direction == 1:
                if current[1] - 1 >= 0:
                    if maze[current[0]][current[1]-1][4] == False:
                        isValidDirection = True
                        maze[current[0]][current[1]][1] = True
                        current[1] -= 1
                        maze[current[0]][current[1]][3] = True

            #Go South
            elif direction == 2:
                if current[0] + 1 < size: 
                    if maze[current[0]+1][current[1]][4] == False: 
                        isValidDirection = True
                        maze[current[0]][current[1]][2] = True
                        current[0] += 1
                        maze[current[0]][current[1]][0] = True

            #Go East
            elif direction == 3:
                if current[1] + 1 < size:
                    if maze[current[0]][current[1]+1][4] == False:
                        isValidDirection = True
                        maze[current[0]][current[1]][3] = True
                        current[1] += 1
                        maze[current[0]][current[1]][1] = True
            takes += 1
            direction = (direction + 1) % 4
        
        #If dead-end or the goal state
        if not isValidDirection or current == [size-1, size-1]:
            if current == [size-1, size-1]:
                print(f"Reached goal: {current}")
                maze[current[0]][current[1]][4] = True
            current = stack.pop()
            print(stack)
        #If valid direction add to stack
        else:
            stack.append([current[0],current[1]])
            print(stack)

    return maze


def main():
    #idk how to get input in python but assign it to n
    #n = input()
    maze = generate_maze(5)

    # for i in range(5):
    #     for j in range(5):
    #         print(maze[i][j])
    #     print("-------------------------------------------------------")
    
    #idk how to get input in python but assign it to n
    n = int(input("Maze Size: "))
    maze = generate_maze(n)
    for i in range(n):
        print("___", end = '')
    
    for i in range(n):
        print(" ")
        print("|", end = '')
        for j in range(n):
            if maze[i][j][2] == False:
                print("__", end = '')
            else:
                print("  ", end = '')
            
            if maze[i][j][3] == False:
                print("|", end = '')
            else:
                if maze[i][j][2] == False:
                    print("_", end = '')
                else:
                    print(" ", end = '')
  
  
if __name__ == "__main__":
    main()
