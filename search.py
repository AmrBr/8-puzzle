import random
import numpy as np

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
