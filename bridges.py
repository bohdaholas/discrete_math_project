"""Module for searching bridges in a
undirected graph.
"""

# import resource, sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

# sys.setrecursionlimit(10**6)
# IF MEMORY ERROR OCCURS, LINES ABOVE WILL HELP FOR LINUX!

import sys

visited = {} #dictionary for checking if node is already visited
h = {} #value is depth of each node
f = {} #value of 'u' is min of h[v], where v are all the nodes that are 
# achievable from node 'u'
bridges = [] #list for saving bridges


def bridge_search(u: (str, int), parent: (str, int), curr_h: int, g: dict):
    """Search bridges using depth first search. Recursive function.
    """

    curr_h += 1
    h[u] = curr_h
    f[u] = h[u]
    visited[u] = True

    for v in g[u]:

        if v == parent:
            continue

        if v not in visited:

            bridge_search(v, u, curr_h, g)
            f[u] = min(f[u], f[v])

            if f[v] > h[u]:
                bridges.append(tuple(sorted([int(u), int(v)])))

        else:

            f[u] = min(f[u], h[v])


def find_bridges(g: dict) -> list:
    """Starts depth first search, which finds bridges, giving it
    first node. Graph is required. Returns list of bridges.
    >>> find_bridges({'a':['b'], 'b':['a', 'c', 'd'], 'c':['b'], 'd':['b']})
    [('b', 'c'), ('b', 'd'), ('a', 'b')]
    >>> find_bridges({0:[1], 1:[0, 2, 3], 2:[1], 3:[1]})
    [(1, 2), (1, 3), (0, 1)]
    >>> find_bridges({0:[1], 1:[0, 2, 3], 2:[1, 3], 3:[1, 2]})
    [(0, 1)]
    >>> find_bridges({'a':['b'], 'b':['a', 'c', 'd'], 'c':['b', 'd'], 'd':['b', 'c']})
    [('a', 'b')]
    """


    sys.setrecursionlimit(len(g)) # sets recursion limit
 
    visited.clear()
    h.clear()
    f.clear()
    bridges.clear()

    # bridge_search(list(g.keys())[0], None, -1, g)

    for key in g.keys():
        if key not in visited:
            bridge_search(key, None, -1, g)

    return bridges
