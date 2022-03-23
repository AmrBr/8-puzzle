import time
import math


# Count number of inversions in the given state
def countInversions(boardState):
    intState = []
    for i in range(len(boardState)):
        if boardState[i] != '0':
            intState.append(boardState[i])
    inversions = 0
    for i in range(len(intState)):
        for j in range(i + 1, len(intState)):
            if intState[i] > intState[j]:
                inversions += 1
    return inversions


# Check if the current state is solvable or not
# if number of inversions is Odd --> unsolvable
def isSolvable(boardState):
    inversions = countInversions(boardState)
    if inversions % 2 == 1:
        return False
    return True


# Swap 2 tiles (tile 1 index (index1), tile 2 index (index2))
def swap(boardState, index1, index2):
    tempState = list(boardState)
    tempState[index1], tempState[index2] = tempState[index2], tempState[index1]
    return ''.join(tempState)


# Get all possible next states (children) of the current board state
# By finding the location of the empty tile (0) and swapping with each adjacent tile depending on the position
def getChildren(boardState):
    nextStates = []
    index = boardState.find('0')
    row = index // 3
    col = index % 3

    # Swap with upper tile
    if row > 0:
        nextStates.append(swap(boardState, index, index - 3))

    # Swap with lower tile
    if row <= 1:
        nextStates.append(swap(boardState, index, index + 3))

    # Swap with right tile
    if col <= 1:
        nextStates.append(swap(boardState, index, index + 1))

    # Swap with left tile
    if col > 0:
        nextStates.append(swap(boardState, index, index - 1))
    return nextStates


# Check if the current board state is the goal state
def isGoal(boardState):
    tiles = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    goalState = ''.join(tiles)
    return boardState == goalState


# Finding Path from goal state (012345678) up to the root node
def findPath(pMap):
    child = '012345678'
    parent = pMap[child]
    path = [child]
    while not parent == child:  # if parent not equal to child (starting node not reached yet) then continue
        child = parent
        parent = pMap[child]
        path.append(child)
    return path


# Represent Board State
def printBoard(boardState):
    print('-------------')
    for i in range(1, 10):
        if boardState[i - 1] == '0':
            print('| ', end='\t')
        else:
            print('| ' + boardState[i - 1], end='\t')
        if i % 3 == 0:
            print('|')
            print('-------------')


# Breadth-First-Search Algorithm
def BFS(boardState):
    time1 = time.time()  # Starting time
    frontier = []  # Frontier list
    oFrontier = set()  # Optimizing Frontier with datatype 'set()' rather than 'list' used to improve search time
    explored = set()
    frontier.append(boardState)
    oFrontier.add(boardState)
    pMap = {boardState: boardState}  # Dictionary used to link each node with its parent in the form (child: parent)
    while len(frontier):
        state = frontier.pop(0)  # Pop first element from the list (to imitate queue)
        oFrontier.remove(state)  # Remove the same element from the optimizing frontier set
        explored.add(state)
        if isGoal(state):  # if current state is the goal state --> break
            break
        children = getChildren(state)  # Get all children of current state
        for child in children:
            if child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                frontier.append(child)  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state  # Store the child with the current state as the parent node
    time2 = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    for i in range(len(path)):  # Print each state in the path
        print(f'Step Number: {i + 1}')
        printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {len(path) - 1}')  # depth of search equal cost since the tree is checked level by level
    print(f'BFS Running time = {time2 - time1} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardState)


# Depth-First-Search Algorithm
def DFS(boardState):
    time1 = time.time()  # Starting time
    frontier = []  # Frontier list
    oFrontier = set()  # Optimizing Frontier with datatype 'set()' rather than 'list' used to improve search time
    explored = set()
    frontier.append(boardState)
    oFrontier.add(boardState)
    pMap = {boardState: boardState}  # Dictionary used to link each node with its parent in the form (child: parent)
    while len(frontier):
        state = frontier.pop()  # Pop last element from the list (to imitate stack)
        oFrontier.remove(state)  # Remove the same element from the optimizing frontier set
        explored.add(state)
        if isGoal(state):  # if current state is the goal state --> break
            break
        children = getChildren(state)  # Get all children of current state
        for child in children:
            if child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                frontier.append(child)  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state
    time2 = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    for i in range(len(path)):  # Print each state in the path
        print(f'Step Number: {i + 1}')
        printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = ')
    print(f'DFS Running time = {time2 - time1} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardState)


# Calculate Manhattan distance
def manhattanHeuristic(boardState):
    heuristic = 0
    for i in range(len(boardState)):
        mainRow = int(boardState[i]) // 3  # row index of element i in the goal state
        mainCol = int(boardState[i]) % 3  # column index of element i in the goal state
        row = i // 3  # row index of element i in the current state
        col = i % 3  # column index of element i in the current state
        if boardState[i] != '0':
            heuristic += abs(mainRow - row) + abs(mainCol - col)
    return heuristic


# Calculate Euclidean distance
def euclideanHeuristic(boardState):
    heuristic = 0
    for i in range(len(boardState)):
        mainRow = int(boardState[i]) // 3  # row index of element i in the goal state
        mainCol = int(boardState[i]) % 3  # column index of element i in the goal state
        row = i // 3  # row index of element i in the current state
        col = i % 3  # column index of element i in the current state
        if boardState[i] != '0':
            heuristic += math.sqrt(abs(mainRow - row) ** 2 + abs(mainCol - col) ** 2)
    return heuristic

