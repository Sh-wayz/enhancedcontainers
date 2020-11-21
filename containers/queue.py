"""Queue data structure, FIFO, more info in the class desc."""

class Queue:

    """This data structure is used in situations where the first submitted object should be the first object viewed.
    This is called FIFO(First In Last Out).
    This would be best compared to a line of people waiting for some new fancy PC part, the first person in line is
    the first person to get the overpriced piece of tech that will be outdated in 4 years.  Of course, in code,
    there isn't much chance of people cutting in line, or stabbing each other to death brutally whilst they camp on
    the sidewalk."""

    def __init__(self):

        self.items = []



    def is_empty(self):
        """Returns a boolean specifying whether or not the queue is empty"""

        return self.items == []


    def enqueue(self, item):
        """Adds an item to the queue."""

        return self.items.append(item)


    def dequeue(self):
        """Remove an item from the queue."""

        return self.items.pop(0)


    def peek(self):
        """View item in the queue without removing."""

        return self.items[0]

    def size(self):
        """Returns length of queue"""

        return len(self.items)
