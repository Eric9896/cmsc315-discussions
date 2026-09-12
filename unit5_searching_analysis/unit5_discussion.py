"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Checks all cards front to back. Worst case is the last card or a miss,
    # so the work grows one for one with the list. That is O(n).
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        # Middle is too small, so left of everything is thrown out.
        if lst[mid] < target:
            low = mid + 1
        # Middle is too big, so everything right of it is thrown out.
        else:
            high = mid - 1
    # Low passed high, nothing left to check. Card is not registered.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")
    print("Lair Keycard Registry")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    registry = [1250, 2500, 3750, 5000, 6250, 7500, 8750]
    print(f"Registry:  {registry}")

    # 7500 gets registered. Both returns index 5, linear took 6 checks and binary took 2.
    print(f"Swipe 7500 - linear {linear_search(registry, 7500)}, binary {binary_search(registry, 7500)} (registered, unlocked)")

    # 3000 was never registered. Both return -1. Linear checked all 7. Binary took 3.
    print(f"Swipe 3000 - linear {linear_search(registry, 3000)}, binary {binary_search(registry, 3000)} (unregistered, deny access)")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # A million card ID range() hands them over already sorted.
    big_registry = list(range(1_000_000))
    last = big_registry[-1]

    # Linear search will walk all million to get to there. And binary
    # havles a million down to one in 20 steps. Doubling the list adds 
    # a million checks to linear and only one check to binary.
    # Thats is O(n) vs O(log n).
    print(f"Swipe {last} - linear {linear_search(big_registry, last)}, binary {binary_search(big_registry, last)}")
    print(f"Worst case checks are linear {len(big_registry)}, binary about 20")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    
    # On an empty registry. Linear never enters the loop, binary starts with high
    # at -1 so the while never runs. Both the -1 and every card is denied.
    empty = []
    print(f"Empty registry, swipe 5000 - linear {linear_search(empty, 5000)}, binary {binary_search(empty, 5000)}")
    #Last card. Linear worst case, all 7 checks. Binary took 3.
    print(f"Last card 8750 - linear {linear_search(registry, 8750)}, binary {binary_search(registry, 8750)}")

    # Unsorted list, the unit 3 patrol route. Linear still finds it. Binary compares against the middle
    # throws out the half that actually has it and misses. Bo error, just a wrong answer. This is why
    # the routestayed a linear scan.
    route = ["Driveway Gate", "North Fence", 'Armory Vault Door', "Trophy Room"]
    print(f"Unsorted route, find 'Armory Vault Door' - linear {linear_search(route, 'Armory Vault Door')}, binary {binary_search(route, 'Armory Vault Door')}")


if __name__ == "__main__":
    main()