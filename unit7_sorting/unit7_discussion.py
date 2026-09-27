"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Copy first so the original alert board stays untouched
    result = lst[:]
    n = len(result)

    # Each pass will bubble the bigggest remaining value to the end
    for i in range(n - 1):
        swapped = False
        # The last i spots are already sorted, so they get skipped.
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        # No swaps mean the list is sorted, stop early. Sorted input is O(n).
        if not swapped:
            break
    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case. Zero or one alert got sorted already
    if len(lst) <= 1:
        return lst[:]

    # Splits the board in half and sorts each half on its own.
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # Stitch back the sorted halves together. log n levels of splits, O(n) works per level.
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = j = 0

    # Keeps ties to the original order, but takes the front value from either half, which
    # is what makes the merge sort stable.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One half ran out first, whatever is left in the other half is already sorted.
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")
    print("Lair Crime Alert Board")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # The lair picked up crime alerts from all over the city tonight. Each one is a threat level
    # from 1 to 10 in the order they came in. Sorted so the patrol can work up the list.
    threats = [7, 2, 9, 4, 4, 10, 1, 6]
    print(f"Threat levels: {threats}")
    print(f'Bubble sort: {bubble_sort(threats)}')
    print(f"Merge sort: {merge_sort(threats)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    # Response times in minutes from the Lair to each crime scene. Mostly sorted already,
    # one late alert came in out of place, which is where bubble sort early stop helps.
    response = [3, 5, 8, 12, 15, 6, 20, 25]
    print(f"Response times: {response}")
    bubble = bubble_sort(response)
    merged = merge_sort(response)
    print(f"Bubble sort: {bubble}")
    print(f"Merged sort: {merged}")
    print(f"Same result: {bubble == merged}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Quiet night, no alerts. Bubble sort never enters its loop and merge sort hits the base case.
    print(f"Empty: {bubble_sort([])} - {merge_sort([])}")

    # One alert pops in. Nothing to compare to, so both hands it straight back
    print(f"Single: {bubble_sort([8])} - {merge_sort([8])}")

    # Sorted already. Bubble sort makes one pass with no swaps and stops. Merge sort will still split
    # and merge everything, O(n log n) either way.
    print(f"Sorted: {bubble_sort([1, 2, 3, 4, 5])} - {merge_sort([1, 2, 3, 4, 5])}")

    # Reverse sorted. Worst case for bubble sort, every pair swaps, O(n^2).
    print(f"Reverse: {bubble_sort([5, 4, 3, 2, 1])} - {merge_sort([5, 4, 3, 2, 1])}")

    # Duplicate threat levels. Both keeps every copy and nothing gets dropped.
    print(f"Duplicates: {bubble_sort([6, 3, 6, 3, 6])} - {merge_sort([6, 3, 6, 3, 6])}")


if __name__ == "__main__":
    main()