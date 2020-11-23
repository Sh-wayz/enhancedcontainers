# TODO: Add .__contains__()
class Queue():

    """FIFO data structure."""

    def __init__(self, _list: list = None):

        self._items = ([] if _list is None else _list)

    def is_empty(self) -> bool:
        """Returns a boolean specifying whether or not the queue is empty"""

        return self._items == []

    def enqueue(self, item):
        """Adds an item to the queue."""
        self._items.append(item)
        return item

    def dequeue(self):
        """Remove an item from the queue."""

        return self._items.pop(0)

    def peek(self):
        """View item in the queue without removing."""

        return self._items[0]

    def size(self) -> int:
        """Returns length of queue"""

        return len(self._items)
