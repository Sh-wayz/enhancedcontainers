from copy import deepcopy

class EnhancedList(list):
    def __init__(self):
        super().__init__()

    def append(self, item):
        """Appends and returns item."""

        list.append(self, item)
        return item

    def indices(self, value):
        """Returns all the indices of a given value"""

        def indices_gen():
            result = EnhancedList()
            offset = -1
            while True:
                try:
                    offset = self.index(value, offset+1)
                except ValueError:
                    return result
                yield offset

        return [*indices_gen()]

    indexes = indices  # for the degenerates who prefer .indexes() over .indices()

    def copy(self):
       """Returns a deep copy of the list"""

       return deepcopy(self)
