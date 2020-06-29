def typeOf(value):
    return type(value).__name__


def tagOf(value):
    return str(value)


def isNull(value):
    return value is None


# not clear how to do this pythonically
def isUndefined(value):
    return isNull(value)


def isArray(value):
    return (type(value) == list) or (type(value) == tuple)

