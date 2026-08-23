"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
Continuation of the smart-home ("Lair") from unit 1, this program adds
the security layer that decides what the hub is allowed to do.
    Queue (FIFO) Access requests waiting on the owners approval
    Stack (LIFO) Rollback history for the security changes applied
"""

from collections import deque


class Stack:
    """LIFO Used here as rollback"""

    def __init__(self):
        # A list works due to adding and removing at the end are both 0(1).
        self._items = []

    def push(self, value):
        # Item is always the next one out.
        self._items.append(value)

    def pop(self):
        # This raises IndexError if the stack is empty, its the same thing
        # python's own list.pop() does on an empty list. Returning None would
        # make "nothing to undo" look like a successful undo, and the caller 
        # would miss it.
        if self.is_empty():
            raise IndexError("Cannot pop: rollback history is empty.")
        return self._items.pop() #No index gets removed the LAST item

    def peek(self):
        # Reads the top item without changing the stack, it answers
        # "what would come off next?"" and leave history intact.
        if self.is_empty():
            raise IndexError("Cannot peek: rollback history is empty.")
        return self._items[-1] # Index is -1 the top of the stack

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._items) == 0


class Queue:
    def __init__(self):
        # Collections.deque removes from the front of the list. The list would be
        # 0 per the dequeue because items shift down one slot.
        self._items = deque()

    def enqueue(self, value):
        # FIFO enqueue adds at the back while dequeue removes from the front. Since
        # they use different ends, the order is preserved
        self._items.append(value)

    def dequeue(self):
        # Raise instead of returning none so empty cannot be ignored
        if self.is_empty():
            raise IndexError("Cannot dequeue: request queue is empty.")
        return self._items.popleft() # removes from the front

    def front(self):
        # returns the request thats been waiting the longest- next in line to
        # be viewed
        if self.is_empty():
            raise IndexError("Cannot read front: request queue is empty.")
        return self._items[0] # index is 0 in front of queue

    def is_empty(self):
        # Return True if the queue has no values.
        return len(self._items) == 0


def main_stack():
    print("\n=== STACK DEMO (LIFO) - Lair rollback history ===")

    history = Stack()

    # ===============================
    # STACK DEMO
    # ===============================
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.

    for change in ["UNLOCK  - Armory Vault",
                   "DISABLE - Vault Alarm",
                   "OPEN    - Suit Display Case",
                   "EQUIP   - Flight Suit"]:
        history.push(change)
        print(f" Applied: {change}")

    print(f"\nNext change to reverse (peek): {history.peek()}")
    print("peek() only reads the top item - nothing removed")

    print("\nRe-securing the lair. The changes reverse in the OPPOSITE order:")
    while not history.is_empty():
        print(f" undo: {history.pop()}")
    print("Reversing UNLOCK first would seal the vault with the display"
        " case still open and alarm off, so LIFO is the only order"
        " that can leave the lair secure.")

        # Edge Cases:
        # 6. Show what happens when peek() is used on an empty stack.
        # 7. Create a stack with only one item, remove it,
        # and verify the stack is empty afterward.

    print("\n--- Stacks edge cases ---")
    print("pop() on an empty stack:")
    try:
        history.pop()
    except IndexError as error:
        print(f" Handled Safely - IndexError {error}")

    print("peek() on empty stack:")
    try:
        history.peek()
    except IndexError as error:
        print(f" Handled safely IndexError: {error}")

    print("A stack holding exactly one item:")
    single = Stack()
    single.push("DIM    Trophy Room Lights")
    print(f" after push is_empty(): {single.is_empty()}")
    print(f" poppped {single.pop()}")
    print(f" after pop  is_empty(): {single.is_empty()}")

def main_queue():
    print("\n=== QUEUE DEMO (LIFO) - Lair approval line ===")

    request_line = Queue()

    # ===============================
    # QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.

    for request in ["REQ-01 Driveway     Open Gate",
                    "REQ-02 Armory Vault Unlock",
                    "REQ-03 Trophy Room  Dim Lights",
                    "REQ-04 Perimeter    Arm Cameras"]:
        request_line.enqueue(request)
        print(f" requested: {request}")
    
    print(f"\nNext request up for approval (front: {request_line.front()})")
    print("front() only read requests - nothing removed.")

    print("\nReviewing. The requests are in ARRIVAL order:")
    while not request_line.is_empty():
        print(f" approved: {request_line.dequeue()}")
    print("REQ-01 waited the longest so it goes first. LIFO requests"
          " would keep piling ontop of the gate request and it could"
          " never be seen")

    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n--- Queues edge cases ---")
    
    print("pop() on an empty stack:")
    try:
        request_line.dequeue()
    except IndexError as error:
        print(f" Handled Safely IndexError: {error}")

    print("front() on an empty queue:")
    try:
        request_line.front()
    except IndexError as error:
        print(f" Handled Safely IndexError: {error}")

    print("A queue holding exactly one item:")
    single = Queue()
    single.enqueue("REQ-05 Workshop      power up tools")
    print(f" after enqueue is_empty(): {single.is_empty()}")
    print(f" dequeued {single.dequeue()}")
    print(f" after dequeue is_empty(): {single.is_empty()}")

def main():
    print("=== STACKS AND QUEUES ===")
    main_stack()
    main_queue()

if __name__ == "__main__":
    main()
