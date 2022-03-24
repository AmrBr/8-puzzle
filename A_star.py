from search import *
import time
import heapq
import math


def takeSecond(list):
    return list[1]


def A_star(boardstate, heuristic):
    maxDep = 0
    Start_time = time.time()
    frontier = []
    oFrontier = set()
    explored = set()
    frontier.append([boardstate, 0])
    oFrontier.add(boardstate)
    pMap = {boardstate: boardstate}
    while len(frontier):
        frontier.sort(key=lambda x: x[1])
        #print(frontier)
        state = frontier.pop(0)  # Pop first element from the list (to imitate queue)
        oFrontier.remove(state[0])  # Remove the same element from the optimizing frontier set
        explored.add(state[0])
        if isGoal(state[0]):  # if current state is the goal state --> break
            #printBoard(state[0])
            break
        children = getChildren(state[0])  # Get all children of current state
        for child in children:
            if child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                maxDep = max(maxDep,state[1])  # maximum depth is the max of current max depth or level of current state
                if heuristic == 'manhattan':
                    frontier.append([child, manhattanHeuristic(state[0])])  # if not found add child to frontier and oFrontier
                elif heuristic == 'euclidean':
                    frontier.append([child, euclideanHeuristic(state[0])])  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state[0]  # Store the child with the current state as the parent node
    end_time = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    for i in range(len(path)):  # Print each state in the path
        printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {maxDep}')  # depth of search equal cost since the tree is checked level by level
    print(f'A* Running time = {end_time - Start_time} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardstate)
