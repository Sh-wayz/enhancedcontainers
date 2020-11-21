class StackOverflowError(BaseException):
    pass


class Stack:
    """LIFO, defaults to a limit of 10."""

    def __init__(self, limit: int = 10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        """ Push element to top of stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)
        return data

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

    def __contains__(self, item):
        """Check if item is in stack"""
        return item in self.stack


def test():
    """Testing stack, what else?"""
    stack = Stack()  # Defaults to 10
    assert stack.is_empty() is True
    assert stack.is_full() is False
    try:
        stack.peek()
        assert False
    except IndexError:
        assert True
    try:
        stack.pop()
        assert False
    except IndexError:
        assert True
    assert stack.push('TEST') == 'TEST'
    assert stack.peek() == 'TEST'
    assert stack.is_empty() is False
    assert stack.size() == 1
    assert stack.is_full() is False
    assert stack.pop() == 'TEST'

    try:
        for i in range(0, 11):
            stack.push(i)
        assert False
    except StackOverflowError:
        assert True
    assert stack.size() == 10
    assert stack.is_full() is True
    assert stack.__contains__(5) is True
    assert stack.__contains__('TEST') is False


test()
