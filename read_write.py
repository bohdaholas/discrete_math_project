'''read_write.py
contain functions:
graph_dict() - to read  graph from file
convert_to_csv() - to write graph into file
'''


def  graph_dict(path_to_file: str, oriented=False) -> (dict):
    '''
    (str, bool) -> (dict)
    
    Read graph from file and return dict of vertices wich belonges to one edge
    if graph is oriented order of vertices is important, and not in other hand
    dictionary contain vertex as key and list of adjacent vertices
    in disoriented graph  there is no matter between edges (a,b) and (b,a)
    '''
    file = open(path_to_file, 'r')
    key_dict = {}
    
    # decide if file contain oriented graph or not
    oriented = int(path_to_file[-5])

    if oriented:
        graph = set(tuple(edge.split(' ')) for edge\
             in file.read().split('\n') if edge != '')
        file.close()
        key_dict = {key[0]: [] for key in graph}
        for edge in graph:
            if edge[0] in key_dict:
                key_dict[edge[0]].append(edge[1])
    else:
        graph = set(frozenset(edge.split(' ')) for edge\
                 in file.read().split('\n') if edge != '')
        file.close()
        '''for edge_el in graph:
            key_dict.update({edge_el[0]: []})'''
        for edge in graph:
            edge = tuple(edge)
            if edge[0] not in key_dict:
                key_dict.update({edge[0]: [edge[1]]})
            else:
                key_dict[edge[0]].append(edge[1])

    return key_dict


def convert_to_csv(graph: dict) -> (None):
    """
    (dict) -> (None)
    Get a dictionary of adjacent vertices of a graph
    Save the graph to a file in a csv format with space separator.
    """
    csv_graph = open('graph.csv', 'w')
    for key in graph:
        for value in graph[key]:
            csv_graph.write(str(key) + ' ' + str(value) + '\n')
    csv_graph.close()


if __name__ == '__main__':
    #graph = graph_dict('data1.csv')
    #convert_to_csv(graph)
    pass
