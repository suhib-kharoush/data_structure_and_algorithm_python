from data_structure_and_algorithm_python.Challenges.hashtables.hashtable import *

def test_add_to_hash_table():
    hashed = HashTable()
    actual = hashed.add('Suhib', "he is in 401-Python course")
    expected = "{['Suhib', 'he is in 401-Python course']} -> None"
    assert actual == expected

def test_get_hash_table():
    hashed = HashTable()
    hashed.add('Ahmad', 'lead instructor')
    expected = 'lead instructor'
    actual = hashed.get('Ahmad')
    assert actual == expected

def test_not_existing_key():
    hashed = HashTable()
    hashed.add('Ahmad', 'lead instructor')
    expected = None
    actual = hashed.get('Suhib')
    assert expected == actual

def test_handle_collisons():
    expected = "{['Suhib', 'Qusai']} -> {['Subhi', 'Hamza']} -> None"
    hashed = HashTable()
    hashed.add('Suhib', 'Qusai')
    hashed.add('Subhi', 'Hamza')
    actual = hashed.__str__()
    assert actual == expected


def test_get_value_for_collisons_bucket():
    expected = ['Qusai', 'Hamza']
    hashed = HashTable()
    hashed.add('Suhib', 'Qusai')
    hashed.add('Subhi', 'Hamza')
    actual = [hashed.get('Suhib'), hashed.get('Subhi')]
    assert actual == expected

def test_hash():
    hashed = HashTable()
    expected = 589
    actual = hashed.hash('Suhib')
    assert actual == expected