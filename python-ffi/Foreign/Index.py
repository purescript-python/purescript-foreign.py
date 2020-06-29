def unsafeReadPropImpl(f, s, key, value):
    return f if value is None else s(value[key])


def unsafeHasOwnProperty(prop, value):
    return hasattr(value, prop)


def unsafeHasProperty(prop, value):
    return prop in value.keys()

