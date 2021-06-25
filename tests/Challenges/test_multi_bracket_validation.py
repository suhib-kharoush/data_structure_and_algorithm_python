  
from data_structure_and_algorithm_python.Challenges.multi_bracket_validation.multi_bracket_validation import *


def test_matched():
    test_array=['{}','{}(){}','()[[Extra Characters]]','(){}[[]]','{}{Code}[Fellows]','(())','[({}]','(](','{(})','{',')','{]']
    expected=[True,True,True,True,True,True,False,False,False,False,False,False]
    actual=[matched(string) for string in test_array]
    assert actual == expected