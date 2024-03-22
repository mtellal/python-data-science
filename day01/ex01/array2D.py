
"""
    A function that takes as parameters a 2D array,
    prints its shape, and returns atruncated version of the array,
    based on the provided start and end arguments
"""


def verify_lists(_list: list, start: int, end: int):
    """
        Verify if arguments are valid

        Arguments:
            _list (list): array to verify
            start (int): int of start index (slice)
            end (int): int of end index (slice)
    """
    assert type(_list) is list, "bad argument"
    assert type(start) is int, "start not an int"
    assert type(end) is int, "end not an int"
    for x in _list:
        assert type(x) is list, "bad type list"
        for e in x:
            assert type(e) is int or type(e) is float, "item not float or int"
        assert len(x) == len(_list[0]), "list item bad size"


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slice a 2D array from start to end and return it

        Arguments:
            family (list): Array to slice
            start (int): first index to slice
            end (int): last index tto slice
        Returns:
            list: new sliced array
    """

    try:
        verify_lists(family, start, end)
        if len(family) == 0:
            print("My shape is: (0, 0)")
            return family
        print(f"My shape is: ({len(family)}, {len(family[0])})")
        x = slice(start, end)
        _list = family[x]
        if len(_list) == 0:
            print("My new shape is: (0, 0)")
        else:
            print(f"My new shape is: ({len(_list)}, {len(_list[0])})")
        return _list
    except AssertionError as msg:
        print("Error:", msg)
