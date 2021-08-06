from data_structure_and_algorithm_python.Data_Structure.Graphs.Graphs import Graph
from data_structure_and_algorithm_python.Data_Structure.Graphs.depth_first import depth_first

def test_return_path():
    graph = {"A": ["B", "C", "D"],
             "B": ["E"],
             "C": ["F", "G"],
             "D": ["H"],
             "E": ["I"],
             "F": ["J"]}
    actual = depth_first(graph, 'A')
    expected = ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']
    assert actual == expected