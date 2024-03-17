
"""
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""


def ft_filter(function, iterable):
    """
        Filter the iterable with the function in argument

    Args:
        function: Function used to filter
        iterable: Object to iterate
    Retuns:
        iterator: iterator of iterable
    """
    if function is None:
        return iter(iterable)
    return iter(x for x in iterable if function(x))
