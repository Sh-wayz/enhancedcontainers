class Stack:
    """LIFO(Last In First Out) data structure. Implemented with lists."""

    def __init__(self, _list=None):

        self._items = ([] if _list is None else _list)

    def empty(self):
        """Returns whether or not the stack is empty"""
        return self._items == []

    def size(self):
        """Returns the total amount of items in stack."""
        return len(self._items)

    def top(self):
        """Returns the value of the top item in the stack without removing."""
        return self._items[-1]

    def push(self, item):
        """Adds an item to the stack."""
        return self._items.append(item)

    def pop(self):
        """Removes the top item in the stack."""
        return self._items.pop()
