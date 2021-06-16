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

    def kthFromEnd(self, k, from_node=None):
        current = self.head
        if current == None:
            return print("linked list is empty")
        if k < 0:
            return print("k should be a larger or equal to 0")

        length = 0
        while current is not None:
            current = current.next
            length += 1
        if k > length:
             print("kth is greater than the linked-list")
             return

        current = self.head
        if from_node:
            for i in range(from_node, length - k - 2):
                current = current.next
            print(current.value)
        else:
            for i in range(0, length - k - 1):
                current = current.next
            print(current.value)
  
  
    def empty_ll(self):
        self.head = None
        return


    def zipLists(list_one, list_two):
        if not list_one:
            return list_two
        elif not list_two:
            return list_one
        zip_list = LinkedList()
        current = list_one
        current = current.head
        current_2 = list_two.head

        while current or current_2:
            if current:
                zip_list.append(current.data)
                current = current.next_node
            return zip_list
            


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(4)

    
    print(ll1)
