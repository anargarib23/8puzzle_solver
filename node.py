import numpy as np


class Node:
    """
    This class, representing a node of the searched graph (specifically, the tree), contains
    information about the state of the game.

    Attributes
    ----------
    visited : bool
        signifies if the node is already visited midst the search
    children : Node[]
        stores the nodes whose states caused by that of the current node. I.e., children of the current node.
    state : np.array
        2D array storing the arrangement of numbers. A state of the game.
    pos0 : (int, int)
        tuple containing the row and column position of the '0' a.k.a. the empty square.
    parent : Node
        the node whose state caused that of the current node. I.e., parent of the current node.
    origin : str
        holds the information of which movement of the '0' generated the state of the current node. E.g., if
        origin == 'left' then moving the '0' to the left has caused the state of this node. Used to avoid generating
        trivial states while searching.
    """

    visited = False
    children = []

    def __init__(self, state, pos0, parent, origin):
        self.state = state
        self.pos0 = pos0
        self.parent = parent
        self.origin = origin


def createStateToRight(node, pos0) -> Node:
    """
    Generates a new state by moving the '0' to the right.

    :param node: node that contains the state in which the '0' shall be moved.
    :param pos0: the position of the '0' in the state.
    :return: a new node in whose state the '0' has been moved to the right.
    """

    # row and column positions of the '0' are stored in i, j.
    i, j = pos0[0], pos0[1]

    if j == 2:
        # if the '0' is in the rightmost column then do nothing.
        return None

    if node.origin == 'left':
        '''
        if the current state has been formed via moving the '0' to the left in the parent state,
        then do nothing. Because moving to the right in this case would be reversing the previous move
        which creates a repeated state that inhibits the performance of search.
        '''

        return None

    new_state = np.copy(node.state)

    # classical approach to replacing array elements
    temp = new_state[i, j]
    new_state[i, j] = new_state[i, j + 1]
    new_state[i, j + 1] = temp

    return Node(new_state, (i, j + 1), node, 'right')


def createStateToLeft(node, pos0) -> Node:
    """
     Generates a new state by moving the '0' to the left.

    :param node: node that contains the state in which the '0' shall be moved.
    :param pos0: the position of the '0' in the state.
    :return: a new node in whose state the '0' has been moved to the left.
    """

    i, j = pos0[0], pos0[1]

    if j == 0:
        return

    if node.origin == 'right':
        '''
        if the current state has been formed via moving the '0' to the right in the parent state,
        then do nothing. Because moving to the left in this case would be reversing the previous move
        which creates a repeated state that inhibits the performance of search.
        '''
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i, j - 1]
    new_state[i, j - 1] = temp

    return Node(new_state, (i, j - 1), node, 'left')


def createStateToDown(node, pos0):
    """
    Generates a new state by moving the '0' to the down.

    :param node: node that contains the state in which the '0' shall be moved.
    :param pos0: the position of the '0' in the state.
    :return: a new node in whose state the '0' has been moved to the down.
    """

    i, j = pos0[0], pos0[1]

    if i == 0:
        return None

    if node.origin == 'up':
        '''
        if the current state has been formed via moving the '0' to the up in the parent state,
        then do nothing. Because moving to the down in this case would be reversing the previous move
        which creates a repeated state that inhibits the performance of search.
        '''
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i - 1, j]
    new_state[i - 1, j] = temp

    return Node(new_state, (i - 1, j), node, 'down')


def createStateToUp(node, pos0):
    """
    Generates a new state by moving the '0' to the up.

    :param node: node that contains the state in which the '0' shall be moved.
    :param pos0: the position of the '0' in the state.
    :return: a new node in whose state the '0' has been moved to the up.
    """

    i, j = pos0[0], pos0[1]

    if i == 2:
        return None

    if node.origin == 'down':
        '''
        if the current state has been formed via moving the '0' to the down in the parent state,
        then do nothing. Because moving to the up in this case would be reversing the previous move
        which creates a repeated state that inhibits the performance of search.
        '''
        return None

    new_state = np.copy(node.state)

    temp = new_state[i, j]
    new_state[i, j] = new_state[i + 1, j]
    new_state[i + 1, j] = temp

    return Node(new_state, (i + 1, j), node, 'up')


def getPossibleStates(node) -> [Node]:
    """
    Returns a list of possible sub-nodes (children) of the given node.
    Before returning the list, the function creates such nodes.

    :param node: node whose potential sub-nodes shall be returned
    :return: a list of nodes that contains the sub-nodes of the given one
    """

    nodes = []
    nodes += filter(None, [createStateToLeft(node, node.pos0), createStateToRight(node, node.pos0),
                           createStateToUp(node, node.pos0), createStateToDown(node, node.pos0)])
    return nodes


def allVisited(nodes) -> bool:
    """
    Given a list of nodes, the function investigates whether every node in the list has been marked visited.
    Used in the DFS algorithm while backtracking.

    :param nodes: list of the given nodes.
    :return: bool that indicates whether all nodes in the given list are marked visited.
    """

    for node in nodes:
        if not node.visited:
            return False

    return True
