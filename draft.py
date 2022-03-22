import math


def getElement(boardState, index):
    numberOfDigits = int(math.log10(boardState))
    if numberOfDigits == 7:
        if index == 1:
            return 0
        digit = int((boardState / pow(10, numberOfDigits - (index - 2))) % 10)
    else:
        digit = int((boardState / pow(10, numberOfDigits - (index - 1))) % 10)
    return digit


temp = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]


# -------------------------------------------------------------------------------------------------
import numpy as np

# temp = [4, 3, 8, 0, 1, 2, 5, 6, 7]
randomState = '438012567'


# Swap 2 tiles (tile 1 index (row1, col1), tile 2 index (row2, col2))
def swap(boardState, row1, col1, row2, col2):
    tempState = boardState.copy()
    tempState[row1][col1], tempState[row2][col2] = tempState[row2][col2], tempState[row1][col1]
    return tempState


# Get all possible next states (children) of the current board state
# By finding the location of the empty tile (0) and swapping with each adjacent tile depending on the position
def getChildren(boardState):
    nextStates = []
    row = int(np.where(boardState == 0)[0])
    col = int(np.where(boardState == 0)[1])

    # Swap with upper tile
    if row > 0:
        nextStates.append(swap(boardState, row, col, row - 1, col))

    # Swap with lower tile
    if row <= 1:
        nextStates.append(swap(boardState, row, col, row + 1, col))

    # Swap with right tile
    if col <= 1:
        nextStates.append(swap(boardState, row, col, row, col + 1))

    # Swap with left tile
    if col > 0:
        nextStates.append(swap(boardState, row, col, row, col - 1))
    return nextStates


# Check if the current board state is the goal state
def isGoal(boardState):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    goalState = np.array(arr).reshape(3, 3)
    return (boardState == goalState).all()


def isFound(boardState, listOfStates):
    for state in listOfStates:
        if (state == boardState).all():
            return True
    return False


def findPath(pMap):
    print('hello')
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    test = (np.array(arr).reshape(3, 3))
    child = tuple(map(tuple, test))
    parent = pMap[child]
    path = [child]
    while not parent == child:
        child = parent.copy()
        parent = pMap[child]
        path.append(child)
    return path


def BFS(boardState):
    frontier = []
    explored = []
    frontier.append(boardState)
    while len(frontier):
        state = frontier.pop(0)
        explored.append(state)
        if isGoal(state):
            print(state)
            break
        children = getChildren(state)
        for child in children:
            if not isFound(child, frontier) and not isFound(child, explored):
                frontier.append(child)
    print('hello')


# --------------------------------------------------------------------------------------------
def BFS(boardState):
    time1 = time.time()
    frontier = []
    explored = set()
    frontier.append(boardState)
    oFrontier.add(boardState)
    pMap = {boardState: boardState}
    while len(frontier):
        state = frontier.pop(0)
        explored.add(state)
        if isGoal(state):
            break
        children = getChildren(state)
        for child in children:
            if child not in frontier and child not in explored:
                frontier.append(child)
                pMap[child] = state
    time2 = time.time()
    path = findPath(pMap)
    path.reverse()
    for i in range(len(path)):
        print(f'Step Number: {i+1}')
        printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {len(path) - 1}')
    print(f'BFS Running time = {time2 - time1} sec')
    print('Starting Board State: ')
    printBoard(boardState)
