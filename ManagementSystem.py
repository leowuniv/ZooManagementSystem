class Manage:

class HashTable:
  def __init__(self, size=10):
    self.size = size
    self.table = [None] * self.size
    self.deletedMarker = "DELETED"

def hashFunction(self, key):
  return abs(hash(key)) % self.size

def insert(self, key, value): 
  index = self.hashFunction(key) # Hash key to find the index input location
  count = 0

  while count < self.size:
    if self.table[index] is None or self.table[index] == self.deletedMarker or self.table[index][0] == key: # Check is hashed index is free
      self.table[index] = (key, value) # Place it there if it is free
      return
    index = (index + 1) % self.size
    count += 1
  raise Exception("Hash Table is full")

def get(self, key):
  index = self.hashFunction(key) # Hash initial index
  count = 0

  while count < self.size:
    if self.table[index] is None:
      return None
    if self.table[index] != self.deletedMarker and self.table[index][0] == key:
      return self.table[index][1]
    index = (index + 1) % self.size
    count += 1
  return None
  
def delete(self, key):
  index = self.hashFunction(key) # Hash to the initial index of the key
  count = 0 

  while count < self.size: 
    if self.table[index] is None:
      return None
    if self.table[index] != self.deletedMarker and self.table[index][0] == key:
      poppedValue = self.table[index]
      self.table[index] = self.deletedMarker
      return poppedValue
    index = (index + 1) % self.size
    count += 1
  return None
