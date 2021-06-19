class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
        

class Stack:
    def __init__(self, node = None):
        self.top = node

    def push(self, value):
        if not self.top:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
    def pop(self):
        if not self.isEmpty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        raise Exception('empty stack, nothing to pop')

    
    def peek(self):
        if not self.isEmpty():
            return self.top.value

        raise Exception('empty stack, nothing to peek')

    def isEmpty(self):
        if self.top:
            return False
        return True

    def __str__(self):
        current = self.top
        content = []
        while current:
            content.append(str(current.value))
            current = current.next
        return '\n'.join(content)

class Queue:
    def __init__(self, node = None):
        self.stack = Stack()
        self.reversed = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        if not self.stack.isEmpty():
            while not self.stack.isEmpty():
             pop_items = self.stack.pop()
             self.reversed.push(pop_items)

            result = self.reversed.pop()
            if self.stack.isEmpty():
                while not self.reversed.isEmpty():
                    self.stack.push(self.reversed.pop())
            return result
        else:
               raise Exception("it's an empty stack")

    

    def peek(self):
        if not self.stack.isEmpty():
            current = self.stack.top
            content = []
            while current:
                content.insert(0, str(current.value))
                current = current.next
            return content[0]
        raise Exception('empty stack, nothing to peek')

    def __str__(self):
         current = self.stack.top
         content = []
         while current:
          content.insert(0,str(current.value))
          current = current.next
         return "\n".join(content) 


if __name__=='__main__':
 Queue = Queue()
 Queue.enqueue(5)
 Queue.enqueue(8)
 Queue.enqueue(1)
 Queue.dequeue()
 print(Queue.peek())

 print(Queue)
