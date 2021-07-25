from data_structure_and_algorithm_python.Challenges.repeated_word.repeated_word import *

def test_repeated_word():
    assert repeated_word('Train Bus Bus Aeroplane Taxi Bus') == 'bus'
    assert repeated_word('it was the age of wisdom it was the age of foolishness') == 'it'
    assert repeated_word('It was a queer, sultry summer , the summer they electrocuted the Rosenbergs , and I didn’t know what I was doing in New York...') == 'summer'