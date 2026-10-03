"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Missing starts (including an empty graph) have no reachable nodes.
    if start not in graph:
        return []

    # FIFO processing explores nearby nodes before more distant nodes.
    # DFS instead follows one branch deeply using a stack or recursion.
    queue = deque([start])
    visited = {start}
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)
        # Neighbors wait at the back while earlier discoveries are processed.
        for neighbor in graph.get(current, []):
            # Mark on enqueue to prevent duplicate scheduling in cycles.
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    # Devices are nodes; bidirectional communication links are edges.
    graph = {
        "Router": ["Switch A", "Switch B"],
        "Switch A": ["Router", "Workstation", "Printer"],
        "Switch B": ["Router", "Server"],
        "Workstation": ["Switch A"],
        "Printer": ["Switch A"],
        "Server": ["Switch B"],
    }
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    start = "Router"
    print("Original order:", " -> ".join(bfs(graph, start)))
    # BFS completes each hop level before expanding the next one.
    print("Level 0: Router; level 1: Switch A, Switch B;")
    print("Level 2: Workstation, Printer, Server.")
    print("Neighbor list order determines the order within a level.")

    # Add a seventh device and its two-way link to the server.
    graph["Server"].append("Backup Server")
    graph["Backup Server"] = ["Server"]
    print("Added link: Server <-> Backup Server")
    print("Updated order:", " -> ".join(bfs(graph, start)))
    print("Backup Server is visited at level 3, after all level 2 devices.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("Different start:", " -> ".join(bfs(graph, "Printer")))
    print("Starting at Printer changes the hop levels and traversal order.")

    # This isolated device is outside the router's connected component.
    graph["Guest Device"] = []
    result = bfs(graph, "Router")
    print("Disconnected graph:", " -> ".join(result))
    print("Guest Device is omitted because no link reaches it.")
    assert "Guest Device" not in result
    print("Isolated start:", bfs(graph, "Guest Device"))
    print("An isolated starting device visits only itself.")
    print("Missing start:", bfs(graph, "Unknown"))
    print("A missing starting device returns an empty list safely.")
    print("Empty graph:", bfs({}, "Router"))
    print("An empty graph also returns an empty list.")
    print("Single node:", bfs({"Router": []}, "Router"))
    print("A single existing device visits itself without any links.")

    # A cycle and shared neighbor must not cause repeated discoveries.
    cycle = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    print("Cycle:", bfs(cycle, "A"))
    print("Each node is visited once despite the cycle and shared neighbors.")
    assert bfs(cycle, "A") == ["A", "B", "C"]
    assert bfs(graph, "Unknown") == []
    assert bfs({}, "Router") == []
    assert bfs({"Router": []}, "Router") == ["Router"]



if __name__ == "__main__":
    main()
