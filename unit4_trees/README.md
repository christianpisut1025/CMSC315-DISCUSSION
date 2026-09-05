# Unit 4 Discussion: Binary Search Trees

## Overview

This project implemented a Binary Search Tree (BST) as an employee ID lookup system. Each node stored one employee ID and references to its left and right children. Smaller IDs were inserted into the left subtree, while larger IDs were inserted into the right subtree. Duplicate IDs were ignored because employee IDs should be unique.

## Features Completed

- Built a BST with recursive insertion and search methods.
- Inserted 11 employee IDs into both left and right subtrees.
- Used in-order traversal to return the IDs in ascending order.
- Searched for two existing IDs and two missing IDs.
- Tested an empty tree, a duplicate ID, and a single-node tree.

## Real-World Application

The program represented an employee directory organized by employee ID. A BST could help locate a record without scanning every earlier record, provided the tree remained reasonably balanced.

## Discussion Board Reflection

While completing this assignment, I learned how a Binary Search Tree organized data through nodes, child references, and recursive decisions. I implemented insertion by comparing each employee ID with the current node. Smaller IDs moved left, while larger IDs moved right until an empty position was found. I also learned why an in-order traversal produced sorted output: it visited the smaller left subtree, the current node, and then the larger right subtree.

The most challenging part was understanding how each recursive call returned an updated child reference. I worked through the process one comparison at a time and tested the program with 11 employee IDs. I also tested an empty tree, a single-node tree, missing values, and a duplicate ID. The duplicate was ignored because employee IDs should remain unique.

Compared with a list, a balanced BST can search more efficiently because each comparison eliminates an entire subtree, producing average O(log n) search time. A list may require O(n) comparisons. However, a BST can become unbalanced when values are inserted in sorted order. It then resembles a linked list, and searching can degrade to O(n).
