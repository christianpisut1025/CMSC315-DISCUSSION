# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.


## Implementation and Results

I modeled a small office network using a dictionary of adjacency lists. The six original devices were vertices, and each communication link appeared in both endpoints' lists. I used a deque as a FIFO queue and a set to record discovered devices. I marked devices when I enqueued them, so cycles and shared neighbors did not schedule duplicate visits.

I ran the program with `python unit8_discussion.py`. Starting at Router produced Router → Switch A → Switch B → Workstation → Printer → Server. Router was level 0, both switches were level 1, and their attached devices were level 2. I added Backup Server and a bidirectional Server link; the updated traversal appended Backup Server at level 3. Neighbor insertion order determined ordering within a level.

I demonstrated a different starting device, a disconnected device, an isolated start, a missing start, an empty graph, a single-node graph, and a cycle with shared neighbors. Missing starts and empty graphs returned empty lists. Disconnected devices were omitted unless selected as the start. The cyclic graph visited A, B, and C exactly once. BFS took O(V + E) time and O(V) auxiliary space over reachable nodes and edges. The function returned traversal order rather than an actual route.

## Reflection

I learned how an adjacency list represented relationships between devices and how breadth-first search explored those relationships by hop count. Implementing the queue helped me understand why first-in, first-out processing completed one level before moving to the next. I also learned why the visited set needed to record a device when it entered the queue: otherwise, multiple neighbors could schedule the same device before it was processed.

The most challenging part was coordinating the queue and visited set while keeping bidirectional links consistent. I addressed this by tracing the router, switches, and attached devices level by level and checking the output against that order. I tested missing starts, disconnected devices, an empty graph, and a cycle to verify the boundary behavior.

BFS would be useful for checking network reachability or finding the fewest links between devices in an unweighted graph. DFS would follow one branch deeply before backtracking, making it useful for exploring dependency chains or detecting cycles with additional bookkeeping. Both algorithms could visit reachable nodes efficiently, but BFS would be preferable when the nearest connections mattered. Neither traversal alone would choose the fastest route when links had different costs.
