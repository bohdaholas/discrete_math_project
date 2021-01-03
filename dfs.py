"""
A module which finds all connected components of both oriented and non-oriented graphs.
"""

graph_example = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': [],
    1: [2],
    2: [1]
}


def dfs(graph: dict, node: (str, int), visited: set) -> set:
    """
    Return a set of nodes that are reachable from the given node
    >>> list(sorted(dfs(graph_example, 'A', set())))
    ['A', 'B', 'C']
    >>> list(sorted(dfs(graph_example, 1, set())))
    [1, 2]
    """
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited


def find_components(graph: dict):
    """
    Return connected components of the given graph
    >>> find_components(graph_example)
    [{'C', 'A', 'B'}, {1, 2}]
    """
    components = []
    used_nodes = set()
    for node in graph:
        if node not in used_nodes:
            visited = set()
            component = dfs(graph, node, visited)
            components.append(component)
            used_nodes = used_nodes.union(component)
    return components
