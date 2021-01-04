# import resource, sys

# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))
# sys.setrecursionlimit(10 ** 6)


def read_graph(path: str) -> dict:
    """
    # >>> read_graph('graphs/graph_100_1942_0.csv')
    # >>> read_graph('graphs/graph_100_2160_1.csv')
    # >>> read_graph('graphs/graph_5000_247404_0.csv')
    # >>> read_graph('graphs/graph_5000_248580_1.csv')
    # >>> read_graph('graphs/graph_100000_4999_0.csv')
    # >>> read_graph('graphs/graph_100000_4999_1.csv')
    # >>> read_graph('graphs/graph_100000_4997346_0.csv')
    # >>> read_graph('graphs/graph_100000_4998622_1.csv')
    >>> read_graph('graphs/0.csv')
    """
    with open(path, "r", encoding="utf-8") as file:
        graph_type = int(path[-5])  # 0 or 1
        adjacency_list = {}
        if not graph_type:  # non-oriented
            for line in file:
                nodes = line.split()
                if nodes[0] not in adjacency_list:
                    adjacency_list[nodes[0]] = [nodes[1]]
                else:
                    adjacency_list[nodes[0]].append(nodes[1])
                if nodes[1] not in adjacency_list:
                    adjacency_list[nodes[1]] = [nodes[0]]
                else:
                    adjacency_list[nodes[1]].append(nodes[0])
        else:  # oriented
            for line in file:
                nodes = line.split(" ")
                if nodes[0] not in adjacency_list:
                    adjacency_list[nodes[0]] = [nodes[1]]
                else:
                    adjacency_list[nodes[0]].append(nodes[1])
                if nodes[1] not in adjacency_list:
                    adjacency_list[nodes[1]] = []
                else:
                    pass
    return adjacency_list


def to_list(graph: str) -> list:
    """
    Return the list of graph edges
    """
    list_graph = []
    for key in graph:
        for vertex in graph[key]:
            list_graph.append([int(key), int(vertex)])

    return list_graph


def articul_points(graph: list) -> set:
    """
    Find all articulation points of a connected undirected graph
    and return the set of them.

    >>> articul_points(to_list(read_graph('graphs/graph_100_1942_0.csv')))
    {0, 100, 1942, 71}
    >>> articul_points(to_list(read_graph('graphs/graph_100_2160_1.csv')))
    {0, 100, 2160, 17, 95}
    >>> articul_points(to_list(read_graph('graphs/graph_5000_247404_0.csv')))
    {0, 5000, 247404, 368, 412}
    """
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


# print(articul_points(to_list(read_graph("graphs/graph_5000_247404_0.csv"))))
