
def enhance(con):
    """Used to recursively convert regular containers into EnhancedDicts"""

    if isinstance(com, dict):  # Convert dict to dot-accessible EnhancedDict
        return EnhancedDict(con)

    # This adds support for iterables which are subclasses or instances of lists and tuples
    if isinstance(thing, (list, tuple)):
        return type(thing)(classify(item) for item in thing)

    return thing


class EnhancedDict(dict):
    """dict subclass required for dot-access"""

    def __init__(self, _dict=None):
        if _dict is None:  # Allow for creating a new EnhancedDict via EnhancedDict()
            _dict = {}

        dict.__init__(self, {k:classify(v) for (k, v) in _dict.items()})

    # Override the attribute methods to add dot access
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # Add dot-access EnhancedDict.a = 'something'
        return dict.__setitem__(self, name, classify(value))

    def copy(self):  # Actually is a deep copy unlike the default shallow .copy()
        return classify(dict.copy(self))
