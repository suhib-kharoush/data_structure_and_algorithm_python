class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def isEmpty(self):
        if self.front:
            return False
        return True

    def dequeue(self):
        if not self.isEmpty():
            value = self.front.value
            self.front = self.front.next
            return value



class Node:
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None
        self.next=None

    def __str__(self, value):
        return str(self.value)


class BinaryTree:
    def __init__(self,root=None):
        self.root=root

    def pre_order(self):
        ## [root][left][right]
        output=[]
        if self.root == None:
            return output
        def walk(root):
            output.append(root.value)
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        return output

    def in_order(self):
        ## [left][root][right]
        output = []
        if self.root==None:
            return output
        def walk(root):
            if root.left:
                walk(root.left)
            output.append(root.value)
            if root.right:
                walk(root.right)
        walk(self.root)
        return output

    def post_order(self):
        ## [left][right][root]
        output = []
        if self.root==None:
            return output
        def walk(root):
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
            output.append(root.value)
        walk(self.root)
        return output

    def find_maximum_value(self):
        if self.root == None:
            return 0
        maximum_value=self.root.value
        def walk(root):
            nonlocal maximum_value
            if root.value > maximum_value:
                maximum_value=root.value
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
            return maximum_value
        return walk(self.root)


def breadth_first(input):
    # by levels from left to right
        output=[]
        if not input.root:
            return []
        q=Queue()
        q.enqueue(input.root)
        while q.front:
            temp=q.dequeue()
            output=output+[temp.value]
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)
        return output
 

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root=Node(value)
        else:
            def walk(root):
                if value<root.value:
                    if not root.left:
                        root.left=Node(value)
                        return
                    else:
                        walk(root.left)
                else:
                    if not root.right:
                        root.right=Node(value)
                        return
                    else:
                        walk(root.right)
            return walk(self.root)

    def contains(self, value):
        if not self.root:
            return False
        
        def walk(root):
            if root:
                if root.value==value:
                    return True

                elif value != root.value:
                    if walk(root.left):
                        return True

            return False
        return walk(self.root)

    



# if __name__=='__main__':
#     node = Node(1)
#     node.left = Node(2)
#     node.left.right = Node(7)
#     node.left.right = Node(9)
#     node.right = Node(3)
#     node.right.left = Node(4)
#     node.right.right = Node(5)
#     binary_tree = BinaryTree(node)

#     print(binary_tree.pre_order())
#     print(binary_tree.in_order())
#     print(binary_tree.post_order())
#     bs = BinarySearchTree(node)
#     print(bs.contains(2))
#     print(bs.contains(10))
#     print(binary_tree.find_maximum_value())

#     bs_2=BinarySearchTree()
#     bs_2.add(5)
#     bs_2.add(9)
#     bs_2.add(-2)
#     bs_2.add(6)
#     bs_2.add(3)
#     bs_2.add(8)
#     bs_2.add(5)

    
#     assert bs_2.root.value == 5
#     assert bs_2.root.left.value == -2
#     assert bs_2.root.right.value == 9
#     assert bs_2.root.left.right.value == 3
#     assert bs_2.root.right.left.left.value == 5


               
if __name__ == "__main__":
    input = BinaryTree()
    input.root = Node(2)
    input.root.left = Node(7)
    input.root.right = Node(5)
    input.root.left.right = Node(6)
    input.root.left.left = Node(2)
    input.root.right.right=Node(9)
    input.root.right.right.left=Node(4)
    input.root.left.left.right=Node(5)
    input.root.left.right.left = Node(11)
    print(breadth_first(input))