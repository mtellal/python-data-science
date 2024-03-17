
"""
    A function that takes as parameters a 2D array, 
    prints its shape, and returns atruncated version of the array,
    based on the provided start and end arguments
"""

def verify_lists(l: list, start: int, end: int) -> bool:
   assert type(l) is list, "bad argument"
   assert type(start) is int, "start not an int"
   assert type(end) is int, "end not an int"
   for x in l:
       assert len(x) == len(l[0]), "list item bad size"


def slice_me(family: list, start: int, end: int) -> list:
    try:
        verify_lists(family, start, end)
        print("My shape is: (%d, %d)", % len(family), %len(family[0]))
        x = slice(start, end)
        l = family[x]
        print("My new shape is: (%d, %d)", % len(l), % len(l[0]))  
    except AssertionError as msg:
        print("Error:", msg)


def main():
    family = [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()

