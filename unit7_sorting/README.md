# Unit 7 Discussion: Sorting Algorithms

## Overview

Continuing to upgrade my Lair smart-home. In this unit, the Lair helps me keep track of crime. Crime alerts came in across the city as different threat levels. So the smart hub sorted them with Bubble Sort and Merge Sort so the patrol could work through them in order. Both algorithms got the same data and gave the same answer. They just operate on a functionally different level.

## Implemented

1. **Bubble Sort** Copied the list first so the original alerts can stay untouched. Each pass compared neighbors and swapped them if they were out of order, which shifts the biggest value to the right. A `swapped` variable kept track of whether a pass made any swaps. if it didn't, the list was already sorted and the loop stops early.
2. **Merged Sort** Used recursion. The base case was a list of 0 or 1 values. Anything bigger got split at `mid = len(lst) // 2`, each half got sorted on its own, then the two halves went to `merged()`.
3. **Merge** Compared the front of each half and takes the smaller one. Used `<=` so equal values would keep their original order, which also keeps it stable. Once one half runs out, `extend()` added the rest which was the other half.
4. **Dataset #1** Eight threat levels from 1 to 10 in the order they came in, including a duplicate 4.
5. **Dataset #2** Response times in minutes from the lair to each scene. It was mostly sorted with one late alert out of order, the nearly sorted case from the scenario.


## Edge Cases

**Empty list** A quite night. Bubble sort never entered its loop and Merge Sort hit the base case. Both returned `[]`.

**Single Alert** Nothing to compare, both returned as is.

**Already Sorted** Bubble Sort made one pass with no swaps, and stopped, O(n). Merge Sort still split and merged everything, O(n log n).

**Reverse Sorted** Worst case for Bubble sort, every pair got swapped, O(n^2).

**Duplicates** Both kept every copy, nothing was dropped.

## Discussion Board Reflection

This weeks unit really helped me nail down the difference between the most two common types of sorts. Even though they have completely different algorithms, they arrive at the same answer. Bubble Sort will continously compare to its neighbors until nothing moves. Merge Sort will cut the list in half until every piece is just one value, then it builds it back up in order.

Pythons indentation got me here. In Bubble Sort, I had the early stop check and return tucked inside the loops, so it quit after one pass and gave back None on an empty list. Just one level of indent completely changed what the code did. In the merge step I also grabbed `left[j]` instead of `right[j]`, which would have doubled the alerts up from one half and drop the other. I had to glean through my code line by line to figure out that each loop needs to finish before the next step runs, each index belongs to its own list.

Bubble Sort is O(n^2) average and worst case, but it barely uses any extra memory and stops early on the sorted data. Merge Sort is O(n log n) every time and stable, but it needs the extra space for the temporary lists. I'd use Bubble Sort for tiny or nearly sorted lists and Merge Sort for anything bigger.