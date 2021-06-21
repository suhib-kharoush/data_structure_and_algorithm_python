from data_structure_and_algorithm_python.Challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest

def test_queue_enqueue():
    expected = "5"
    queue = Queue()
    queue.enqueue(5)
    actual = f"{queue}"
    assert actual == expected

def test_queue_multiple_enqueue(queue_test):
    expected = "4 3 2 1"
    actual = f"{queue_test}"
    assert actual == expected

def test_queue_dequeue(queue_test):
    expected = 4
    actual = queue_test.dequeue()
    assert actual == expected
    
def test_queue_peek_front(queue_test):
    expected = None
    actual = queue_test.peek()
    assert actual == expected

@pytest.fixture
def queue_test():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    return queue