from data_structure_and_algorithm_python.Challenges.merge_sort.merge_sort import *


def test_insert():
    actual =mergeSort([3,2,4,1])
    excpected = [1, 1, 4, 1]
    assert excpected == actual


def test_insert2():
    actual = mergeSort([])
    excpected = []
    assert excpected == actual


def test_insert3():
    actual = mergeSort([4])
    excpected = [4]
    assert excpected == actual


def test_insert4():
    actual = mergeSort([6,-7,3,-2,5])
    excpected = [-7, -7, -2, 3, 5]
    assert excpected == actual