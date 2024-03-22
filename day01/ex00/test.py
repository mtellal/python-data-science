from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))


c = '\033[0;1;97m'
nc = '\033[0m'

# PRINT MORE TESTS ON BMI FUNCTION

def test_give_bmi(heights: list, weights: list):
    print(f"height='{heights}', weights='{weights}'")
    print(give_bmi(heights, weights))
    print()

print(c, "\nMORE TESTS ON give_bmi\n", nc)

print(c, "INVALID ARGUMENTS\n", nc)

test_give_bmi("not list", [1, 2, 3])

test_give_bmi(15, [1, 2, 3])

test_give_bmi((1, 2), [1, 2, 3])

test_give_bmi(["oi"], [1, 2, 3]) # invalid type item

test_give_bmi([1], [1, 2, 3]) # not same size

test_give_bmi([(1), "e", 5], [1, 2, 3]) # invalid type item

test_give_bmi([(1), (1), 5], [1, 2, 3]) # invalid type item

test_give_bmi([(1, 2)], [1, 2, 3]) # invalid type item + size

test_give_bmi([[1], 2, 3], [1, 2, 3]) # invalid item 

test_give_bmi([1, 2, [3]], [1, 2, 3]) # invalid item 

test_give_bmi([[1], 2, 3], [1, 2, 3]) # invalid item 

test_give_bmi([], [1]) # invalid size

test_give_bmi([1], []) # invalid size

test_give_bmi([1], "") # invalid size

test_give_bmi([1], None) # invalid size

test_give_bmi(None, None) # invalid size

test_give_bmi([0], [1]) # can't calculate bmi from height as 0 

print(c, "\nVALID ARGUMENTS\n", nc)

test_give_bmi([], [])

test_give_bmi([1], [0])

test_give_bmi([1], [1])

test_give_bmi([-1, 1], [1, -1])

test_give_bmi([0], [56464646464646464])

test_give_bmi([64164164165416841654], [56464646464646464])

test_give_bmi([1, 2.58, 6564616816818184141841], [1654.64, 123.34, 3234])

test_give_bmi([1, 2, 3], [35.553, 234])

test_give_bmi([1, 234, 233], [-54654651, -542, -3543])

test_give_bmi([1, 1e300, 233], [-54654651, -542, -3543])



def test_apply_limit(bmi: list, limit: int) -> list[bool]:
    print(f"bmi={bmi}, limit={limit}")
    print(apply_limit(bmi, limit))
    print()

print(c, "\nMORE TEST ON apply_limit\n", nc)

print(c, "\nINVALID ARGS\n", nc)

test_apply_limit("dwf", 5)

test_apply_limit(5, 5)

test_apply_limit((5, 5), 5)

test_apply_limit([], 5)

test_apply_limit([""], 5)

test_apply_limit([[1]], 5)

test_apply_limit([1, 3, 2], 5.0)

test_apply_limit([1, 3, 2], "dwfw")

test_apply_limit([1, 3, 2], [5])

print(c, "\nVALID ARGS\n", nc)

test_apply_limit([1, 2, 3], 654654654654654465465464565465465465465)

test_apply_limit([654654, 646.235, 927.3], -654)

test_apply_limit([0, 0, 0], 9223372036854775808)

test_apply_limit([0, 0, 0], -9223372036854775808)

