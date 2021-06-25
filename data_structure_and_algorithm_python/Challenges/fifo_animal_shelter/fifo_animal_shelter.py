from typing import Counter


class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.stack_1=None
        self.stack_2=None
    
    def isEmpty(self):
        if self.stack_1:
            return False
        return True

    def enqueue(self, value):
        node = Node(value)
        if not self.stack_1:
            self.stack_1 = node
            self.stack_2 = node
        else:
            self.stack_2.next = node
            self.stack_2 = self.stack_2.next

    def dequeue(self):
        if not self.isEmpty():
            temp = self.stack_1
            self.stack_1 = self.stack_1.next
            temp.next = None
            return temp.value

    def peek(self):
        if not self.isEmpty:
            return self.stack_1.value

    def __str__(self):
        current = self.stack_1
        content = []
        while current:
            content.append(str(current.value))
            current = current.next
        return " ".join(content)


class Cat:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = 'cat'

class Dog:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = 'dog'

class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, pet):
        if pet.type == 'cat':
            self.cat.enqueue(pet.name)
        elif pet.type == 'dog':
            self.dog.enqueue(pet.name)
        else:
            return 'cats & dogs just'

    def dequeue(self, pref):
        if pref == 'cat':
            self.cat.dequeue()
        elif pref == 'dog':
            self.dog.dequeue()
        else:
            return 'cats & dogs just'


if __name__=='__main__':
    firststDog = Dog('shewawa')
    secondDog = Dog('haski')
    thirdDog = Dog('germanShebered')
    firstCat = Cat('seyami')
    secondCat = Cat('sherazi')
    thirdCat = Cat('hamalaya')

    animals = AnimalShelter()
    animals.enqueue(secondDog)
    animals.enqueue(firstCat)
    animals.enqueue(secondCat)
    print(animals.cat)

    animals.dequeue('cat')
    print(animals.cat)
