
def enhance(thing):
    """Used to recursively convert regular containers into EnhancedDicts"""

    if isinstance(thing, dict):  # Convert dict to dot-accessible EnhancedDict
        return EnhancedDict(thing)

    # Adds support for iterables which are subclasses or instances of lists and tuples
    if isinstance(thing, (list, tuple)):
        return type(thing)(enhance(item) for item in thing)

    return thing


class EnhancedDict(dict):
    """Dict subclass with the following changes:
        - dot-access | dict values are accessible via dict.key
        - .copy() returns a deep copy rather than shallow"""

    def __init__(self, _dict=None):
        if _dict is None:  # Allows creating EnhancedDict via EnhancedDict()
            _dict = {}

        dict.__init__(self, {k: enhance(v) for (k, v) in _dict.items()})

    # Override the attribute methods to add dot access
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # Add dot-access EnhancedDict.a = 'Gt'
        return dict.__setitem__(self, name, enhance(value))

    def copy(self):  # Deep copys instead of default shallow copy
        return enhance(dict.copy(self))
