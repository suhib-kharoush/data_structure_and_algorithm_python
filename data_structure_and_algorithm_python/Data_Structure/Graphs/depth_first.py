from data_structure_and_algorithm_python.Data_Structure.Graphs.Graphs import Graph


def depth_first(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            return path
        for neighbor in graph[source]:
            path = depth_first(graph, neighbor, path)
    

    return path




if __name__=='__main__':
    graph = {'A':['B', 'C', 'D'],
    'B':['E'],
    'C':['F', 'G'],
    'D':['H'],
    'E':['I'],
    'F':['J']}

    path = depth_first(graph, 'A')
    print(' '.join(path))
