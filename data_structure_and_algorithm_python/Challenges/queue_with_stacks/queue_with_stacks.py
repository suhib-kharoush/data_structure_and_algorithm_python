class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None

class PseudoQueue:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        current = self.stack_1.top

        while current:
            self.stack_2.push(current.value)
            current = current.next
            self.stack_1.pop()

        self.stack_1.push(value)
        current_2 = self.stack_2.top
        while current_2:
            self.stack_1.pop()

    
    def peek(self):
        if not self.isEmpty():
            return self.stack_1.value


    def dequeue(self):
        if not self.stack_1.top:
            print ('empty queue')
        
        strQueue = str(self.stack_1.top.value)
        self.stack_1.top
        return strQueue

    def isEmpty(self):
        if self.stack_1:
            return False
        return True


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