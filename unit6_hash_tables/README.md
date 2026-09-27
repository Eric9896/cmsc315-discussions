# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

Still keeping to my theme of the Lair smart-home from the previous units. The keycard registry from units 4 and 5 came back one more time as a python dictionary. The card ID was the key and the door it opened was the value. A swipe looks the card up by ID, an existing key unlocked the door and a missing key meant deny.

unit 4 stored the registry in a tree and unit 5 searched it as a sorted list. Both had to compare the card ID against the other cards to find it. A dictionary hashes the IDs and jumps straight to the slot, so theres nothing to compare against.

## Implementation

## Insert

The registry started empty and six cards were added with `registry[card_id] = door`. Python ran all of the IDs through a hash function to pick which slot it lived in. That is what makes a dictionary a hash table, the key gets to decide where the value is stored, so finding it later is one hop. Average O(1) no matter how many cards are registered.

## Lookup

Swiping `7500` and `3750` used `registry[card_id]`. The ID gets hashed, the slot gets found, and the key in that slot gets checked against the one swiped. No other card gets touched.

## Update

Card `2500` was bumped from the Driveway Gate to the Trophy Room. Assigning to a key that already existed overwrote the value in the same slot. Keys are unique so the count stayed at 6.

## Delete

Card `6250` was reported lost, so `del registry[6250]` removed the key and its value. The count dropped to 5 and the next swipe of `6250` finds nothing.

## Edge Cases

**Missing card.** `registry[3000]` would have thrown a `KeyError` and crashed the hub. `registry.get(3000, 'Deny access')` returns the default instead.

**Delete a missing card.** `del` on a missing key is another `KeyError`, so the card was checked with `in` first and delete gets skipped.

**Update a missing card.** Assigning to a key that is not there does not fail, it quietly registers a new card. For a door that is the wrong default, so the update for `9999` was refused unless the card already existed.

**Empty registry.** Nothing was hashed in just yet, so every swipe missed and was denied.

## Discussion Board Reflection

This unit taught me that a dictionary is not searching for anything. The tree in unit 4 and the binary search in unit 5 both kept asking is the card bigger or smaller than this one. The hash function skips all of that, the card ID itself says where to look.

The update edge case was my biggest challenge. I expected `registry[9999] = "Full Access"` to complain the way a lookup on `9999` does, and it did not. The count went to 6 and the hub had handed full access to a card nobody registered. It ran fine and did the wrong thing, same as the last few units. Checking with `in` first fixed it.

Collisions are when two different card IDs hash to the same slot. Python has to keep both and check the actual key on a swipe, so a crowded slot costs a couple of extra checks instead of one. A decent hash function and a table that grows before it fills up keeps that rare, which is why the average stays O(1). A bad hash function puts every card in one slot and the dictionary quietly turns back into the unit 5 linear scan.