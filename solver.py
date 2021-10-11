import numpy as np
import time
from node import allVisited, getPossibleStates

goal_table = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


def isSolveable(initial_state):
    array = np.ravel(initial_state)
    inversions = 0

    for i in range(0, 9):
        for j in range(i + 1, 9):
            if array[i] != 0 and array[j] != 0 and array[i] > array[j]:
                inversions += 1

    return inversions % 2 == 0


def isSolution(solution_state):
    return np.array_equal(solution_state, goal_table)


def solveBFS(start):
    q = [start]

    while len(q) != 0:
        front = q[0]

        if isSolution(front.state):
            return front

        if len(front.children) == 0:
            front.children = getPossibleStates(q.pop(0))

        q += front.children

    return None


def solveDFS(start):
    s = [start]

    while len(s) != 0:
        top = s[-1]
        # print(peek.table)

        if isSolution(top.state):
            return top

        if len(top.children) == 0 and len(s) < 30:
            top.children = getPossibleStates(top)

        if len(top.children) == 0 or allVisited(top.children):
            s.pop()

        for st in top.children:
            if not st.visited:
                st.visited = True
                s.append(st)
                break

        # time.sleep(2)

    return None


def trackSolution(end):
    nodes = []
    current = end

    while current is not None:
        nodes.append(current)
        current = current.parent

    nodes.reverse()

    return nodes
