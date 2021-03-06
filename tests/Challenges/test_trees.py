from data_structure_and_algorithm_python.Challenges.trees.trees import *

import pytest

def test_instansiate_an_empty_tree():
    expected = []
    bt = BinaryTree()
    actual = bt.pre_order()
    assert actual == expected

def test_instantiate_tree_with_single_root():
    expected = [5]
    node = Node(5)
    bt = BinaryTree(node)
    actual = bt.pre_order()
    assert expected == actual

def test_tree_add_children_to_single_root():
    expected = [2, 5, 6]
    node = Node(5)
    node.left = Node(2)
    node.right = Node(6)
    bt = BinaryTree(node)
    actual = bt.in_order()
    assert actual == expected

def test_pre_order_traversal(tree_test):
    expected = [1, 2, 9, 7, 3, 4, 5]
    actual = tree_test.pre_order()
    assert actual == expected

def test_in_order_traversal(tree_test):
    expected = [9,2,7,1,4,3,5]
    actual=tree_test.in_order()
    assert actual == expected

def test_post_order_traversal(tree_test):
    expected=[9,7,2,4,5,3,1]
    actual=tree_test.post_order()
    assert actual == expected

def test_find_max_value_within_tree(tree_test):
    expected=9
    actual=tree_test.find_maximum_value()
    assert actual == expected 

def test_breadth_first():
    input = BinaryTree()
    input.root = Node(2)
    input.root.left = Node(7)
    input.root.right = Node(5)
    input.root.left.right = Node(6)
    input.root.left.left = Node(2)
    input.root.right.right = Node(9)
    input.root.right.right.left = Node(4)
    input.root.left.left.right = Node(5)
    input.root.left.right.left = Node(11)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = breadth_first(input)
    assert actual == expected

@pytest.fixture
def tree_test():
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.right = Node(7)
    node1.left.left = Node(9)
    node1.right = Node(3)
    node1.right.left = Node(4)
    node1.right.right = Node(5)
    binary_tree = BinaryTree(node1)
    return binary_tree

@pytest.fixture
def tree_test_two():
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.right = Node(7)
    node1.left.left = Node(9)
    node1.right = Node(3)
    node1.right.left = Node(4)
    node1.right.right = Node(5)
    bs = BinarySearchTree(node1)
    return bs