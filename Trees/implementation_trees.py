class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self,data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
      return

    else:
      current_node = self.root
      while True:
        if data < current_node.data:
          if current_node.left == None:
            current_node.left = new_node
            return         
            
          else:
            current_node = current_node.left


        elif data > current_node.data:
          if current_node.right == None:
            current_node.right = new_node
            return
          else:
            current_node = current_node.right


  def lookup(self,data):
    current_node = self.root
    while(True):
      if current_node == None:
        return False
      elif current_node.data == data:
        return "Finally got",  current_node.data
      elif data < current_node.data:
        current_node = current_node.left
        print("checked here")
      else:
        current_node = current_node.right


tree = BinaryTree()
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.insert(5)
print(tree.lookup(3))
print(tree.root.left.right.data)
            
