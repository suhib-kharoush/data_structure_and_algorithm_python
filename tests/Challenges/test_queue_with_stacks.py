from data_structure_and_algorithm_python.Challenges.queue_with_stacks.queue_with_stacks import PseudoQueue, Stack
import pytest
queue = PseudoQueue()


def test_enqueue():
    expected = "5"
    queue = PseudoQueue()
    queue.enqueue(5)
    actual = f"{queue}"
    assert actual == expected

# test : Can successfully enqueue multiple values into a queue
def test_multiple_enqueue(queue_test):
    expected = "9 7 5 3"
    actual = f"{queue_test}"
    assert actual == expected

# test : Can successfully dequeue out of a queue the expected value
def test_dequeue(queue_test):
    expected = 9
    actual = queue_test.dequeue()
    assert actual == expected



@pytest.fixture
def queue_test():
    queue = PseudoQueue()
    queue.enqueue(9)
    queue.enqueue(7)
    queue.enqueue(5)
    queue.enqueue(3)
    return queue