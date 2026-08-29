# Unit 3 Discussion: List Operations

## Overview

This program continued the Lair smart-home hub from Units 1 and 2 by storing the perimeter patrol route: the checkpoints the security sweep walks, in walk order.

The scenario was chosen because position in the list *is* position in the route. The index was not just a storage slot, it was the order the sweep happened in. That drove every decision below. The insertion index was never arbitrary, and the route could not be sorted to speed up searching without destroying the thing it represented.

## Implementation

### 1. Insertion

`insert_at()` used `list.insert()`, which opens a slot by shifting every element from that index one position to the **right**. Nothing was overwritten or lost, but every checkpoint after the new one was renumbered.

The cost depended on *where* the insertion happened, not on what was inserted. Storing the value was a single assignment in every case — the shifting was the entire cost. Inserting at the end moved 0 elements, O(1). Inserting in the middle moved about half. Inserting at index 0 moved all n, O(n), the worst case.

The demonstration ran all three on the same route and printed the number of elements that shifted next to each one: 4, then 2, then 0. Same operation, same value, three different costs, and the only thing that changed was position.

### 2. Deletion

`delete_at()` validated the index first, then used `list.pop(index)`, which closes the gap by shifting everything after the removed item one position to the **left**. Delete was the exact mirror of insert, including the cost profile — removing the last checkpoint moved nothing, removing index 0 moved everything remaining.

The bounds were written as `0 <= index < len(lst)` deliberately so that negative indexes were rejected. Python reads `-1` as "the last item", so an unguarded `pop(-1)` would have asked for "checkpoint -1" and deleted a real checkpoint while reporting success. A wrong answer returned confidently is worse than an error. An `isinstance()` check was included as well, because a string index would raise `TypeError` on the comparison itself before `pop()` ever ran.

The empty list needed no special case. When `len(lst)` is 0, the condition `0 <= index < 0` is false for every index, so an empty route fell through the same guard.

### 3. Searching

`search_value()` walked forward from index 0 and returned the first matching index, or `-1` when the value was absent.

It had to scan sequentially because the route was ordered by **patrol sequence, not sorted**. Binary search needs sorted data so it can discard half the remaining range at each step. Here, learning that checkpoint [2] was not the target said nothing about whether the target sat to its left or its right, so no half could be thrown away and every element still had to be compared. The ordering that made it a route was exactly what ruled out the faster search.

Best case was O(1) and worst case O(n). A miss was always the worst case, since absence cannot be proven without checking all n.

### 4. Edge Cases

**Invalid index.** `delete_at(route, 99)` and `delete_at(route, -1)` both returned `None` and left the route untouched. The negative one was the case that would have failed silently.

**Empty list.** `delete_at([], 0)` returned `None` and `search_value([], 'x')` returned `-1`, while `insert_at()` stayed valid on an empty route, since insertion is what rebuilds one from nothing.

**Insert does not validate.** `list.insert()` does *not* raise on an out-of-range index the way `pop()` does. It silently clamps and appends, so `insert_at(route, 99, ...)` ran with no error at all. This meant validation had to be written per operation rather than assumed across the file.

One related trap was noted in the output. `-1` is the conventional "not found" sentinel, but it is also a legal Python index, so a caller who passes the search result straight into `route[...]` without checking gets the **last** checkpoint back instead of an error.

## Reflection

This unit taught me that the cost of a list operation lives in the shifting, not in the operation. Insert and delete do the same amount of work on the value itself and a completely different amount of work on everything around it. Printing the number of elements that moved next to each call made that concrete in a way the notation on its own did not.

My main challenge was an assumption I did not know I had. I guarded `delete_at()` carefully against bad indexes and assumed `insert_at()` was protected the same way, then found that `list.insert()` accepts an out-of-range index and quietly appends instead of raising. Nothing crashed, which is exactly what made it worth catching. Same lesson as the `front()` bug in Unit 2 — code running is not code working.

Lists show up anywhere order is the point. A music playlist is the clearest one: dragging a song into the middle shifts everything after it, and you scan it linearly because it is sequenced by how you want to hear it, not sorted for lookup. Sorting it to search faster would destroy the playlist. At scale this is where it bites, since front-inserting into an array-backed list is O(n) per call and code that looks fine at five items falls over at fifty thousand.

The list does not just hold the checkpoints. It holds the order, and the order is the job.
