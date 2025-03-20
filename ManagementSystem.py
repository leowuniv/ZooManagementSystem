class Manage:

def hashFunction(self, key):
  return abs(hash(key)) % self.size
  
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
