def read_graph(path: str) -> dict:
    """
    Read graph from file
    """
    with open(path, 'r', encoding='utf-8') as file:
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
                nodes = line.split()
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
