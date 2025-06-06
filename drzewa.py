class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

def is_value_in_tree(root, value):
    if root.data == value:
        return True
    if root.left != None and is_value_in_tree(root.left, value):
        return True
    if root.right != None and is_value_in_tree(root.right, value):
        return True
    return False

def node_count(root):
    count = 0
    if root != None:
        count += 1
    if root.left != None:
        count += node_count(root.left)
    if root.right != None:
        count += node_count(root.right)
    return count

def tree_balanced(root):
    if root == None:
        return True
    lcount = node_count(root.left) if root.left != None else 0
    rcount = node_count(root.right) if root.right != None else 0
    if abs(lcount - rcount) > 1:
        return False
    return True

def tree_globally_locally_balanced(root):
    if root == None:
        return True
    if root.left == None and root.right != None or root.left != None and root.right == None:
        return False
    if root.left != None and root.right != None:
        return not tree_globally_locally_balanced(root.left) or not tree_globally_locally_balanced(root.right)

if __name__ == "__main__":
    assert(is_value_in_tree(root, 1)    == True)
    assert(is_value_in_tree(root, 7)    == True)
    assert(is_value_in_tree(root, 11)   == True)
    assert(is_value_in_tree(root, 12)   == False)

    assert(node_count(root)         == 11)
    assert(node_count(root.left)    == 5)

    assert(tree_balanced(root) == True)
    assert(tree_balanced(root.left) == False)
    assert(tree_balanced(root.left.left) == True)
    assert(tree_balanced(root.left.right) == True)

    assert(tree_globally_locally_balanced(root) == False)
