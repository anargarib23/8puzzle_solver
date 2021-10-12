import os
from datetime import datetime

import solver
import ui
from node import *
from solver import isSolveable

'''
---Goal State in This Problem---
 _____ _____ _____
|     |     |     |
|  1  |  2  |  3  |
|_____|_____|_____|
|     |     |     |
|  4  |  5  |  6  |
|_____|_____|_____|
|     |     |     |
|  7  |  8  |  0  |
|_____|_____|_____|

sample 1: [[1, 2, 3], [0, 4, 6], [7, 5, 8]], (1, 0)
sample 2: [[1, 2, 3], [5, 6, 0], [7, 8, 4]], (1, 2)
sample 3: [[1, 8, 2], [0, 4, 3], [7, 6, 5]], (1, 0)
sample 4: [[7, 2, 4], [5, 0, 6], [8, 3, 1]], (1, 1);
'''

os.system('color a')

samples = [np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]]),
           np.array([[1, 2, 3], [5, 6, 0], [7, 8, 4]]),
           np.array([[1, 8, 2], [0, 4, 3], [7, 6, 5]]),
           np.array([[7, 2, 4], [5, 0, 6], [8, 3, 1]])]

# it will hold the user input data
args = {}
print("Pick the initial state from:\n[1] Samples (4 available);\n[2] Random generator\n[3] Input")

args['start'] = int(input())

# Deciding how the initial state is to be generated. From samples, randomized, or manually.
if args['start'] == 1:
    print("Select the sample:\n1 2 3 4")
    initial_state = samples[int(input()) - 1]

elif args['start'] == 2:
    initial_state = np.random.default_rng().choice(9, size=9, replace=False).reshape(3, 3)

elif args['start'] == 3:
    # input 2D array
    print("Enter input (3x3):")
    initial_state = np.array([input().split() for _ in range(3)], int)

else:
    os.system('exit')

# find the position of the '0' in the state
initial_pos0 = tuple(*np.argwhere(initial_state == 0))

print("---Initial State---")
ui.displayTable(initial_state)

if not isSolveable(initial_state):
    print("The puzzle is not solvable.")
    exit()

root_node = Node(initial_state, initial_pos0, None, None)

print("Choose algorithm:\n[1] BFS\n[2] DFS")

args['alg'] = int(input())
start_time = datetime.now()

if args['alg'] == 1:
    solution_node = solver.solveBFS(root_node)
elif args['alg'] == 2:
    print("Enter depth limit:")
    args['depth'] = int(input())
    solution_node = solver.solveDFS(root_node, args['depth'])

    if solution_node is None:
        print("No solution found for depth: ", args['depth'])
        exit()
else:
    os.system('exit')

finish_time = datetime.now()
final_nodes = solver.trackSolution(solution_node)

print("---Solution---")

for node in final_nodes:
    ui.displayTable(node.state)

print("# of steps: " + str(len(final_nodes) - 1))
print("Time elapsed: " + str((finish_time - start_time).total_seconds()))

os.system('pause')
