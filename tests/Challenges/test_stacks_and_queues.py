import queue
from data_structure_and_algorithm_python.Challenges.stacks_and_queues.stacks_and_queues import *
import pytest
import unittest


def test_push(test_stack):
    expected = "three\ntwo\none"
    actual = f'{test_stack}'
    assert expected == actual


def test_push_empty():
    stack = Stack()
    stack.push('one')
    expected = 'one'
    actual = f'{stack}'
    assert expected == actual


def test_peek(test_stack):
    stack = test_stack
    expected = 'three'
    actual = f'{stack.peek()}'
    assert expected == actual


def test_isEmpty():
    stack = Stack()
    expected = True
    actual = stack.isEmpty()
    assert expected == actual


def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()


def test_pop_empty_queue():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_pop(test_stack):
    test_stack.pop()
    expected = 'two\none'
    actual = f'{test_stack}'
    assert expected == actual


def test_queue(test_enqueue):
    expected = 'one\ntwo\nthree'
    actual = f'{test_enqueue}'
    assert expected == actual


def test_empty_stack(test_stack):
    for i in range(3):
        test_stack.pop()
    excpected = True
    actual = test_stack.isEmpty()
    assert excpected == actual


def test_adding_multiple_to_stack():
    stack = Stack()
    for i in range(1, 4):
        stack.push(i)
    excpected = "3\n2\n1"
    actual = f"{stack}"
    assert excpected == actual


def test_enqueue_empty():
    queue = Queue()
    queue.enqueue('one')
    expected = 'one'
    actual = f'{queue}'
    assert expected == actual


def test_peek(test_queue):
    expected = 'one'
    actual = f'{test_queue.peek()}'
    assert expected == actual


def test_queue_empty_peek():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()


def test_empty():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()


def test_dequeue(test_queue):
    test_queue.dequeue()
    excpected = "two\nthree"
    actual = f"{test_queue}"
    assert excpected == actual


def test_adding_multiple_to_queue():
    queue = Queue()
    for i in range(1, 4):
        queue.enqueue(i)
    excpected = "1\n2\n3"
    actual = f"{queue}"
    assert excpected == actual


@pytest.fixture
def test_stack():
    stack = Stack()
    stack.push('one')
    stack.push('two')
    stack.push('three')
    return stack


@pytest.fixture
def test_queue():
    queue = Queue()
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')
    return queue
