class Node:
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None

    def __str__(self, value):
        return str(self.value)


class BinaryTree:
    def __init__(self, root=None):
        self.root=root

    def pre_order(self):
        output=[]
        if self.root==None:
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
        output=[]
        if self.root ==None:
            return output
        def walk(root):
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
            output.append(root.value)
        walk(self.root)
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



if __name__=='__main__':
    node = Node(1)
    node.left = Node(2)
    node.left.right = Node(7)
    node.left.right = Node(9)
    node.right = Node(3)
    node.right.left = Node(4)
    node.right.right = Node(5)
    binary_tree = BinaryTree(node)

    print(binary_tree.pre_order())
    print(binary_tree.in_order())
    print(binary_tree.post_order())
    bs = BinarySearchTree(node)
    print(bs.contains(2))
    print(bs.contains(10))

    bs_2=BinarySearchTree()
    bs_2.add(5)
    bs_2.add(9)
    bs_2.add(-2)
    bs_2.add(6)
    bs_2.add(3)
    bs_2.add(8)
    bs_2.add(5)

    
    assert bs_2.root.value == 5
    assert bs_2.root.left.value == -2
    assert bs_2.root.right.value == 9
    assert bs_2.root.left.right.value == 3
    assert bs_2.root.right.left.left.value == 5


               