from typing import Counter

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, value):
        new_value = Node(value)
        new_value.next = self.head
        self.head = new_value

    def includes(self, x):
        current = self.head
        try:
            while current != None:
                if current.value == x:
                    return True
                current = current.next
            return False
        except:
            print("something went wrong")

    def __str__(self):
        output = ''
        current = self.head
        try:
            while current:
                output += f"{ {current.value} } --->"
                current = current.next
            output += f"{None}"
            return output
        except:
            print("wrong insertion")

    def append(self, value):
        new_value = Node(value)
        current = self.head
        if not self.head:
            self.head = new_value
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_value

    def __repr__(self):
        pass

    
    def insertBefore(self, val, new_value):
        newNode = Node(new_value)
        current = self.head

        if current == None:
            return "list is empty"
        else:
            if current.value == val:
                newNode.next = current.next
                current.next = newNode
                return
            else:
                current = current.next


    def insertAfter(self, val, new_value):
        if val is None:
            return "wrong value"
        else:
            current = self.head
            new_node = Node(new_value)
            while current:
                if current.value == val:
                   new_node.next = current.next
                   current.next = new_node
                current = current.next

 




if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(4)

    
    print(ll1)
