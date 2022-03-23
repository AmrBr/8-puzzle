from search import *

randomState = generateRandomState()

print('Solving: ')
printBoard(randomState)
if not isSolvable(randomState):
    print('This state is Unsolvable! (Odd number of inversions)')
else:
    print('Select Method:')
    print('1) BFS')
    print('2) DFS')
    print('3) A* (Manhattan Distance Heuristic)')
    print('4) A* (Euclidean Distance Heuristic)')
    choice = input('Choice: ')
    if choice == '1':
        BFS(randomState)
    elif choice == '2':
        DFS(randomState)
    else:
        print('')
