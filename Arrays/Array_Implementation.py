class Array:
  def __init__(self):
    self.length = 0
    self.arr = {}

  def get(self,index):
    return self.arr[index]

  def push(self,elem):
    self.arr[self.length] = elem
    self.length+= 1

  def pop(self):
    popped = self.arr[self.length-1]
    del self.arr[self.length-1]
    self.length -= 1
    return popped

  def delete(self,index):
    deleted_item = self.arr[index]
    for i in range(index,self.length-1):
      self.arr[i] = self.arr[i+1]
      
    del self.arr[self.length-1]
    self.length -= 1
    return deleted_item





obj1 = Array()
print(obj1.length)
print(obj1.arr)

obj1.push(7)

obj1.push(8)
obj1.push(11)
obj1.push(16)
obj1.push(9)
print(obj1.arr)

print(obj1.length)

print(obj1.delete(2))

print(obj1.arr)
print(obj1.length)

print(obj1.get(3))
