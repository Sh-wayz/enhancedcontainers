class Stack:
    """LIFO(Last In First Out) data structure implemented with lists."""

    def __init__(self):

        self.items = []

    def empty(self):
        """Returns whether or not the stack is empty"""
        return self.items == []

    def size(self):
        """Returns the total amount of items in stack."""
        return len(self.items)

    def top(self):
        """Returns the value of the top item in the stack without removing."""
        return self.items[-1]

    def push(self, item):
        """Adds an item to the stack."""
        return self.items.append(item)

    def pop(self):
        """Removes the top item in the stack."""
        return self.items.pop()
