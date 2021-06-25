class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None

class PseudoQueue:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.front=None
    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self ):
        while not self.stack_1.isEmpty():
            popped = self.stack_1.pop()
            self.stack_2.push(popped)
        result = self.stack_2.pop()
        if self.stack_1.isEmpty():
            while not self.stack_2.isEmpty():
                 self.stack_1.push(self.stack_2.pop())
            return result

    def isEmpty(self):
        if self.stack_1:
            return False
        return True



    def __str__(self):
        stack= self.stack_1.top
        items = []
        while stack:
            items.insert(0,str(stack.value))
            stack = stack.next
        return " ".join(items)



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
        else:
            return 'empty stack'

    def peek(self):
        if not self.isEmpty():
            return self.top.value

        return 'empty stack'

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


if __name__=='__main__':
    stack = Stack()
    stack.push('first level')
    stack.push('second level')
    stack.push('third level')
    stack.push('fourth level')
    print(stack)

    pesudoQ= PseudoQueue()
    pesudoQ.enqueue(3)
    pesudoQ.enqueue(5)
    pesudoQ.enqueue(7)
    pesudoQ.enqueue(9)
    print(pesudoQ)
    print(pesudoQ.dequeue())
    print(pesudoQ.dequeue())
    print(pesudoQ)
