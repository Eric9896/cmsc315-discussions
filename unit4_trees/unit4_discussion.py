"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.

Overview:
Continuation of the Lair smart-home hub from the previous units. This unit
will focus on storing the keycard registry. Every card ID the door controllers
accept. Search answers if the card is registered. True unlocks, false denies.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # One card ID per node, both of the children start empty.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # Root, the tree is empty until the first insert.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Smaller goes left and larger goes right at each node.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Empty spot. This is where the value goes.
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal is duplicate and gets ignored, a card registered twice is still
        # just one card.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Linear search checks every card. A BST compares at the root and only
        # follows one side, so a balanced tree is O(log n) not O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Ran off the end of a branch, the card isn't registered.
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        # Left, then self, then right. Left is smaller and right is larger, that way the list
        # comes out sorted.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Lair Keycard Registry")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Middle value is first so both sides fill. Each insert compares at the root and drops into
    # one side, the other side isn't touched.
    registry = BST()
    cards = [5000, 2500, 7500, 1250, 3750, 6250, 8750]
    for card in cards:
        registry.insert(card)
    print(f"Inserted: {cards}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Cards went in scrambled and come out sorted without sort() call. Left is smaller
    # and right is larger at each node, so left, self, right is ascending order.
    print(f"In-Order: {registry.inorder()}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Two registered cards, both are True. 5000 is the root so it is the one comparison.
    print(f"Swipe 5000 - {registry.search(5000)} (registered, unlock)")
    print(f"Swipe 8750 - {registry.search(8750)} (registered, unlock)")

    # Two cards never registered. The search follows one path, runs off the end, and
    # will return false without checking all 7.
    print(f"Swipe 3000 - {registry.search(3000)} (unregistered, deny)")
    print(f"Swipe 9999 - {registry.search(9999)} (unregistered, deny)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Empty Tree. No root, so in-order is [] and every search is false
    # Nothing registered would mean every card is denied.
    empty = BST()
    print(f"Empty registry: inorder - {empty.inorder()}, search 5000 - {empty.search(5000)}")

    # Duplicate. Inserting 2500 again is ignored, so in-order is unchanged.
    registry.insert(2500)
    print(f"Duplicate 2500: inorder - {registry.inorder()}")


if __name__ == "__main__":
    main()