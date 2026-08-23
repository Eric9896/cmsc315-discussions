# Unit 2 Discussion: Stacks and Queues

## Overview

This program continued the smart-home hub ("Lair") from Unit 1 by adding the security layer that decides what the hub is allowed to do. Two structures ran that pipeline, and each one needed a different ordering rule:

- **Queue (FIFO)** — the pending approval line. Access requests from lair systems were reviewed in the order they arrived.
- **Stack (LIFO)** — the rollback history of security changes already applied. Re-securing the lair reversed the newest change first.

The scenario was chosen because the ordering was not a style preference in either case. FIFO was what kept the approval line fair, and LIFO was what made the rollback valid.

## Implementation

### 1. Stack Operations (LIFO)

The `Stack` class stored values in a Python list, assigned to `self._items` in the constructor. A list was the right internal structure because adding to the end and removing from the end are both O(1) — no items have to shift positions.

`push()` appended to the end of the list and `pop()` removed from that same end. Because both operations worked on one end, the most recently added item was always the next one out, which is what LIFO means at the mechanical level. `peek()` returned the item at index `-1` without removing it, answering "what would come off next?" while leaving the history intact. `is_empty()` returned `True` when no values remained.

### 2. Queue Operations (FIFO)

The `Queue` class stored values in a `collections.deque`. This mattered for performance: `deque` removes from the front in O(1), while a plain list would be O(n) per dequeue because every remaining item shifts down one slot each time.

`enqueue()` appended to the back while `dequeue()` used `popleft()` to remove from the front. Because the two operations used **opposite** ends, arrival order was preserved and a newer request could not cut ahead of an older one. `front()` returned the item at index `0` — the request that had been waiting longest — without removing it. `is_empty()` mirrored the stack.

### 3. Demonstrating LIFO

The `main_stack()` function pushed four security changes that each depended on the one before it: `UNLOCK - Armory Vault`, `DISABLE - Vault Alarm`, `OPEN - Suit Display Case`, and `EQUIP - Flight Suit`. Re-securing the lair popped them in exact reverse order.

This made the reason for LIFO concrete rather than abstract. Reversing `UNLOCK` first would have sealed the vault with the display case still open and the alarm still off, leaving the lair less secure than before the rollback started. LIFO unwound the dependencies in the only order that actually re-secured everything.

### 4. Demonstrating FIFO

The `main_queue()` function enqueued four access requests — `REQ-01` through `REQ-04`, covering the driveway gate, the vault, the trophy room lights, and the perimeter cameras — and dequeued them in arrival order. `REQ-01` had waited the longest, so it was approved first. The output noted the failure mode this prevented: under LIFO, newer requests would keep piling on top of the gate request and it might never be seen.

### 5. Edge Cases

**Empty structures.** Both classes raised `IndexError` on `pop()`, `peek()`, `dequeue()`, and `front()` when empty. `IndexError` was chosen because it is what Python's own `list.pop()` raises on an empty list, so the behavior matched what a Python developer would already expect without having to read the class first. Returning `None` was rejected because it would have made "nothing left to undo" look identical to a successful undo, and a caller could have missed it. All four cases were caught in `try/except` blocks and printed the error message instead of crashing.

**Single-item structures.** A stack holding only `DIM Trophy Room Lights` and a queue holding only `REQ-05 Workshop power up tools` were each emptied and then verified with `is_empty()` returning `True`. This confirmed the boundary between one item and zero items was handled correctly.

### 6. Memory Growth

Both structures stored one reference per item, so memory use grew linearly with the number of items — O(n) space. Nothing was duplicated or precomputed, so n changes in the rollback history meant n slots held.

The operations themselves were O(1) and used no extra space per call: `push` and `pop` touched one end of the list, and `enqueue` and `dequeue` touched one end of the deque. Cost scaled with what was **stored**, not with what was **done**.

### 7. Program Structure

In the starter file, the queue demo block and both placeholder `print()` statements were written at module level rather than inside `main()`, so they executed on import instead of as part of the program. The demo work was reorganized into two functions, `main_stack()` and `main_queue()`, which `main()` calls in order.

## Reflection

This unit taught me that the ordering rule in each structure is not a convention but a consequence of which end the operations touch. Writing `push()` and `pop()` myself made that concrete in a way that reading about it did not.

The challenges were mostly my own mistakes, and the most useful one never crashed. My `front()` method originally returned `len(self._items) == [0]`, which compared a number to a list and evaluated to `False` every time. The program ran without any error and simply printed `False` where the request should have been. That was a better lesson than any of the syntax errors I made, because it showed that code running is not the same as code working. I also had a naming inconsistency where the constructor created `self._items` but other methods read `self.items`. Python reported that as an `AttributeError` pointing at the method rather than the constructor, so I had to trace backward to find the real cause.

Stacks and queues map to genuinely different problems. A stack fits anything that unwinds — undo, browser history, the call stack. A queue fits anything where waiting order has to be respected, like a print spooler.
