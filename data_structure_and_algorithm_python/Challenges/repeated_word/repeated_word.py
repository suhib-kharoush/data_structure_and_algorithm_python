from data_structure_and_algorithm_python.Challenges.hashtables.hashtable import *
from data_structure_and_algorithm_python.Challenges.hashtables.linked_list import *
import re

def repeated_word(string):
    
    if string == '':
        return 'empty'
    words = re.sub(r'[^\w\s]', '',string).lower().split(' ')
    hashMap = HashTable()
    for i in words:
        if hashMap.contains(i):
            return i
        else:
            hashMap.add(i, 1)
    return 'nothing repeated'



if __name__=='__main__':
    str1="Train Bus Bus Aeroplane Taxi Bus"
    print(repeated_word(str1))
    str2="it was the age of wisdom it was the age of foolishness"
    print(repeated_word(str2))
    str3="It was a queer, sultry summer , the summer they electrocuted the Rosenbergs , and I didn’t know what I was doing in New York..."
    print(repeated_word(str3))