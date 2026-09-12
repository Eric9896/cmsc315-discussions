# Unit 4 Discussion: Binary Search Trees

## Overview

This program continued the Lair smart-home hub from the previous units by storing the keycard registry: ID cards that the door controllers accept. A swipe asked the tree one question, is this card registered, and the answer was unlock (`True`) or deny (`False`).

The scenario was chosen because it is the mirror of Unit 3. The patrol route could not be sorted because its order *was* the data. A keycard ID has no order beyond its value, so the registry could be kept sorted, and the BST is what sorted buys: every comparison throws away one whole side of the tree.

## Implementation

### 1. Node and Tree

`Node` held one card ID and two child references that started as `None`. `BST` held only the root, also `None` until the first insert. Every method treated a `None` node as the end of the tree, so the empty tree never needed special handling.

### 2. Insertion

`insert()` called `_insert_recursive()` and assigned the result back to `self.root`. The helper compared the value at each node: smaller went left, larger went right, and an empty spot became a new `Node`. Each call returned the node it was given so the parent's link stayed valid, which is what connected a new leaf into the tree.

Duplicates were ignored. Registering a card twice still means one card, and storing it twice would leave a second copy behind if the first were ever revoked.

The seven cards were inserted middle value first: `5000`, then `2500` and `7500`, then the four quarter values. That put half the cards left of the root and half right, so each insert compared at the root, dropped into one side, and never touched the other.

### 3. Searching

`search()` called `_search_recursive()`, which returned `True` on a match, `False` after running off the end of a branch, and otherwise went left or right by the same rule as insertion.

Two registered cards, `5000` and `8750`, returned `True`. `5000` was the root, so it took one comparison. Two unregistered cards, `3000` and `9999`, returned `False`. Neither search checked all seven cards. Each followed one path down and stopped when the branch ended. That was the contrast with Unit 3, where a miss on the linear scan cost all n because absence could only be proven by checking everything.

### 4. In-Order Traversal

`inorder()` built a list by visiting the left subtree, then the node, then the right subtree. Because the left side was always smaller and the right side always larger, every value landed after the smaller ones and before the larger ones, and the list came out ascending with no call to `sort()`. The cards went in scrambled and came back sorted. The sorting happened at insert time.

### 5. Edge Cases

**Empty tree.** In-order returned `[]` and search returned `False`. Nothing registered meant every card was denied, which is the right default for a door.

**Duplicate.** Inserting `2500` a second time walked to the existing `2500`, hit the equal case, and returned without creating a node. The in-order list was unchanged.

## Reflection

This unit taught me that a BST is not sorted data so much as a sorting rule applied on every insert. Search is that same rule run again, and in-order is just reading the rule back out. Once that clicked, all three methods felt like the same walk with different endings.

The main challenge was the reattach pattern. My first version created the node in the base case but never assigned the return value back to `node.left` or `self.root`, so every insert built a node and dropped it. The tree stayed empty and nothing crashed. Same lesson as the last two units: code running is not code working. The other bug was the opposite kind, curly braces instead of parentheses on the in-order call, and Python caught that one before the first line ran.

The performance story is the ordering. A linear scan is O(n) because unsorted data gives nothing to skip. A sorted list gets O(log n) search from binary search but pays O(n) shifting on every insert, which was the whole cost story of Unit 3. A balanced BST gets O(log n) for both, because the order lives in the links and a new value just hangs off a leaf. The catch is that a plain BST only stays balanced if the input cooperates. Insert the same seven cards smallest first, the way sequential employee IDs arrive, and every node hangs off the right. Height 7 instead of 3, and search is back to O(n).

Badge and keycard systems are the natural real-world fit. The controller needs a fast yes or no on an ID, and the IDs have no meaning beyond their value. The same shape shows up in employee numbers, part numbers, and account IDs, and the same trap does too. A real system shuffles the load, inserts middle first as this program did, or uses a self-balancing tree such as an AVL tree that repairs the shape on every insert.
