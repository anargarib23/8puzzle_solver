import numpy as np

class Node:
    visited = False
    children = []

    def __init__(self, state, pos0, parent, origin):
        self.state = state
        self.pos0 = pos0
        self.parent = parent
        self.origin = origin


def createStateToRight(node, pos0):
    i, j = pos0[0], pos0[1]

    if j == 2:
        return None

    if node.origin == 'left':
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i, j + 1]
    new_state[i, j + 1] = temp

    return Node(new_state, (i, j + 1), node, 'right')


def createStateToLeft(node, pos0):
    i, j = pos0[0], pos0[1]

    if j == 0:
        return

    if node.origin == 'right':
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i, j - 1]
    new_state[i, j - 1] = temp

    return Node(new_state, (i, j - 1), node, 'left')

def createStateToDown(node, pos0):
    i, j = pos0[0], pos0[1]

    if i == 0:
        return None

    if node.origin == 'up':
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i - 1, j]
    new_state[i - 1, j] = temp

    return Node(new_state, (i - 1, j), node, 'down')


def createStateToUp(node, pos0):
    i, j = pos0[0], pos0[1]

    if i == 2:
        return None

    if node.origin == 'down':
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i + 1, j]
    new_state[i + 1, j] = temp

    return Node(new_state, (i + 1, j), node, 'up')


def getPossibleStates(node):
    nodes = []
    nodes += filter(None, [createStateToLeft(node, node.pos0), createStateToRight(node, node.pos0),
                           createStateToUp(node, node.pos0), createStateToDown(node, node.pos0)])
    return nodes

def allVisited(nodes):
    for node in nodes:
        if not node.visited:
            return False

    return True