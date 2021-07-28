from data_structure_and_algorithm_python.Challenges.hashmap_left_join.hashmap_left_join import *
import pytest



def test():
  hash_one = HashTable()
  hash_one.add('fond', 'enamored')
  hash_one.add('wrath', 'anger')
  hash_one.add('diligent', 'employed')
  hash_one.add('guide', 'garp')
  hash_one.add('outfit', 'usher')
  hash_two = HashTable()
  hash_two.add('fond', 'averse')
  hash_two.add('wrath', 'delight')
  hash_two.add('diligent', 'idle')
  hash_two.add('guide', 'follow')
  hash_two.add('flow', 'jam')
  assert hash_left_join(hash_one,hash_two).__str__() =="{['diligent', ['employed', 'idle']]} -> None{['outfit', ['usher', None]]} -> None{['fond', ['enamored', 'averse']]} -> None{['guide', ['garp', 'follow']]} -> None{['wrath', ['anger', 'delight']]} -> None"
