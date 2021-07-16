class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next


    def __str__(self):
        return self.data


    def getNext(self):
        return self.next

    def set_new(self, new):
        self.next=new

class LinkedList:
    def __init__(self, head=None):
        self.head=head

    
    def append(self, val):
        new=Node(val)
        new.__str__()
        current=self.head
        if current:
            while current.getNext() != None:
                current=current.getNext()
            current.set_new(new)
        else:
            self.head=Node(val)
            current=self.head
        return current.__str__()

