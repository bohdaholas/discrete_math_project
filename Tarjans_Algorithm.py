'''
Tarjan’s Algorithm
to find Strongly
Connected Components
'''

# from rsrc import Resource
import sys
# Resource.setrlimit(Resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

next_index = 0  # Next index
nextgroup = 0  # Next SCC ID.


def tarjan_algorithm_scc(graph: dict) -> list:
    '''
    Tarjan's Algorithm (named for its discoverer, Robert Tarjan) is a graph theory algorithm
    for finding the strongly connected components of a graph. Returns list of scc.
    '''
    vertex = {}
    stack = []
    groups = []  # SCCs: list of vertices.
    groupid = {}  # Map from vertex to SCC ID.

    def strongconnect(v: int):
        '''
        Returns scc for graph.
        '''
        global next_index, nextgroup
        # set the depth index for this node to the smallest unused index
        vertex[v] = [next_index, next_index, True]
        next_index += 1
        stack.append(v)

        for w in graph[v]:
            if w not in vertex:
                strongconnect(w)
                vertex[v][1] = min(vertex[v][1], vertex[w][1])
            elif vertex[w][-1]:
                vertex[v][1] = min(vertex[v][1], vertex[w][0])
        # -----------------------------------------------
        if vertex[v][0] == vertex[v][1]:
            com = []
            while True:
                w = stack[-1]
                del stack[-1]
                vertex[w][-1] = False
                com.append(w)
                groupid[w] = nextgroup
                if w == v:
                    break
            groups.append(min(com))
            nextgroup += 1

    for v in graph:
        if v not in vertex:
            strongconnect(v)
    return sorted(groups)
