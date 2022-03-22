import time


# Swap 2 tiles (tile 1 index (row1, col1), tile 2 index (row2, col2))
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


def isFound(boardState, listOfStates):
    for state in listOfStates:
        if (state == boardState).all():
            return True
    return False


def findPath(pMap):
    child = '012345678'
    parent = pMap[child]
    path = [child]
    while not parent == child:
        child = parent
        parent = pMap[child]
        path.append(child)
    return path


def printBoard(boardState):
    print('-------------')
    for i in range(1, 10):
        print('| ' + boardState[i-1], end='\t')
        if i % 3 == 0:
            print('|')
            print('-------------')


def BFS(boardState):
    time1 = time.time()
    frontier = []
    oFrontier = set()
    explored = set()
    frontier.append(boardState)
    oFrontier.add(boardState)
    pMap = {boardState: boardState}
    while len(frontier):
        state = frontier.pop(0)
        oFrontier.remove(state)
        explored.add(state)
        if isGoal(state):
            break
        children = getChildren(state)
        for child in children:
            if child not in oFrontier and child not in explored:
                frontier.append(child)
                oFrontier.add(child)
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


def DFS(boardState):
    time1 = time.time()
    frontier = []
    oFrontier = set()
    explored = set()
    frontier.append(boardState)
    oFrontier.add(boardState)
    pMap = {boardState: boardState}
    while len(frontier):
        state = frontier.pop()
        oFrontier.remove(state)
        explored.add(state)
        if isGoal(state):
            break
        children = getChildren(state)
        for child in children:
            if child not in oFrontier and child not in explored:
                frontier.append(child)
                oFrontier.add(child)
                pMap[child] = state
    time2 = time.time()
    path = findPath(pMap)
    path.reverse()
    for i in range(len(path)):
        print(f'Step Number: {i+1}')
        printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = ')
    print(f'DFS Running time = {time2 - time1} sec')
    print('Starting Board State: ')
    printBoard(boardState)
