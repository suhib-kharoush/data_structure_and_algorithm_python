from data_structure_and_algorithm_python.Challenges.tree_fizz_buzz.tree_fizz_buzz import *

def test_fizz_buzz_tree():
    tree = BinaryTree()
    tree.root = Node(12)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.right = Node(6)
    tree.root.left.left = Node(8)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    tree.root.left.left.right = Node(5)
    tree.root.left.right.left = Node(11)
    expected = ['Fizz', '7', '8', 'Buzz', 'Fizz', '11', 'Buzz', 'Fizz', '4']
    actual = FizzBuzz_tree(tree)
    assert actual == expected