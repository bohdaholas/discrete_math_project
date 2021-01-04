'''
Tarjan’s Algorithm
to find Strongly
Connected Components
'''

next_index = 0  # Next index
nextgroup = 0  # Next SCC ID.


def tarjan_algorithm_scc(graph: dict) -> list:
    '''
    Tarjan's Algorithm (named for its discoverer, Robert Tarjan) is a graph theory algorithm
    for finding the strongly connected components of a graph. Returns list of scc.
    '''
    n = len(graph)
    index = [None] * n
    lowlink = [None] * n
    onstack = [False] * n
    stack = []
    groups = []  # SCCs: list of vertices.
    groupid = {}  # Map from vertex to SCC ID.

    def strongconnect(vertex: int) -> list:
        '''
        Returns scc for graph.
        '''
        global next_index, nextgroup
        # set the depth index for this node to the smallest unused index
        v = vertex-1
        index[v] = next_index
        lowlink[v] = next_index
        next_index += 1
        stack.append(v)
        onstack[v] = True
        for w_vertex in graph[vertex]:
            w = w_vertex-1
            if index[w] == None:
                strongconnect(w_vertex)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], index[w])
        # -----------------------------------------------
        if index[v] == lowlink[v]:
            com = []
            while True:
                w = stack[-1]
                del stack[-1]
                onstack[w] = False
                com.append(w+1)
                groupid[w] = nextgroup
                if w == v:
                    break
            groups.append(min(com))
            nextgroup += 1

    for v in range(1, n+1):
        if index[v-1] == None:
            strongconnect(v)

    return sorted(groups)
