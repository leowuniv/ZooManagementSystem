import heapq

class Manage:
  
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

# ===========================================

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
            index = (index + 1) % self.size 
            count += 1
            #index = (index + count + count**2) % self.size
        return None

# ================================

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

# ===========================================================

'''
Part 1: Hash Table (Animal Lookup)
'''

# ===========================================================

'''
Part 2: Binary Search Tree (Care Priority Management)
'''

'''
Care Facilities:
Basic Care: Can handle animals with care levels 1-3.

Advanced: Handles animals with care levels 4-7.

Intensive: Handles animals with care levels 8-10.
'''

# ===========================================================

# Testing here
def main():
  
if __name__ = "__main__":
  main()

