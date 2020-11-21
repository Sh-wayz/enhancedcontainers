class Queue():

    """FIFO data structure. Implemented with a list."""

    def __init__(self, _list: list = None):

        self._items = ([] if _list is None else _list)

    def is_empty(self) -> bool:
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

    def size(self) -> int:
        """Returns length of queue"""

        return len(self._items)


def test():
    """Basic testing."""
    queue = Queue()
    assert queue.is_empty() is True
    try:
        queue.peek()
        assert False
    except IndexError:
        assert True
    queue.enqueue(69)
    queue.enqueue(666)
    assert queue.peek() == 69
    assert queue.dequeue() == 69
    assert queue.peek() == 666
    assert queue.size() == 1
    assert queue.is_empty() is False
    assert queue.dequeue() == 666
    assert queue.size() == 0
    assert queue.is_empty() is True


# test()
