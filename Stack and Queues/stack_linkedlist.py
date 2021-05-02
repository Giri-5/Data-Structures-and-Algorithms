#peek, push, pop gmfa

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self,data):
    new_node = Node(data)
    if self.bottom == None:
      self.bottom = new_node
      self.top = self.bottom
      self.length += 1

    else:
      new_node.next = self.top
      self.top = new_node
      self.length += 1

    return(self.top.data)

  def pop(self):

    if self.length > 0:

      holderpoint = self.top
      self.top = self.top.next
      self.length += 1
    else:
      return "No elements present"


    return holderpoint.data

  def peek(self):
    return self.top.data



stack_list = stack()
print(stack_list.pop())
print(stack_list.push("Google"))
print(stack_list.push("Microsoft"))
print(stack_list.push("Facebook"))
print(stack_list.push("Amazon"))
print("Removed element - ", stack_list.pop())

print("Top element in the stack - ", stack_list.peek())
