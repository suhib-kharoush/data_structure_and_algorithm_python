
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

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, val):
        self.dq.appendleft(val)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)
           
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
    def breadth_first_search(self ,start_vertex):
        list=[]
        queue = Queue()
        visited = set()

        queue .enqueue(start_vertex)
        visited.add(start_vertex)
        
        while len(queue):
            current_vertex = queue.dequeue()
            list.append(current_vertex)
            for child in self.adjacency_list[current_vertex]:
                if child[0] not in visited:
                    child=child[0]
                    visited.add(child)
                    queue.enqueue(child)
        return list


    def business_trip(self, cities):
        sum = 0
        flag = False
        for i in range(len(cities) - 1):
            neighbors = self.adjacency_list[cities[i]]
            
            print(neighbors)

            for neighbor in neighbors:
                if cities[i + 1] == neighbor[0]:
                    sum+=neighbor[1]
                    flag = True
                    break
                else:
                    sum+=0
                    flag = False
        if not flag:
            return False, '$0'
        return True, '$' + str(sum)



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
    graph.print()


