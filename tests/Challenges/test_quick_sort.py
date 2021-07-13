from data_structure_and_algorithm_python.Challenges.quick_sort.quick_sort import *

def test_insertion():
    actual = quick_sort([8,4,23,42,16,15],0, len([8,4,23,42,16,15]) - 1)
    expected = [8, 23, 42, 16, 15, 4]
    assert expected == actual

def test_insertion_2():
    actual = quick_sort([], 0, len([]) - 1)
    excpected = []
    assert excpected == actual

def test_insertion_3():
    actual = quick_sort([4], 0, len([4]) - 1)
    expected = [4]
    assert expected == actual


def test_insertion_4():
    actual = quick_sort([2,3,5,7,13,11], 0, len([2,3,5,7,13,11]) - 1)
    expected = [3, 5, 7, 13, 11, 2]
    assert expected == actual