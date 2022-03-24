from search import *
import time
import heapq
import math


def A_star(boardstate, heuristic):
    maxDep = 0
    Start_time = time.time()
    frontier = []   # Frontier list
    oFrontier = set()   # Optimizing Frontier with datatype 'set()' rather than 'list' used to improve search time
    explored = set()
    frontier.append([boardstate, 0, 0]) #appending  boardstate, heuristic, depth
    oFrontier.add(boardstate)
    pMap = {boardstate: boardstate}
    while len(frontier):
        frontier.sort(key=lambda x: x[1])   #sorting heap ascendingly according to total cost
        state = frontier.pop(0)  # Pop first element from the list (to imitate queue)
        oFrontier.remove(state[0])  # Remove the same element from the optimizing frontier set
        explored.add(state[0])
        if isGoal(state[0]):  # if current state is the goal state --> break
            break
        children = getChildren(state[0])  # Get all children of current state
        for child in children:
            if child in oFrontier:
                temp=[]
                for i in range(len(frontier)):
                    if frontier[i][0]==child:
                        break
                        #temp=frontier[i].copy()
                frontier[i]=[child,min(frontier[i][1],heuristic(child)+state[2]+1,)]

                #temp=frontier.pop(frontier.index('child'))
                compare=min(temp[1], heuristic(child)+state[2]+1)
                if compare == temp[1]:
                    frontier[i]([temp[0],temp[1],temp[2]])
                else:
                    frontier.append([child, heuristic(child)+state[2]+1, state[2]+1])
            elif child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                maxDep = max(maxDep,state[2])  # maximum depth is the max of current max depth or level of current state
                frontier.append([child, heuristic(child)+state[2]+1, state[2]+1])  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state[0]  # Store the child with the current state as the parent node
    end_time = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    for i in range(len(path)):  # Print each state in the path
        print(f'Step Number: {i + 1}')
        printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {maxDep}')  # depth of search equal cost since the tree is checked level by level
    print(f'A* Running time = {end_time - Start_time} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardstate)
