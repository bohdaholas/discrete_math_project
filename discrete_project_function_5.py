# import resource, sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)


from collections import defaultdict


def articul_points(to_list: list) -> set:
    """
    Find all articulation points of a connected undirected graph
    and return the set of them.
    """
    graph = defaultdict(to_list)
    for u, v in to_list:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    articulation_points = set()
    parents = {}
    lowest = {}

    def dfs(id: int, node: (str, int), parent: set):
        """
        Provide help function articul points
        """
        edges = 0

        visited.add(node)
        parents[node] = parent
        lowest[node] = id

        for neighbour in graph[node]:
            if neighbour == parent:
                continue
            if neighbour not in visited:
                parents[neighbour] = node
                edges += 1
                dfs(id + 1, neighbour, node)

            lowest[node] = min(lowest[neighbour], lowest[node])

            if (id <= lowest[neighbour]) and (parents[node] != -1):
                articulation_points.add(node)

        if (parents[node] == -1) and (edges >= 2):
            articulation_points.add(node)

    dfs(0, 0, -1)

    return articulation_points
