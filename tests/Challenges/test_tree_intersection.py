from data_structure_and_algorithm_python.Challenges.tree_intersection.tree_intersection import *
import pytest

def test_tree_intersection(test_1):
    expected=[100, 160, 125, 175, 200, 350, 500]
    actual=test_1
    assert actual == expected

def test_first_tree_empty():
     t1=BinaryTree()
     node=Node(2)
     node.left=Node(1)
     t2=BinaryTree()
     expected=None
     actual=tree_intersection(t1,t2)
     assert actual == expected


@pytest.fixture
def test_1():
    t1 = Node(150)
    t1.left = Node(100)
    t1.left.left = Node(75)
    t1.left.right = Node(160)
    t1.left.right.left = Node(125)
    t1.left.right.right = Node(175)
    t1.right = Node(250)
    t1.right.left = Node(200)
    t1.right.right = Node(350)
    t1.right.right.left = Node(300)
    t1.right.right.right = Node(500)
    binary_t1 = BinaryTree(t1)
    t2 = Node(42)
    t2.left = Node(100)
    t2.left.left = Node(15)
    t2.left.right = Node(160)
    t2.left.right.left = Node(125)
    t2.left.right.right = Node(175)
    t2.right = Node(600)
    t2.right.left = Node(200)
    t2.right.right = Node(350)
    t2.right.right.left = Node(4)
    t2.right.right.right = Node(500)
    binary_t2 = BinaryTree(t2)
    return tree_intersection(binary_t1, binary_t2)
