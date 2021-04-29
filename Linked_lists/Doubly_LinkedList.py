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
      new_node.prev = self.tail
      self.tail = new_node
      self.length += 1
      """When i printed the below statement after the if condition ended, for the very first time load, self.tail will be self.head, when I print the prev node address will be none, so .data will throw error."""
      print("last",self.tail.prev.data)

    
    
    return self.tail.data

  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
    self.length +=1
    print("Prepended data", self.head.data)

  def insert(self,index,data):
    new_node = Node(data)
    i = 0
    temp = self.head

    if index == 0:
      new_node = self.prepend(data)
      return

    if index >= self.length:
      new_node = self.append(data)
      return


    while i < self.length:
      if i == index-1:
        leader = temp
        follower = temp.next
        leader.next = new_node
        new_node.next = follower
        new_node.prev = leader
        follower.prev = new_node
        self.length += 1
        break
      temp = temp.next
      i += 1


  def remove(self,index):
        temp = self.head
        i = 0
    
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return

        while i < self.length:
          if i == index -1:
            leader = temp
            follower = temp.next.next
            leader.next = follower
            follower.prev = leader
            self.length -= 1
            break

          temp = temp.next
          i += 1

  def print(self):
    temp = self.head
    while(temp):
      print(temp.data,end = " ")

      temp = temp.next




llist = Linkedlist()

print(llist.append(10))
print(llist.append(20))
llist.prepend(5)
llist.insert(2,15)
llist.insert(0,2)
llist.remove(2)
print(llist.length)
llist.print()

