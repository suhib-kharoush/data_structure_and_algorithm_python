from data_structure_and_algorithm_python.Challenges.hashtables.linked_list import *



class HashTable():
    def __init__(self):
        self.size = 1024
        self.map = [None] * self.size

    def hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        index = (hash * 599) % self.size
        return index

    def contains(self, key):
        index = self.hash(key)
        if self.map[index]:
            temp = self.map[index].head
            while temp:
                if key == temp.data[0]:
                    return True
                temp = temp.next
        return False

    def add(self, key, value):
       index = self.hash(key)
       key_value = [key, value]
       if self.contains(key):
            temp = self.map[index].head
            while temp:
                if key == temp.data[0]:
                    temp.data[1] =  value
                temp = temp.next
                return self
       if self.map[index] is None:
           self.map[index] = LinkedList()
       self.map[index].append(key_value)
       return self.__str__()

    def get(self, key):
        index = self.hash(key)
        if self.map[index]:
            temp = self.map[index].head
            while temp:
                if key == temp.data[0] :
                    return temp.data[1]
                temp = temp.next
        return None

    def __str__(self):
        result = ""
        for i in self.map:
            if i is not None:
                temp = i.head
                while temp:
                    result +="{%s} -> " %(temp.data,)
                    temp = temp.next
                result+='None'
        return result



if __name__ == "__main__":
    hashed = HashTable()
    hashed.add('ahmad',29)
    hashed.add('hamad',24)
    hashed.add('class','Python-401d4')
    hashed.add('listen','Hey man')
    print(hashed.add('Suhib',"he is in 401-python course"))
    print(hashed)
