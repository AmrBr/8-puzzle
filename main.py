from search import *
import random


# Generate random board state
tiles = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
random.shuffle(tiles)
randomState = ''.join(tiles)

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
