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

def test_add_method_for_BinarySearch_class():
    bts=BinarySearchTree()
    bts.add(5)
    bts.add(9)
    bts.add(-2)
    bts.add(6)
    bts.add(3)
    bts.add(8)
    bts.add(5)
    assert bts.root.value == 5
    assert bts.root.left.value == -2
    assert bts.root.right.value == 9
    assert bts.root.left.right.value == 3
    assert bts.root.right.left.left.value == 5

def test_contains_method(tree_test_two):
    expected=True
    actual=tree_test_two.contains(2)
    assert actual == expected

def test_find_max_value_within_tree(tree_test):
    expected=9
    actual=tree_test.max_val()
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