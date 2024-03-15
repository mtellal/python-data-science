
"""
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

def ft_filter(function, iterable):
    if (type(function) == type(None)):
        return iter(iterable)
    return iter(x for x in iterable if function(x))
