# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

I hung up my cape in the trophy room created back at the beginning of this class. It's 2026 and I got my computer science degree so my way of fighting crime has changed. I do not patrol the streets myself anymore. Instead I sit in my newly designed Lair and send my drones out to do the crime fighting for me. This unit mapped the city as a graph, using the districts as the nodes and the streets as the edges. BFS decided the dispatch order, so the drones can cover the closest districts first and work their way out.

## Implementation

1. **BFS** used a `deque` as the queue and set for visited districts. Each district came off of the front, got added to the visit order, and any unvisited neighbors went to the back. Districts were marked visited when they were queued, not when they came off, so a district that is shared by two streets only got added once.
2. **Graph** Six districts were in an adjacency list. Streets went both ways, so each district listed the other one as well.
3. **Traversal** Dispached from the Lair, Downtown and Uptown came first, then the Docks and Old Town, and then the Warehouse.
4. **New Node** Added the Harbor off the Docks. It showed up on level 3 next to the Warehouse.

## Edge Cases

**Different Start** A drone starting at the Warehouse worked back toward the Lair, so the order flipped.

**Missing Start Node** Suburbs wasn't in the graph. BFS checked first and returned `[]` instead of a KeyError.

**Disconnected Graph** The Island had no streets. Drones from the Lair never reached it, and starting from the Island returned just `[Island]`

## Discussion Board Reflection

It took me a minute to figure out how I wanted to close out my Lair story for the final week. The transition into drones deploying was the best fit. This unit taught me how a graph is stored as an adjacency list and how BFS walks through it one level at a time. The queue does all the work. Whatever goes in first comes out first, so every district next to the Lair gets covered before anything further out.

My biggest challenge in this unit was trying to figure out how to add the Harbor into the mix. I gave the Harbor a street to the Docks, but forgot to give the Docks a street back. Starting from the Harbor worked fine, but drones starting out from the Lair would have never found it. It ran and did the wrong thing, same as the last few units. Streets go both ways, so the edge has to go in both lists.

BFS uses a queue and pans wide level by level, so it finds the shortest route in an unweighted graph, like the smallest amount of streets to get to a crime scene. DFS uses a stack or recursion and follows the one path as far as it can before it has to backtrack, which fits in mazes, folder trees and cycle checks. The choice comes down to memory, since BFS hold a whole level at once on a wide graph, while DFS only keeps track of the path it's on.

