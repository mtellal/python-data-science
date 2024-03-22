from array2D import slice_me

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))


### MORE TESTS ####

c='\033[0;1;97m'
red='\033[0;1;91m'
green='\033[0;1;92m'
nc='\033[0m'


def test_slice_me(array: list, start: int, end: int):
    print(f"array={array}, start={start}, end={end}")
    _slice_me = slice_me(array, start, end)
    print("slice_me:", _slice_me)
    try:
        _slice = array[slice(start, end)] 
        print("slice:", _slice)
        if _slice == _slice_me:
            print(green, "OK", nc)
        else:
            print(red, "KO", nc)
    except Exception as msg:
        print("Error: slice:", msg)
    print()


print(c, "\nMORE TESTS\n", nc)

print(c, "\nINVALID ARGS on slice_me\n", nc)

print(c, "\nempty list\n", nc)
test_slice_me([], 0, 0)
test_slice_me([], 1, 3)

print(c, "\nnot 2d array\n", nc)
test_slice_me("wdf", 0, 1)
test_slice_me(10, 0, 1)
test_slice_me((1, 2), 0, 1)
test_slice_me([1], 0, 0)
test_slice_me(["s"], 0, 1)
test_slice_me([{1, 2}], 0, 1)

print(c, "\ninvalid lists", nc)
test_slice_me([["s"]], 0, 1)
test_slice_me([[1], "d"], 0, 1)
test_slice_me([[1], [1, 2]], 0, 1)
test_slice_me([["s"]], 0, 1)

print(c, "\nvalid 2d array\n", nc)
test_slice_me([[1], [2], [3]], 0, 1)
test_slice_me([[1], [2], [3]], 2, 1)
test_slice_me([[1], [2], [3]], 0, 2)
test_slice_me([[1], [2], [3]], 0, 10)
test_slice_me([[1], [2], [3]], 0, -1)

