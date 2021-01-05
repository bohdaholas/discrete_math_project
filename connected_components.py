from read_write_graph import *


def dfs(graph, starting_node):
    """
    Return a list of nodes that are reachable from the given node
    >>> dfs(read_graph('graphs/graph_100000_4999_0.csv'), '99669')
    ['99669', '32739']
    >>> dfs(read_graph('graphs/graph_100000_4999_1.csv'), '14331')
    ['14331']
    """
    visited = []
    stack = {starting_node}
    while len(stack):
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in stack and neighbor not in visited:
                stack.add(neighbor)
    return visited


def find_components(graph: dict, all=False):
    """
    Return connected components of the given graph
    >>> find_components(read_graph('graphs/graph_100_1942_0.csv'))
    ['100']
    >>> find_components(read_graph('graphs/graph_5000_247404_0.csv'))
    ['5000']
    """
    components = []
    used_nodes = set()
    for node in graph:
        if node not in used_nodes:
            component = dfs(graph, node)
            if all:
                components.append(component)
            else:
                components.append(component[0])
            used_nodes = used_nodes.union(component)
    return components
