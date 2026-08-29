"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.

OVERVIEW:
Continuation of the Lair smart-home hub from the previous units. This unit
will store the perimeter patrol route: the checkpoints the security sweep
walks, in walk order. Position in the list IS position in the route, so the
index carries the meaning.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert() adds a slot by shifting every element from index RIGHT one position.
    # Nothing is lost, but every checkpoint after it gets renumbered. Cost depends
    # on WHERE: the end moves 0 elements(O(1)), the middle moves n/2, index moves
    # all(O(n), worst case). The shifting costs.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # pop() raises IndexError on a bad index, and a crash happening mid sweep is worse
    # than skipping one checkpoint. Bounds are 0 <= index , len so NEGATIVE indexes are 
    # rejected as well. Empty lists do not need any special cases: 0 <= index < 0 is
    # always false.
    if not isinstance(index, int) or not (0 <= index < len(lst)):
        return None
    
    # pop() closes any gaps by shifting everything after it, left one slot. Deleting
    # the last item moves nothing, index 0 moves all.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear Search: Checks index 0, then 1, then 2, until a match or it hits the end.
    # Can only scan sequentially because the route is ordered by PATROL SEQUENCE, not
    # sorted. Binary search needs sorted data so it can discard half the range each step;
    # Best case O(1), worst case O(n). Miss is always O(n), since every element must get 
    # checked.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("Lair Perimeter Patrol Route")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # The starting route. This order is the walking order.
    route = ["Driveway Gate", "North Fence", "Armory Vault Door", "Trophy Room"]
    print(f"Original route:         {route}")

    # Beginning: The front entry must get cleared before anything else. Index 0.
    # Worst case, all 4 existing checkpoints shift right one slot.
    insert_at(route, 0, "Front Entry")
    print(f"Insert Beginning, 4 move:   {route}")

    # Middle: The shed sits between the north fence and vault door, so index spot 3
    # works perfect. Only two checkpoints after it moves.
    insert_at(route, 3, "Generator Shed")
    print(f"Insert Middle, 2 move:    {route}")

    # End: Passingg len(route) appends. Nothing follows after it, so nothing shifts.
    insert_at(route, len(route), "Hanger")
    print(f"Insert End, 0 move:    {route}")
    print(f"Same operation, three costs. Only the positions changed.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Beginning: The front entry is blocked off. Removing index 0 pulls the
    # remaining 6 checkpoints left one slot. The most hurtful delete here.
    print(f"Delete Beginning, 6 move - removed '{delete_at(route, 0)}'")
    print(f" {route}")

    # Middle: The sheds camera went offline, so stop 2 leaves the rotation. Only 3
    # checkpoints after it gets renumbered.
    print(f"Delete Middle, 3 move - removed '{delete_at(route, 2)}'")
    print(f" {route}")

    # End: len(route) is last - Nothing follows after, so nothing moves. 
    print(f"Delete End, 0 move - removed '{delete_at(route, len(route) -1)}'")
    print(f" {route}")
    print("Delete mirrors insert. Insert shifts right, deletes shift left.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Value that Exists: The scan stops on the first match, the checkpoint
    # in which it was compared to.
    hit = search_value(route, "Armory Vault Door")
    print(f"Search 'Armory Vault Door' - index {hit} (found, {hit + 1} compared)")

    # A value that doesn't exist: the scan runs at full length first, because an
    # absence cannot be proven without having to check all elements.
    hit = search_value(route, "Rooftop pad")
    print(f"Search 'Rooftop Pad - index {hit} (not found, all {len(route)} compared)")
    print(f" Careful: -1 is a legal python index. route[-1] is '{route[-1]}', so a")
    print(f" caller who skips the check gets the Last stop instead of an error.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Invalid index. 99 is past the end, and -1 would delete a real checkpoint.
    # Both are rejected, so that the route is left untouched
    print(f"delete_at(route, 99) - {delete_at(route, 99)}")
    print(f"delete_at(route, -1) - {delete_at(route, -1)} (would have deleted '{route[-1]}')")

    # Empty List. Delete and search have to fail cleanly on an empty route, while
    # insert is the one operation still valid. 
    empty = []
    print(f"delete_at([], 0) - {delete_at(empty, 0)} search_value([], 'x') - {search_value(empty, 'x')}")
    insert_at(empty, 0, "Driveway Gate")
    print(f" insert into empty route - {empty}")

    # list.insert() does Not raise on a bad index the way pop() does, it silently appends. So validation
    # should be written per operation instead of assumed.
    insert_at(route, 99, "Rooftop Pad")
    print(f"insert_at(route, 99,'Rooftop Pad') - no error, appended: {route}")
    

if __name__ == "__main__":
    main()