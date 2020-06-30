def unsafeFromForeign(value):
    return value


def unsafeToForeign(value):
    return value


def typeOf(value):
    return type(value).__name__


def tagOf(value):
    return "Number" if type(value) in [int, float] else "String" if type(value) == str else "Boolean" if type(value) == bool else "Function" if callable(value) else "Null" if value is None else "Object"


def isNull(value):
    return value is None


# not clear how to do this pythonically
def isUndefined(value):
    return isNull(value)


def isArray(value):
    return (type(value) == list) or (type(value) == tuple)

