import numpy as np
import time
from node import allVisited, getPossibleStates, Node

# the desired state at which the search stops, problem is pronounced solved.
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


def isSolveable(initial_state) -> bool:
    """
    Indicates if the goal state can be yielded from the initial state. I.e., whether the puzzle is solvable.
    It adopts an algorithm to check if the total count of inversions for all numbers within the array is even or odd.
    An inversion is defined as the fact that there is a smaller element than the current one which
    succeeds it within the array. E.g., in the array [1, 2, -1] there's 2 inversions considering the pairs
    (1, -1) & (2, -1). In this problem, the '0' is to be ignored.

    :param initial_state: the state which shall be investigated.
    :return: bool value whether the goal state could be reached (True) or not (False)
    """

    # to flatten the 2D array into 1D
    array = np.ravel(initial_state)
    inversions = 0

    for i in range(0, 9):
        for j in range(i + 1, 9):
            if array[i] != 0 and array[j] != 0 and array[i] > array[j]:
                inversions += 1

    return inversions % 2 == 0


def isSolution(solution_state) -> bool:
    """
    Indicates whether the given state equals the goal state.

    :param solution_state: the given state suspected to be the solution/equal to the goal state.
    :return: bool value if the given state equals the goal state.
    """

    return np.array_equal(solution_state, goal_state)


def solveBFS(start) -> Node:
    """
    Implementation of the Breadth-First Search algorithm to investigate the nodes beginning from the 'start'
    node and find the solution (the state of the node that equals the goal state). In this algorithm, the graph (specifically, tree
    in this problem) is not pre-given, yet it is being expanded as the search advances; new nodes (children) emerge
    at every instance of a queue entry. A list is used to emulate a queue in this implementation.

    :param start: node from which the search is to begin.
    :return: the found node whose state equals the goal state.
    """

    # the start node is added to the queue.
    q = [start]

    # until the queue is empty, continue the search
    while len(q) != 0:

        # store the first element of the queue in the variable 'front'
        front = q[0]

        if isSolution(front.state):
            # if the node has the state equal to the goal state, then return it.
            return front

        if len(front.children) == 0:
            # create new nodes within the search process.
            front.children = getPossibleStates(q.pop(0))

        # add the newly-emerged nodes in the queue to be investigated.
        q += front.children

    return None


def solveDFS(start, depth) -> Node:
    """
    Implementation of the Depth-First Search algorithm to investigate the nodes beginning from the 'start' node and
    find the solution (the state of the node that equals the goal state). In this algorithm, the graph (specifically,
    tree in this problem) is not pre-given, yet it is being expanded as the search advances; new nodes (children)
    emerge at every instance of a stack entry. A list is used to emulate a stack in this implementation. A depth
    variable is used to limit the search. Since the DFS algorithm searches the tree branch by branch, unlike the BFS,
    using a depth limit eliminates an infinite loop.

    :param depth: depth limit till which the search shall continue.
    :param start: node from which the search is to begin.
    :return: the found node whose state equals the goal state.
    """

    # the start node is added to the stack.
    s = [start]

    while len(s) != 0:

        # the top element is reached
        top = s[-1]

        if isSolution(top.state):
            return top

        if len(top.children) == 0 and len(s) < depth:
            '''
            Checking if the top node has children will guarantee that on backtracking when the same node is visited
            no new nodes will be generated as it will already have children. Doing so will eliminate the generation of
            redundant nodes that would slow down the search and waste memory.
            '''
            top.children = getPossibleStates(top)

        if len(top.children) == 0 or allVisited(top.children):
            '''
            when the depth limit is reached no new children are generated. Therefore it's checked if the current node
            has children. Also, if all of the child nodes are already visited backtrack.
            '''

            # backtracking starts with the popping the top node.
            s.pop()

        for st in top.children:
            # among the children pick the first unvisited node.
            if not st.visited:
                st.visited = True
                s.append(st)
                break

    return None


def trackSolution(end) -> [Node]:
    """
    Taking the end node, goes back to the first node using the parent links. Utilized to construct the solution path.
    The list is later to be reversed to show the solution path in order.

    :param end: end node starting from which tracking shall occur.
    :return: returns a list of linked nodes starting with the end node till the root node holding the initial state.
    """

    nodes = []
    current = end

    while current is not None:
        # while the root node has not been reached

        nodes.append(current)
        current = current.parent

    nodes.reverse()

    return nodes
