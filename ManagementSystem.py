# import heapq
# class Manage:
  
# **CARE FACILITIES** cannot be used by multiple animals at the same time (can implement as boolean value) --> not a class some data structure

# if animal in the facility then NOT AVAILABLE HAVE TO WAIT THE TURN (hash table and binary tree)

# facility can exist free floating does NOT HAVE TO EXIST IN ANY DATA STRUCTURE

'''
Binary Search Tree
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None # Left Child
        self.right = None # Right Child

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, current, target):
        if current is None: # Check if current existsm it not then return False or None
            return None
        if target == current.data: # If current exists, checj target
            return current
        elif target < current.data:
            return self.search(current.left, target) # search left if target < current
        else:
            return self.search(current.right, target) # search right subtree if target is greater than current

    def iterativeSearch(self, target):
        current = self.root
        while current != None:
            if current.data == target:
                return current
            elif current.data > target:
                current = current.left
            else:
                current = current.right
        return None
    
    def insert(self, current, data):
        if current is None: # Make new node at this location if current is none
            return Node(data)
        elif data == current.data: # Check for duplicates; if none, navigate to appropriate subtree
            print("No duplicates") 
            return current
        elif data < current.data: # Navgiate to appropriate subtree if not none
            current.left = self.insert(current.left, data)
        else:
            current.right = self.insert(current.right, data)
            # reutrn the current node to ensure that the subtrees remain linked
        return current 
    
    def delete(self, current, data):
        if current is None: # Step 1: Search for node we are deleting
            return None
        elif data < current.data:
            current.left = self.delete(current.left, data)
        elif data > current.data:
            current.right = self.delete(current.right, data)
        else:
            # Step 2: Node found; check the case
            # Case 1: if node has no children, delete
            if current.left is None and current.right is None:
                return None
            
            # Case 2: if node has one child, point parent to that child
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else: # Case 3: Node has two children
                # Find the inorder successor, the smallest in the right subtree
                successor = self.inorderSuc(current.right)
                # Replace data with inorder successor's data
                current.data = successor.data
                # Recursively delete old inorder successor in its subtree
                current.right = self.delete(current.right, successor.data)

    def inorderSuc(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Inorder traversal
    def inorderTrav(self, node):
      if node:
        self.inorderTrav(node.left) # travel left if possible
        print(node.current) # print the current data
        self.inorderTrav(node.right) # travel right if possible
        
    # Preorder traversal
    def preorderTrav(self, node)
      if node:
        print(node.data) # print current data
        self.preorderTrav(node.left) # travel left if possible
        self.preorderTrav(node.right) # travel right if possible

    # Postorder traversal
    def postorderTrav(self, node)
      if node:
        self.postorderTrav(node.left) # travel left if possible
        self.postorderTrav(node.right) # travel right if possible
        print(node.data) # print current data
# ===========================================

'''
Hash Table
'''

class HashTable:
    def __init__(self, size=10):
        self.size = size 
        self.table = [None] * self.size
        self.deletedMarker = "DELETED"
        
    def hashFunction(self, key):
        return abs(hash(key)) % self.size
        
    def insert(self, key, value): # Hash key to find index input location
        index = self.hashFunction(key)
        count = 0
        
        while count < self.size:
            if self.table[index] is None or self.table[index] == self.deletedMarker or self.table[index][0] == key: # Check if the hashed index is free, is so store there
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size # If not linear probe: keep checking next index for a spot (stop when found)
            count += 1 
        raise Exception("Hash Table is full") #alternatively: resize and grow the hashtable
                
    def get(self, key):
        index = self.hashFunction(key) # Hash initial index
        count = 0
        
        while count < self.size: # probe through table until we find our key/run out of elements
            if self.table[index] is None: # Find none = key does not exist, exit early
                return None
            if self.table[index] != self.deletedMarker and self.table[index][0] == key: # Find key = return and exit early
                return self.table[index][1]
            index = (index + 1) % self.size # If another key is found or if we find a "DELETED" keep probing!
            count += 1
        return None
        
    def delete(self, key):
        index = self.hashFunction(key) # Hash initial index of the key
        count = 0
        
        while count < self.size: # probe through table until we find our key/confirm it is not present
            if self.table[index] is None: # Find none = key does not exist, exit early
                return None
            if self.table[index] != self.deletedMarker and self.table[index][0] == key: # If we find key then we replace key with deleted marker
                poppedValue = self.table[index]
                self.table[index] = self.deletedMarker
                return poppedValue
            index = (index + 1) % self.size # address linear probing (open addressing)
            count += 1
            #index = (index + count + count**2) % self.size
        return None
  
# ================================

'''
Hash Table Linked List
'''
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
            
class HashTableLL:
    def __init_(self, size=10):
        self.size = size 
        self.table = [None] * self.size
        
    def hashFunction(self, key):
        return abs(hash(key)) % self.size
        
    def insert(self, key, value): 
        index = self.hashFunction(key)
        head = self.table[index]
        if head is None:
            self.table[index] = Node(key, value)
            return
        
        current = head
        prev = None
        while current:
            if current.key == key:
                current.value = value
                return
            prev = current
            current = current.next
            
        newNode = Node(key, value)
        prev.next = newNode
        
    def get(self, key):
        index = self.hashFunction(key)
        head = self.table[index]
        current = head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
        
    def delete(self, key):
        index = self.hashFunction(key)
        head = self.table[index]
        current = head
        prev = None
        while current: 
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return current.value
            prev = current
            current = current.next
        return None
'''
# ===========================================================

