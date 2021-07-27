class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
    def pre_order(self):
        output = []
        if self.root == None:
            return output

        def walk(root):
            output.append(root.val)
            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)
        
        walk(self.root)
        return output

def tree_intersection(t1,t2):
  result=[]
  if t1.root == None or t2.root == None:
    return None
  def _walk(root1,root2):
    if root1.val == root2.val:
      result.append(root1.val)
    if root1.left and root2.left:
      _walk(root1.left ,root2.left)
    if root1.right and root2.right :
      _walk(root1.right ,root2.right)
  _walk(t1.root,t2.root)
  return result


if __name__=='__main__':
    t1 = Node(150)
    t1.left = Node(100)
    t1.left.left = Node(75)
    t1.left.right = Node(160)
    t1.left.right.left = Node(125)
    t1.left.right.right = Node(175)
    t1.right = Node(250)
    t1.right.left = Node(200)
    t1.right.right = Node(350)
    t1.right.right.left = Node(300)
    t1.right.right.right = Node(500)
    binary_t1 = BinaryTree(t1)
    print(binary_t1.pre_order())
    t2 = Node(42)
    t2.left = Node(100)
    t2.left.left = Node(15)
    t2.left.right = Node(160)
    t2.left.right.left = Node(125)
    t2.left.right.right = Node(175)
    t2.right = Node(600)
    t2.right.left = Node(200)
    t2.right.right = Node(350)
    t2.right.right.left = Node(4)
    t2.right.right.right = Node(500)
    binary_t2 = BinaryTree(t2)
    print(binary_t2.pre_order())
    print(tree_intersection(binary_t1, binary_t2))