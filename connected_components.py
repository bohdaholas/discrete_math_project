from read_write_graph import *


def dfs(graph, starting_node):
    """
    Return a set of nodes that are reachable from the given node
    >>> dfs(graph_example, 'L')
    ['L', 'J', 'K']
    >>> dfs(graph_example, 'A')
    ['A', 'C', 'B']
    >>> dfs(graph_example, 1)
    [1, 2]
    >>> dfs(read_graph('graphs/graph_100_1942_0.csv'), '71')
    >>> dfs(read_graph('graphs/graph_100_2160_1.csv'), '92')
    >>> dfs(read_graph('graphs/graph_5000_247404_0.csv'), '5000')
    >>> dfs(read_graph('graphs/graph_5000_248580_1.csv'), '4932')
    >>> dfs(read_graph('graphs/graph_100000_4999_0.csv'), '99669')
    >>> dfs(read_graph('graphs/graph_100000_4999_1.csv'), '14331')
    >>> dfs(read_graph('graphs/graph_100000_4997346_0.csv'), '17351')
    >>> dfs(read_graph('graphs/graph_100000_4998622_1.csv'), '20319')
    """
    path = []
    stack = {starting_node}
    while len(stack):
        current_node = stack.pop()
        if current_node not in path:
            path.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in stack and neighbor not in path:
                stack.add(neighbor)
    return path


def find_components(graph: dict):
    """
    Return connected components of the given graph
    >>> find_components(graph_example)
    ['A', 1, 'J']
    >>> find_components(read_graph('graphs/graph_100_1942_0.csv'))
    >>> find_components(read_graph('graphs/graph_100_2160_1.csv'))
    >>> find_components(read_graph('graphs/graph_5000_247404_0.csv'))
    >>> find_components(read_graph('graphs/graph_5000_248580_1.csv'))
    >>> find_components(read_graph('graphs/graph_100000_4999_0.csv'))
    >>> find_components(read_graph('graphs/graph_100000_4999_1.csv'))
    >>> find_components(read_graph('graphs/graph_100000_4997346_0.csv'))
    >>> find_components(read_graph('graphs/graph_100000_4998622_1.csv'))
    """
    components = []
    used_nodes = set()
    for node in graph:
        if node not in used_nodes:
            component = dfs(graph, node)
            components.append(component[0])
            used_nodes = used_nodes.union(component)
    return components









