class Array_stack:
  def __init__(self):
    self.arr = []
    self.length = 0

  def peek(self):
    return self.arr[self.length - 1]

  def push(self,data):
    self.arr.append(data)
    self.length += 1
    return self.arr[self.length-1]

  def pop(self):
    popped_item = self.arr[self.length - 1]
    del self.arr[self.length - 1]
    self.length -= 1

    return popped_item


array_s = Array_stack()
print(array_s.push("Giri"))
print(array_s.push("Hari"))
print("Top element", array_s.peek())
print("Top removed element", array_s.pop())
