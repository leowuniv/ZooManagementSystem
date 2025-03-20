# ZooManagementSystem
Lab Week 8 &amp; 9 🐘🦒🐅

A management system for a zoo containing three types of care facilities with different care capacities (**Basic**, **Advanced**, and **Intensive**). The zoo will ensure that animals recieve timely care and attention through this establishment. To manage...

## Objectives
- Demonstrate proficiency in implementing hash tables for rapid animal lookups.

- Use BST structures for efficiently prioritizing animal care.

- Understand the benefits and limitations of different data structures.

## Part 1: Hash Table (Animal Lookup)

Implement a hash table (dictionary insufficient) to store and quickly access animals by their unique names. Each animal will have:

- Name (string, unique identifier)

- Species (e.g., lion, penguin, elephant, etc.)

- Care Level (integer, initially set from 1-10)

Your hash table should:

- Support insertion, deletion, and searching by animal name.

- Handle collisions through chaining or open addressing.

## Part 2: Binary Search Tree (Care Priority Management)

Implement a binary search tree (BST) to prioritize animals based on their care level. Each node will store:

- Care Level (key)

- List of animals sharing the same care level

- Animals' care levels increase over time if they are not attended to, simulating the urgency of care.

Your BST should:

- Support insertion of animals based on care level.

- Efficiently retrieve animals that urgently need attention within a care level range.

---------------------------------------------------------------------------------------------------------

Care Facilities:
Basic Care: Can handle animals with care levels 1-3.

Advanced: Handles animals with care levels 4-7.

Intensive: Handles animals with care levels 8-10.


Tasks
Define Data Structures: Define your hash table and tree node classes clearly.

Implement Hash Table Operations

Implement Tree Operations

Testing:

Populate your structures with at least 10 sample animals.

Demonstrate insertion, deletion, periodic care-level increases, and efficient retrieval of animals based on facility availability.

Deliverables
Your Python implementation (.py file).

Hash Table with collision managment

BST capable of managing animal care needs
Demo
