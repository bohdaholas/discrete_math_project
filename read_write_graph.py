graph_example = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': [],
    1: [2],
    2: [1],
    'J': ['K', 'L'],
    'L': ['J'],
    'K': ['L']
}


def read_graph(path: str) -> dict:
    """
    >>> read_graph('graphs/graph_100_1942_0.csv')
    >>> read_graph('graphs/graph_100_2160_1.csv')
    >>> read_graph('graphs/graph_5000_247404_0.csv')
    >>> read_graph('graphs/graph_5000_248580_1.csv')
    >>> read_graph('graphs/graph_100000_4999_0.csv')
    >>> read_graph('graphs/graph_100000_4999_1.csv')
    >>> read_graph('graphs/graph_100000_4997346_0.csv')
    >>> read_graph('graphs/graph_100000_4998622_1.csv')
    """
    with open(path, 'r', encoding='utf-8') as file:
        graph_type = int(path[-5])  # 0 or 1
        file = file.read().splitlines()
        adjacency_list = {}
        if not graph_type:  # non-oriented
            for line in file:
                nodes = line.split(' ')
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
                nodes = line.split(' ')
                if nodes[0] not in adjacency_list:
                    adjacency_list[nodes[0]] = [nodes[1]]
                else:
                    adjacency_list[nodes[0]].append(nodes[1])
                if nodes[1] not in adjacency_list:
                    adjacency_list[nodes[1]] = []
                else:
                    pass
    return adjacency_list


def write_graph(graph: dict) -> None:
    """
    Write graph to csv file
    """
    with open('graph.csv', 'w', encoding='utf-8') as file:
        for node in graph:
            for other_nodes in graph[node]:
                file.write(f"{node} {other_nodes}\n")


if __name__ == '__main__':
    write_graph(graph_example)






