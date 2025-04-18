from typing import Any, Generator
#https://docs.python.org/3/library/typing.html

class Animal:
  def __init__(self, name: str, species:str, care:int) -> None:
    self.name:str = name 
    self.species:str = species 
    # make sure care is between 1-10
    care = 10 if care > 10 else care
    care = 1 if care < 1 else care
    self.care:int = care 

  def __str__(self) -> str:
    return f"{self.name}: ({self.species}), Care - {self.care}"

  def __getitem__(self, key) -> str|int:
    return getattr(self, key)
  
  def __setitem__(self, key, value):
    return setattr(self, key, value)
  
  def __eq__(self, value: object|int) -> bool:
    if type(value) is int:
      return self.care == value
    return self.care == value.care
  
  def __ne__(self, value: object|int) -> bool:
    if type(value) is int:
      return self.care != value
    return self.care != value.care
  
  def __lt__(self, value: object|int) -> bool:
    if type(value) is int:
      return self.care < value
    return self.care < value.care
  
  def __gt__(self, value: object|int) -> bool:
    if type(value) is int:
      return self.care > value
    return self.care > value.care
  
  def __le__(self, value: object|int) -> bool:
    if type(value) is int:
      return self.care <= value
    return self.care <= value.care
  
  def __ge__(self, value: object|int) -> bool:
    if type(value) is int:
      return self.care >= value
    return self.care >= value.care

class Node:
  def __init__(self, data):
    self.data = data
    self.left: Node|None = None
    self.right: Node|None = None

class BinarySearchTree:
  def __init__(self, root: Any|None = None) -> None:
    if (root is not None) and (type(root) is not Node):
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
    # if root was not initialized with a value, handle here
    if self.root is None:
      self.root = self._insert(self.root, data)
      return 
    return self._insert(self.root, data)
    
  def _insert(self, current, data) -> Any|None:
    # base case: create node at this location if empty 
    if current is None:
      return Node(data)
    # if not, navigate to correct subtree
    elif data <= current.data:
      current.left = self._insert(current.left, data)
    elif data > current.data:
      current.right = self._insert(current.right, data)
    return current
  
  def delete(self, data) -> None:
    if self.root:
      self.root = self._delete(self.root, data)

  def _delete(self, current, data) -> Node|None:
    # base case
    if current is None:
        return 
    
    # If key to be searched is in a subtree
    elif data < current.data:
        current.left = self._delete(current.left, data)
    elif data > current.data:
        current.right = self._delete(current.right, data)
        
    else:
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
        
    return current
  
  def inorder(self) -> Generator[Any]:
    yield from self._inorder(self.root)

  def _inorder(self, current) -> Generator[Any]:
    if current:
      # instead of just printing, allow for them to yield recursively
      yield from self._inorder(current.left)
      yield current.data
      yield from self._inorder(current.right)
  
  def postorder(self) -> Generator[Any]:
    yield from self._postorder(self.root)

  def _postorder(self, current) -> Generator[Any]:
    if current:
      # instead of just printing, allow for them to yield recursively
      yield from self._postorder(current.left)
      yield from self._postorder(current.right)
      yield current.data

class HashTable:
  def __init__(self, size=10):
    self.size = size
    self.table = [None] * self.size
    self.deletedMarker = "DELETED"

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, value):
    return self.insert(key, value)

  def __str__(self):
    output = "{"
    for item in self.table:
      if item is not None and item != self.deletedMarker:
        output += f" {item[0]}: {item[1]},"
    
    if len(output) > 1:
      output = output[:-1]
    output += " }"
    return output

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

class CareManagement:
  def __init__(self) -> None:
    self.animals = BinarySearchTree()

  def __str__(self) -> str:
    output = "Inorder:\n"
    for animal in self.animals.inorder():
      output += str(animal) + " -> "
    if len(output) > 10:
      return output[:-4]
    return output + " None"

  def insert(self, animal: Animal):
    if type(animal) is Animal:
      return self.animals.insert(animal)
    print(f"Cannot insert: not an animal ({animal})")

  def increaseCareLevel(self):
    for animal in self.animals.inorder():
      animal.care += 1

  def decreaseCareLevel(self):
    for animal in self.animals.inorder():
      animal.care -= 1

  def getAtLevel(self, care: int) -> Generator[None, Animal]:
    current = self.animals.search(care) 
    if not current:
      yield None
    
    for animal in self.animals._inorder(current):
      if animal.care != care:
        break
      yield animal

  def removeAnimal(self, animal:Animal) -> None:
    # redefine delete so we can make sure we delete the correct object since we are now doing comparisons with care level by default
    if self.animals.root:
      self.animals.root = self._removeAnimal(self.animals.root, animal)

  def _removeAnimal(self, current, animal):
    """ Specfically compare by name in order to remove animal"""
    if current is None:
        return 
    
    if current.data['name'] == animal['name']:
      # Cases when root has 0 children or right
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
      current.right = self._removeAnimal(current.right, temp.data)
    
    elif animal <= current.data:
        current.left = self._removeAnimal(current.left, animal)
    elif animal > current.data:
        current.right = self._removeAnimal(current.right, animal)
        
    return current
  
class CareFacility(CareManagement):
  def __init__(self, minCare:int, maxCare:int) -> None:
    super().__init__()
    self.MIN_CARE = minCare
    self.MAX_CARE = maxCare

  def intakeAnimal(self, animal:Animal) -> bool:
    if self.MIN_CARE <= animal.care <= self.MAX_CARE:
      self.animals.insert(animal)
      return True
    return False

  def dischargeAnimals(self) -> Generator[None, Animal]:
    """ Pop animals below minimum care level to be handled elsewhere."""
    for animal in self.animals.inorder():
      if animal.care >= self.MIN_CARE:
        return None
      # if current animal is less than min care level, pop inorder until element is >= min care
      self.removeAnimal(animal)
      yield animal
      
  def escalateAnimals(self) -> Generator[None, Animal]:
    """For any animals that have too high of a care level for this facility, pop them from tree to be used elsewhere"""
    # traverse backwards with postorder
    for animal in self.animals.postorder():
      if animal.care <= self.MAX_CARE:
        return None
      # if current animal is less than min care level, pop inorder until element is >= min care
      self.removeAnimal(animal)
      yield animal

if __name__ == "__main__":
  test1 = Animal('Bob', 'Tiger', 1)
  test2 = Animal('Jane', 'Lion', -1)
  test3 = Animal('John', 'Weasel', 3)
  test4 = Animal('Jill', 'Mink', 11)
  test5 = Animal('Jack', 'Ermine', 6)
  test6 = Animal('Jean', 'Tanuki', 11)
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
  management.delete('Wasd')
  for data in management.inorder():
    print(data)

  testTable =  HashTable()
  testTable[test1['name']] = test1
  testTable[test2['name']] = test2
  print(testTable)
  testManagement = CareManagement()
  testManagement.insert(test1)
  testManagement.insert(test2)
  testManagement.insert(test3)
  testManagement.insert(test4)
  testManagement.insert(test5)
  testManagement.insert(test6)
  print(testManagement)
  print(testManagement.getAtLevel(1))
