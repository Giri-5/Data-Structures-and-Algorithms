class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class Linkedlist:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
      self.length = 1

    else:
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1

    return self.tail.data

  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.length +=1
    return self.head.data

  def insert(self,index,data):
    # 10 -> 20 -> 30 -> 40
    new_node = Node(data)
    i = 0
    temp = self.head

    if index >= self.length:
      self.append(data)
      return
    if index == 0:
      self.prepend(data)
      return
    
    while i <self.length:
      if i == index -1:
        new_node.next = temp.next
        temp.next  = new_node
        print(new_node.data)
        print(self.tail.data)
        print(temp.data)
        self.length += 1

        break

      temp = temp.next
      i += 1

  def remove(self,index):
    temp = self.head
    i = 0
    print("First elem", self.head.data)
    print("Second elem", self.head.next.data)
    print("Third elem", self.head.next.next.data)

    if index == 0:
      self.head = self.head.next
      self.length -= 1
      return

    if index >= self.length:
      print("Entered wrong index")

      # 10 -> 15 -> 20 -> 30 -> 40
    while i< self.length:
      if i == index -1:
        print("before removing", temp.next.data)
        temp.next = temp.next.next
        print("After removing", temp.next.data)
        self.length -= 1
        break

      temp = temp.next
      i += 1

  def reverse(self):
    prev = None
    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp.next = prev
      prev = temp

    self.head = prev


  def print(self):

    temp = self.head
    while temp != None:
      print(temp.data,end = ' ')
      temp = temp.next
      
    print()
    print("Length of the list", self.length)
    

  
    






llist = Linkedlist()

print(llist.append(10))
print(llist.append(20))
print(llist.append(30))
print(llist.append(40))

"""llist.insert(1,15)
llist.remove(2)"""
llist.print()
llist.reverse()
llist.print()
