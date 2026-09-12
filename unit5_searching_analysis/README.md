# Unit 5 Discussion: Search Algorithms

## Overview

I continue to build off of the Lair smart-home hub from the previous units. The keycard registry from unit 4 came back, but as a plain sorted list instead of a tree. A swipe searched the list for the card ID in two ways, linear and binary. An index means the card was registered and the door unlocked, and '-1' meant deny.

The scenario was chosen because it also helped put unit 3 and unit 4 side by side. The patrol route could not be sorted because its order was the data, so a linear scan was the only option. Card IDs have no order beyond their value, so the registry could be kept sorted, and binary search is the payoff for keeping it sorted.

## Implementation

### Linear Search

`linear_search()` walked the list front to back and returned the index on the first match or `-1` after the loop ran out. The worst case was the last card or a miss, where every card got checked, so the work grew one for one with the list. O(n)

### Binary Search

`binary_search()` kept a `low` and a `high` index and it checks the middle. A match returned `mid`. If the middle is too small, `low` moves past it. If the middle was too big, `high` moved before it. Half of what's left gets thrown out on every pass. When `low` passed `high` there was nothing left and it returns `-1`. Halving a million down to one took 20 passes, so that is O(log n).

### Small Dataset

The same seven card IDs as the Unit 4 tree, already sorted. Swiping `7500` returned index 5 from both, linear in 6 checks and binary in 2. Swiping `3000` returned `-1` from both. Linear checked all 7 to prove it was missing, binary took 3.

### Large Dataset

`range(1_000_000)` produces a million sorted IDs. Swiping the last one returned the same index from both, but linear goes through all million to get there and binary took 20. Doubling the list would add a million checks to linear and one check to binary. The gap gets wider as the registry grows.

### Edge Cases

**Empty registry.** Linear never entered the loop. Binary started with `high` at `-1`, so the while condition failed on the first check. Both returned `-1` without touching anything, and every card was denied, which is the right default for a door.

**Last card.** `8750` was the linear worst case, all 7 checks. Binary took 3, since the ends of the list are the farthest from the middle.

**Unsorted list.** The Unit 3 patrol route went in unsorted. Linear found "Armory Vault Door" at index 2. Binary compared against the middle, threw out the half that actually held it, and returned `-1`. It did not crash or warn, it just gave a wrong answer. Binary search trusts the order, so on unsorted data it is not slow, it is wrong.

## Reflection

This unit taught me that binary search is not really a search so much as a rule for what to throw away. Every comparison answers one question, is the target left or right of here, and half the list is gone. Linear search never throws anything away, so it has to check everything to prove something is missing.

My challenge was the loop condition. My first version used `low < high` instead of `low <= high`, and the swipe for `8750` came back `-1` even though it was the last card in the list. When the range shrank to a single index the loop quit before checking it. Same lesson as the last three units, the code ran fine and the answer was wrong.

The patrol route and the keycard registry are what works here for me. The route is unsorted, small, and changes every time I add a checkpoint, so sorting it would cost more than the scan saves and would wreck the walking order anyway. Linear is the only option there. The registry changes maybe once a month and gets swiped a thousand times a day, so the sort gets paid once and the search gets paid every swipe. That is when binary search wins over linear.