'''
Part 1: Hash Table (Animal Lookup)

Stores animals by unique names

Include:
- Insertion
- Deletion
- Searching by name
'''

# Name (string, unique identifier)
# Species (e.g., lion, penguin, elephant, etc.)
# Care Level (integer, initially set from 1-10)

class animalLookup:
    def __init__(self, name, species, careLevel):
        self.name = name
        self.species = species
        self.careLevel = careLevel

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Care Level: {self.careLevel}"

# ===========================================================

'''
Part 2: Binary Search Tree (Care Priority Management)

Ensure that animals are with greater values are handles first.
Ex. 10 > 8, animals with a 10 priority care will have priority in the intensive care before a level 8 animal.
'''

'''
Care Facilities:
Basic Care: Can handle animals with care levels 1-3.

Advanced: Handles animals with care levels 4-7.

Intensive: Handles animals with care levels 8-10.
'''

# Each node will store:
# Care Level (key)
# List of animals sharing the same care level

# Important Implementation: Animals' care levels increase over time if they are not attended to, simulating the urgency of care.

class Manage:

# ===========================================================

# Testing here (part 1)
def main1():
    lookup = HashTable()
    t1 = animalLookup("a", "Lion", 6)
    t2 = animalLookup("b", "Penguin", 2)
    t3 = animalLookup("c", "Elephant", 8)
    t4 = animalLookup("d", "Eagle", 10)
    t5 = animalLookup("e", "Ants", 1)
    
    # add and search testing
    lookup.insert(t1.name, t1)
    lookup.insert(t2.name, t2)
    lookup.insert(t3.name, t3)
    lookup.insert(t4.name, t4)
    lookup.insert(t5.name, t5)
    search1 = lookup.get("a")
    print(search1)
    search2 = lookup.get("b")
    print(search2)
    search3 = lookup.get("c")
    print(search3)
    
    # delete test
    lookup.delete("a")
    print(lookup.get("a"))
  
'''
Testing:

Populate your structures with at least 10 sample animals.

Demonstrate insertion, deletion, periodic care-level increases, and efficient retrieval of animals based on facility availability.
'''
def main2():
  
if __name__ == "__main__":
  main1() # part 1
  main2() # part 2
