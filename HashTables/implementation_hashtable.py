class HashTable:
  def __init__(self):
    self.bucket = 10
    self.hashmap = [[] for i in range(self.bucket)]

  def hash(self,key):
    return len(key) % self.bucket

  def put(self,key,value):
    hashvalue = self.hash(key)
    reference = self.hashmap[hashvalue]

    for i in range(len(reference)):
      if(reference[i][0] == key):
        reference[i][1] = value
        return "Over written"

    reference.append([key,value])
    return "Appended"


  def get(self,key):
    hashvalue = self.hash(key)
    reference = self.hashmap[hashvalue]

    for i in range(len(reference)):
      if(reference[i][0] == key):
        return reference[i][1]
    return "Not found giri"

  def remove(self,key):
    hashvalue = self.hash(key)
    reference = self.hashmap[hashvalue]

    for i in range(len(reference)):
      if(reference[i][0] == key):
        reference.pop(i)
        return "Removed"

    return "Element not found"

h = HashTable()
print(h.put("Giri",5))
print(h.put("Giri",10))
print(h.put("giri",10))
print(h.put("giri",100))
print(h.put("Anderson",500))
print(h.hashmap)
print(h.get("giri"))
print(h.remove("girii"))
print(h.hashmap)
