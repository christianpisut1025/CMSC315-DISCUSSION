# Unit 2 Discussion: Stacks and Queues

## Overview

This project explored two fundamental linear data structures:

- Stack using last-in, first-out (LIFO) behavior
- Queue using first-in, first-out (FIFO) behavior

## Implementation

The stack was implemented with a Python list. The `push()` method appended an item to the top, while `pop()` removed the most recently added item. The `peek()` method returned the top item without removing it.

The queue was implemented with `collections.deque`. The `enqueue()` method added an item to the back, while `dequeue()` removed the oldest item from the front. The `front()` method returned the oldest item without removing it.

Both structures safely returned `None` when removal or viewing operations were attempted while empty.

## Demonstrations and Edge Cases

The program demonstrated:

- LIFO behavior through a text-editor undo history
- FIFO behavior through an IT support-ticket queue
- Empty stack and queue operations
- Single-item stack and queue boundary conditions
- A combined support-desk simulation using both structures

## Discussion Board Reflection

While completing this assignment, I learned how stacks and queues control the order in which data is accessed. I implemented stack operations with a Python list and queue operations with `collections.deque`. The stack removed the newest item first, demonstrating LIFO behavior, while the queue removed the oldest item first, demonstrating FIFO behavior. I also learned how `peek()` and `front()` could inspect values without changing either structure.

One challenge I encountered was configuring Python 3.14 as the interpreter in IntelliJ. The project initially attempted to use the previous Unit 1 run configuration. I resolved this by installing Python, adding it as the project SDK, and creating the correct Unit 2 run configuration. I also handled empty structures by returning `None`, which prevented invalid removal operations from crashing the program.

Stacks are useful for text-editor undo histories because the latest action should be reversed first. Queues are useful for IT support tickets because requests should normally be handled in their arrival order. The custom support-desk scenario demonstrated how both structures could work together in one application.
