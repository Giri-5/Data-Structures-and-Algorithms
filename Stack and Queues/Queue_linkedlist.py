class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    return self.first.data

  def enqueue(self,data):
    new_node = Node(data)
    if self.first == None:
      self.first = new_node
      self.last = self.first
      

    else:
      self.last.next = new_node
      self.last = new_node

    self.length += 1

  def dequeue(self):
    temp = self.first.next
    self.first.next = None
    self.first = temp
    self.length -= 1

    return self.first.data

  
ll_queue = Queue()
ll_queue.enqueue("Giri")
ll_queue.enqueue("Giridhar")
ll_queue.enqueue("Giridharan")
print(ll_queue.dequeue())

