
from collections import deque

  
class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight
    
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, val):
        new_val = Vertix(val)
        new_val = str(new_val)
        self.adjacency_list[new_val] = []
        return new_val

    def add_edge(self, start_vertix, end_vertix, weight = 0):
        if start_vertix not in self.adjacency_list:
            raise KeyError('Start Not found in the graph')

        if end_vertix not in self.adjacency_list:
            raise KeyError('End not found in the graph')
        
        self.adjacency_list[start_vertix].append((str(end_vertix), weight))

    def get_nodes(self):
        return self.adjacency_list.keys()
    
    def get_neighbors(self, vertix):
        return self.adjacency_list[vertix]

    def size(self):
        return len(self.adjacency_list)

    def print(self):
        print(self.adjacency_list)



if __name__=='__main__':
    graph = Graph()
    Vertix_1 = graph.add_node('A')
    Vertix_2 = graph.add_node('B')
    Vertix_3 = graph.add_node('C')
    Vertix_4 = graph.add_node('D')
    Vertix_5 = graph.add_node('E')

    graph.add_edge(Vertix_1, Vertix_2, 1)
    graph.add_edge(Vertix_1, Vertix_3, 2)
    graph.add_edge(Vertix_2, Vertix_4, 4)
    graph.add_edge(Vertix_3, Vertix_4, 8)
    graph.add_edge(Vertix_3, Vertix_5, 3)
    graph.add_edge(Vertix_4, Vertix_5, 5)

    assert graph.size() == 5

    print(graph.get_nodes())
    print(graph.get_neighbors(Vertix_1))
    print(graph.get_neighbors(Vertix_2))
    print(graph.get_neighbors(Vertix_3))
    print(graph.get_neighbors(Vertix_4))
    print(graph.get_neighbors(Vertix_5))
    graph.print()
