def articul_points(graph: dict) -> set:
    """
    Find all articulation points of a connected undirected graph
    and return the list of them.

    >>> articul_points()
    []
    >>> articul_points()
    []
    """
    articulation_points = set()
    parents = {}
    lowest = {}

    def dfs(graph: dict, id: int, node: (str, int), parent: set, visited: set) -> set:
        """
        Provide help function articul points
        """
        edges = 0

        if node not in visited:
            visited.add(node)
            parents[node] = parent
            lowest[node] = id

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if neighbour not in visited:
                    parents[neighbour] = node
                    edges += 1
                    dfs(graph, id + 1, neighbour, node, visited)

                lowest[node] = min(lowest[node], lowest[neighbour])

                if id <= lowest[neighbour]:
                    if parents[node] != -1:
                        articulation_points.add(node)

            if parents[node] == -1 and edges >= 2:
                articulation_points.add(node)

    dfs(graph, 0, 0, -1, set())

    return articulation_points
