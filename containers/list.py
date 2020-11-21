from copy import deepcopy


class EnhancedList(list):
    """List subclass with the following alterations:
        - .append() returns the appended value.
        - .indices() returns all indices of the provided value
        - .copy() is a deep copy instead of shallow.

        """

    def __init__(self, _list=None):
        super().__init__([] if _list is None else _list)

    def append(self, item):
        """Appends and returns item."""

        list.append(self, item)
        return item

    def indices(self, value) -> int:
        """Returns all the indices of a given value"""

        def indices_gen() -> int:
            result = EnhancedList()
            offset = -1
            while True:
                try:
                    offset = self.index(value, offset+1)
                except ValueError:
                    return result
                yield offset

        return [*indices_gen()]

    indexes = indices  # for degenerates who prefer .indexes() over .indices()

    def copy(self):
        """Returns a deep copy of the list"""

        return deepcopy(self)


def test():
    """Simple testing."""
    list = ['1', '2', '2']
    test = EnhancedList(list)
    assert test.append('3') == '3'
    assert test.indices('2') == [1, 2]
    test2 = test.copy()
    test2[0] = 'test'
    if test[0] == 'test':
        assert False
    else:
        assert True


test()
