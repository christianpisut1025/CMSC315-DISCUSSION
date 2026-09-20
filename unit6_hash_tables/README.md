# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used a Python dictionary to demonstrate hash table behavior through a network-device inventory. Unique device IDs served as keys, while nested dictionaries stored each device's type, location, and status.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation Summary

I created five device records and demonstrated insertion, lookup, update, and deletion operations. I looked up a router and a SATCOM terminal by device ID, changed the terminal status from Standby to Online, and removed a wireless access point. I also tested four edge cases: a missing lookup, safe deletion of a missing key, insertion through an absent key, and lookup in an empty dictionary. The output labeled every operation so each state change was easy to follow.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Reflection

While completing this assignment, I learned how Python dictionaries use key-value pairs to model hash table operations. My network-device inventory used unique device IDs as keys and stored each device's type, location, and status as its value. I practiced inserting, retrieving, updating, and deleting records while keeping the output easy to follow. The most useful skill was handling missing keys safely. Direct access or deletion can raise a KeyError, so I used get() and pop() with default values to prevent the program from stopping. I also checked membership before adding a missing device so the program clearly explained whether it was updating or inserting a record.

A hash table applies a hash function to a key to determine where its value should be stored. A collision occurs when different keys map to the same internal location. Python resolves collisions automatically, although frequent collisions can require extra comparisons and reduce performance. With a well-distributed hash function and a reasonable load factor, dictionary lookup, insertion, update, and deletion usually run in average O(1) time. This efficiency makes dictionaries useful for device inventories because an administrator can retrieve a specific record without scanning the entire collection.
