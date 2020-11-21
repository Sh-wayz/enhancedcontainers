class StackOverflowError(BaseException):
    pass


class Stack:
    """LIFO(Last In First Out) data structure. Implemented with lists."""

    def __init__(self, limit: int = 10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        """ Push element to top of stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        return self.stack.pop()

    def peek(self):
        """ Peek at the top-most element of the stack."""
        return self.stack[-1]

    def is_empty(self) -> bool:
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """ Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item) -> bool:
        """Check if item is in stack"""
        return item in self.stack


def test():
    """testing stack, what else?"""
    # Only basic texting here atm, feel free to improve
    stack = Stack()  # Defaults to 10
    assert stack.is_empty() is True
    assert stack.is_full() is False
