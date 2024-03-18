
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
    assert len(_list) > 0, "list empty"
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


def test(_list: list, start: int, end: int):
    print(f"\nslice_me({_list}, {start}, {end})")
    print(slice_me(_list, start, end))


def main():
    whiteBold = '\033[0;1;97m'
    default = '\033[0m'
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print("\nMORE TESTS\n")
    print(whiteBold, "\nEMPTY LIST\n", default)
    test([], 0, 0)
    test([], 1, 3)
    print(whiteBold, "\nNOT 2D ARRAY\n", default)
    test("wdf", 0, 1)
    test(10, 0, 1)
    test((1, 2), 0, 1)
    test([1], 0, 0)
    test(["s"], 0, 1)
    test([{1, 2}], 0, 1)
    print(whiteBold, "\nINVALID LISTS", default)
    test([["s"]], 0, 1)
    test([[1], "d"], 0, 1)
    test([[1], [1, 2]], 0, 1)
    test([["s"]], 0, 1)
    print(whiteBold, "\nVALID 2D ARRAYS\n", default)
    test([[1], [2], [3]], 0, 1)
    test([[1], [2], [3]], 2, 1)
    test([[1], [2], [3]], 0, 2)
    test([[1], [2], [3]], 0, 10)
    test([[1], [2], [3]], 0, -1)


if __name__ == "__main__":
    main()
