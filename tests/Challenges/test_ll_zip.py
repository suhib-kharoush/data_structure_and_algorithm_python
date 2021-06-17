from data_structure_and_algorithm_python.Challenges.ll_zip.ll_zip import LinkedList, zipLists
import pytest
def test_Thhhh():
    assert 1==1


# @pytest.mark.skip
def test_ll_zip():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert(1)
    ll1.insert(1)
    ll1.insert(1)
    ll1.insert(1)
    ll2.insert(2)
    ll2.insert(2)
    ll2.insert(2)
    ll2.insert(2)
    actual = zipLists(ll1, ll2).__str__()
    expect = "{2} --->{1} --->{2} --->{1} --->{2} --->{1} --->{2} --->{1} --->None"
    assert actual == expect

def test_first_greater():
    llg = LinkedList()
    lll = LinkedList()

    llg.insert(2)
    llg.insert(3)
    llg.insert(1)

    lll.insert(9)
    lll.insert(5)

    assert zipLists(llg, lll) == "{5} --->{1} --->{9} --->{3} --->None"

def test_first_less():
    lll2 = LinkedList()
    llg2 = LinkedList()

    llg2.insert(4)
    llg2.insert(3)
    llg2.insert(1)

    lll2.insert(9)
    lll2.insert(5)

    assert zipLists(llg2, lll2) == "{5} --->{1} --->{9} --->{3} --->None"