"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")
    print("Lair Keycard Registry")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")

    # I am using my previous keycard registry from units 4 and 5 to come back as a
    # dictionary. Card ID is the key, the door it opens is the value.
    registry = {}

    # Python runs the card ID through a hash function to pick which slot it will go in.
    # A swipe goes into that slot instead of scanning the list like it was linear or halving
    # like its binary. Average O(1)
    registry[1250] = "Driveway Gate"
    registry[2500] = "Driveway Gate"
    registry[3750] = "North Fence"
    registry[5000] = "Trophy Room"
    registry[6250] = "Armory Vault Door"
    registry[7500] = "Full Access"
    print(f"Registry: {registry}")
    print(f"Cards Registered: {len(registry)}")
    
    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A swipe hashes the card ID, jumpp to the slot, and checks whether or not the key stored
    # there matches. One hop, no walking of the other cards.
    print(f"Swipe 7500 - {registry[7500]}")
    print(f"Swipe 3750 - {registry[3750]}")
    
    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    # Card 2500 gets bumped from the gate to the trophy room. Assigning to a key that already
    # exists overwrites the value in the same slot. No second 2500 gets added, the keys are 
    # unique so the count stays 6.
    print(f"Before: 2500 - {registry[2500]}")
    registry[2500] = "Trophy Room"
    print(f"After:  2500 - {registry[2500]}")
    print(f"Cards registered: {len(registry)}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    # Card 6250 was reported lost. del removes the key and the value from the table, so that
    # the next swipe of 6250 finds nothing in its slot and gets denied.
    print(f"Before: {registry}")
    del registry[6250]
    print(f"After:  {registry}")
    print(f"Cards registered: {len(registry)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Swipe a card that was never registered. registry[3000] throws a keyError and crahses the
    # hub. get() hands back the default to prevent that.
    print(f"Swipe 3000 - {registry.get(3000, 'Deny access')}")

    # Swipe the lost card. It was deleted above, so the lost card gets the same results as a card
    # that was never registered.
    print(f"Swipe 6250 - {registry.get(6250, 'Deny access')}")

    # Delete a missing card safely. del on a missing key is another KeyError. Check with in first.
    if 3000 in registry:
        del registry[3000]
    else:
        print("Delete 3000 - not registered, nothing removed")

    # Update a missing card. Assigning to a key that is not there does not fail, it quietly
    # registers a new card. For a door that is the wrong default, the update only goes 
    # through if the card already exists.
    if 9999 in registry:
        registry[9999] = "Full Access"
    else:
        print("Update 9999 - not registered, refused")
    print(f"Cards registered: {len(registry)}")

    # Empty registry. Nothing hashed in yet. So every swipe misses and gets denied.
    empty = {}
    print(f"Empty registry, swipe 5000 - {empty.get(5000, 'Deny Access')}")


if __name__ == "__main__":
    main()