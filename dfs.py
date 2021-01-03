graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
    1: [2],
    2: [1]
}


def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited


def find_components(graph):
    components = []
    used_nodes = set()
    for node in graph:
        if node not in used_nodes:
            visited = set()
            component = dfs(graph, node, visited)
            components.append(component)
            used_nodes = used_nodes.union(component)
    return components
