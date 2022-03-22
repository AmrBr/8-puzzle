from search import *
import random


# Generate random board state
# tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(tiles)
# randomState = np.array(tiles).reshape(3, 3)

temp = [4, 3, 8, 0, 1, 2, 5, 6, 7]
# randomState = np.array(temp).reshape(3, 3)
randomState = '438012567'
DFS(randomState)
