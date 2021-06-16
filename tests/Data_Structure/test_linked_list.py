import pytest
from unittest.mock import patch

from data_structure_and_algorithm_python.Data_Structure.Linked_list.Linked_list import *

def test_import():
    assert LinkedList


l_list = LinkedList()

def test_empty():
    actual = l_list.head
    expect = None
    assert actual == expect


def test_insert():
    l_list.insert(5)
    actual = l_list.includes(5)
    expect = True
    assert actual == expect


def test_head():
    l_list.insert(5)
    l_list.insert(10)
    l_list.insert(18)
    actual = l_list.head.value
    expect = 18
    assert actual == expect
    actual2 = l_list.head.next.value
    expect2 = 10
    assert actual2 == expect2




def test_return():
    actual = l_list.__str__()
    expect = "{18} --->{10} --->{5} --->{5} --->None"
    assert actual == expect


def test_append():
    l_list.append(8)
    actual = l_list.__str__()
    expect = "{18} --->{10} --->{5} --->{5} --->{8} --->None"
    assert actual == expect



@patch('builtins.print')
def test_kth_from_end(mock_print):
    l_list.kthFromEnd(5)
    mock_print.assert_called_with(18)

@patch('builtins.print')
def test_k_is_greater_than_list_length(mock_print):
    l_list.kthFromEnd(10)
    mock_print.assert_called_with('kth is greater than the linked-list')

@patch('builtins.print')
def test_k_and_len_are_the_same(mock_print):
    l_list.kthFromEnd(5)
    mock_print.assert_called_with(18)


@patch('builtins.print')
def test_negative_value(mock_print):
    l_list.kthFromEnd(-1)
    mock_print.assert_called_with('k should be a larger or equal to 0')

@patch('builtins.print')
def test_k_in_the_middle(mock_print):
    l_list.kthFromEnd(2,2)
    mock_print.assert_called_with(18)

@patch('builtins.print')
def test_empty_ll(mock_print):
    l_list.empty_ll()
    l_list.kthFromEnd(1)
    mock_print.assert_called_with("linked list is empty")