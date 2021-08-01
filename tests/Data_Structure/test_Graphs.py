from data_structure_and_algorithm_python.Data_Structure.Graphs.Graphs import *

import pytest


def test_add_node_successfully():
  graph = Graph()
  graph.add_node('A')
  expected = 1
  actual = graph.size()
  assert  actual == expected

def test_add_edge_successfully():
  graph = Graph()
  vertix_1 = graph.add_node('A')
  vertix_2  =graph.add_node('B')
  graph.add_edge(vertix_1,vertix_2,1)
  assert graph.adjacency_list[vertix_1] == [(vertix_2 , 1)]


def test_get_all_nodes_and_check_the_size():
  graph = Graph()
  vertix_1= graph.add_node('A')
  vertix_2 =graph.add_node('B')
  vertix_3=graph.add_node('C')
  vertix_4=graph.add_node('D')
  vertix_5=graph.add_node('E')
  assert graph.size() == 5

def test_get_neighbor_and_with_weights():
  graph = Graph()
  vertix_1= graph.add_node('A')
  vertix_2 =graph.add_node('B')
  vertix_3=graph.add_node('C')
  graph.add_edge(vertix_1,vertix_2,1)
  graph.add_edge(vertix_1,vertix_3,2)
  assert graph.get_neighbors(vertix_1) == [('Vertix > B', 1), ('Vertix > C', 2)]


def test_graph_with_one_node_and_edge():
  graph=Graph()
  vertix_1 = graph.add_node('A')
  with pytest.raises(KeyError):
    graph.add_edge(vertix_1,None)

def test_empty_graph():
  graph = Graph()
  assert graph.print()== None
  print('pass')
