"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending places the newest value on top, supporting LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            # None safely indicates that no value was available to remove.
            return None

        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek examines the newest value without changing the stack.
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Appending at the back preserves the order in which values arrived.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            # None safely indicates that no value was available to remove.
            return None

        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front examines the oldest value without changing the queue.
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: TEXT-EDITOR UNDO HISTORY ===")

    undo_stack = Stack()
    editing_actions = [
        "Typed title",
        "Added paragraph",
        "Changed font",
        "Inserted image"
    ]

    for action in editing_actions:
        undo_stack.push(action)
        print(f"Pushed onto stack: {action}")

    print(f"\nCurrent top action: {undo_stack.peek()}")
    print("Undoing actions demonstrates LIFO order:")

    while not undo_stack.is_empty():
        print(f"Undid: {undo_stack.pop()}")

    empty_pop = undo_stack.pop()
    print(f"\nPopping from an empty stack returned: {empty_pop}")

    empty_peek = undo_stack.peek()
    print(f"Peeking at an empty stack returned: {empty_peek}")

    single_item_stack = Stack()
    single_item_stack.push("Only action")
    print("\nCreated a stack containing one item.")
    print(f"Removed from single-item stack: {single_item_stack.pop()}")
    print(
        "Is the single-item stack empty after removal? "
        f"{single_item_stack.is_empty()}"
    )

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: IT SUPPORT TICKETS ===")

    ticket_queue = Queue()
    support_tickets = [
        "Reset password",
        "Install printer",
        "Restore network access",
        "Update software"
    ]

    for ticket in support_tickets:
        ticket_queue.enqueue(ticket)
        print(f"Added to back of queue: {ticket}")

    print(f"\nTicket currently at the front: {ticket_queue.front()}")
    print("Processing tickets demonstrates FIFO order:")

    while not ticket_queue.is_empty():
        print(f"Processed: {ticket_queue.dequeue()}")

    empty_dequeue = ticket_queue.dequeue()
    print(f"\nDequeuing from an empty queue returned: {empty_dequeue}")

    empty_front = ticket_queue.front()
    print(f"Viewing the front of an empty queue returned: {empty_front}")

    single_item_queue = Queue()
    single_item_queue.enqueue("Only ticket")
    print("\nCreated a queue containing one item.")
    print(f"Removed from single-item queue: {single_item_queue.dequeue()}")
    print(
        "Is the single-item queue empty after removal? "
        f"{single_item_queue.is_empty()}"
    )

    # ==========================================
    # TODO (Student): CUSTOM SCENARIO APPLICATION
    # ==========================================
    # This support-desk simulation combines a FIFO queue for incoming
    # tickets with a LIFO stack for recently completed ticket actions.

    print("\n=== CUSTOM SCENARIO: SUPPORT DESK WITH UNDO HISTORY ===")

    pending_tickets = Queue()
    completed_actions = Stack()

    scenario_tickets = [
        "Ticket 101 - Reset password",
        "Ticket 102 - Configure email",
        "Ticket 103 - Repair printer",
        "Ticket 104 - Install security update"
    ]

    for ticket in scenario_tickets:
        pending_tickets.enqueue(ticket)
        print(f"Received: {ticket}")

    print("\nThe oldest tickets are processed first:")

    for _ in range(3):
        processed_ticket = pending_tickets.dequeue()

        if processed_ticket is not None:
            completed_actions.push(processed_ticket)
            print(f"Completed: {processed_ticket}")

    print(f"\nNext pending ticket: {pending_tickets.front()}")
    print(f"Most recently completed ticket: {completed_actions.peek()}")

    reopened_ticket = completed_actions.pop()

    if reopened_ticket is not None:
        print(f"Reopened most recent completed ticket: {reopened_ticket}")

    print(
        "The queue used FIFO for fair ticket processing, while the "
        "stack used LIFO to access the most recent completed action."
    )


if __name__ == "__main__":
    main()
