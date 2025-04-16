from typing import Any, Generator

class Animal:
  def __init__(self, name: str, species:str, care:int) -> None:
    self.name:str = name 
    self.species:str = species 
    # make sure care is between 1-10
    care = 10 if care > 10 else care
    care = 1 if care < 1 else care
    self.care:int = care 

  def __getitem__(self, key) -> str|int:
    return getattr(self, key)
  
  def __setitem__(self, key, val):
    return setattr(self, key, val)

class Node:
  def __init__(self, data):
    self.data = data
    self.left: Node|None = None
    self.right: Node|None = None

class BinarySearchTree:
  def __init__(self, root: Any|None = None) -> None:
    if type(root) is not None and type(root) is not Node:
      root = Node(root)
    self.root: Node|None = root

  def search(self, target) -> Any|None:
    return self._search(self.root, target)

  def _search(self, current, target) -> Any|None:
    # does the current exist, if not then return None
    if current is None:
      return None
    
    if target == current.data:
      return current
    elif target < current.data:
      self._search(current.left, target)
    else:
      self._search(current.right, target)

  def insert(self, data) -> None:
    self._insert(self.root, data)
    
  def _insert(self, current, data) -> Any|None:
    # base case: create node at this location if empty 
    if current is None:
      return Node(data)
    # if not, navigate to correct subtree
    elif data < current.data:
      current.left = self._insert(current.left, data)
    elif data > current.data:
      current.right = self._insert(current.right, data)
    return current
  
  def delete(self, data):
    return self._delete(self.root, data)

  def _delete(self, current, data):
    # base case
    if current is None:
        return 
    
    # If key to be searched is in a subtree
    elif data < current.data:
        current.left = self._delete(current.left, data)
    elif data > current.data:
        current.right = self._delete(current.right, data)
        
    else:
      # If root matches with the given key

      # Cases when root has 0 children or 
      # only right child
      if current.left is None:
        return current.right
      # When root has only left child
      if current.right is None:
        return current.left

      # When both children are present, find inorder successor (leaf of right subtree)
      temp = current.right
      while temp.left is not None:
        temp = temp.left
      current.data = temp.data
      # after moving inorder successor here, delete old one
      current.right = self._delete(current.right, temp.data)
        
    return current.data
  
  def inorder(self) -> Generator[Any]:
    yield from self._inorder(self.root)

  def _inorder(self, current) -> Generator[Any]:
    if current:
      # instead of just printing, allow for them to yield recursively
      yield from self._inorder(current.left)
      yield current.data
      yield from self._inorder(current.right)

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

if __name__ == "__main__":
  test1 = Animal('Bob', 'Tiger', 1)
  test2 = Animal('Jane', 'Lion', -1)
  management = BinarySearchTree('Wasd')
  management.insert(test1['name'])
  management.insert(test2['name'])
  management.insert('a')
  management.insert('g')
  management.insert('d')
  management.insert('f')
  management.insert('c')
  management.insert('e')
  management.insert('b')
  for data in management.inorder():
    print(data)
  management.delete(test1['name'])
  for data in management.inorder():
    print(data)