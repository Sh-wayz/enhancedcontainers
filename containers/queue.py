class Queue():

    """FIFO data structure. Implemented with a list."""

    def __init__(self, _list=None):


        self._items = ()[] if _list is None else _list)



    def is_empty(self):
        """Returns a boolean specifying whether or not the queue is empty"""

        return self._items == []


    def enqueue(self, item):
        """Adds an item to the queue."""

        return self._items.append(item)


    def dequeue(self):
        """Remove an item from the queue."""

        return self._items.pop(0)


    def peek(self):
        """View item in the queue without removing."""

        return self._items[0]

    def size(self):
        """Returns length of queue"""

        return len(self._items)
