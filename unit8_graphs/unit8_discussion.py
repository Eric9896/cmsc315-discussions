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
    # Missing start node returns an empty list to avoid a KeyError
    if start not in graph:
        return []

    # A queue is first in, first out, so the drones cover every district next door before flying any further.
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        # Neighbors go to the back of the line, to make them wait for the current level to finish.
        # Marked visited when queued, so a district with two streets sharing don't get added twice.
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # DFS would use a stack instead and chase one street to the end before backtracking.
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")
    print("Lair Drone Dispatch")

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

    # Nodes are city districts, edges are the streets a drone can fly between.
    # Streets are two way, so each district lists the other one as well.
    city = {
        "Lair": ["Downtown", "Uptown"],
        "Downtown": ["Lair", "Docks", "Old Town"],
        "Uptown": ["Lair", "Old Town"],
        "Docks": ["Downtown", "Warehouse"],
        "Old Town": ["Downtown", "Uptown"],
        "Warehouse": ["Docks"],
    }
    for district, streets in city.items():
        print(f"{district} - {', '.join(streets)}")

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

    # Drones launch from the Lair. Level 1 is Downtown and Uptown, level 2 are the Docks
    # and Old Town, level 3 is the Warehouse. Closest districts are evaluated first.
    print(f"Dispatch from Lair: {bfs(city, 'Lair')}")

    # New area located off of the Docks, it is added into level 3 with the Warehouse
    city["Harbor"] = ["Docks"]
    city["Docks"].append("Harbor")
    print(f"After adding Harbor: {bfs(city, 'Lair')}")

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

    # Different start. A drone operating out at the Warehouse makes its return back to the Lair
    print(f"Start from the Warehouse: {bfs(city, 'Warehouse')}")

    # Missing start node. There's no district named Suburbs, so the drone stays home.
    print(f"Start from the Suburbs: {bfs(city, 'Suburbs')}")

    # Disconnected graph. The Island has no streets, so the drones from the Lair never reach it.
    city["Island"] = []
    print(f"Island reached from Lair: {'Island' in bfs(city, 'Lair')}")
    print(f"Start from Island: {bfs(city, 'Island')}")


if __name__ == "__main__":
    main()