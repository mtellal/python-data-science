from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))


c = '\033[0;1;97m'
nc = '\033[0m'

# PRINT MORE TESTS ON BMI FUNCTION

def test(heights: list, weights: list):
    print(f"height='{heights}', weights='{weights}'")
    print(give_bmi(heights, weights))
    print()

print(c, "\nMORE TESTS ON give_bmi\n", nc)

print(c, "INVALID ARGUMENTS\n", nc)

test("not list", [1, 2, 3])

test(15, [1, 2, 3])

test((1, 2), [1, 2, 3])

test(["oi"], [1, 2, 3]) # invalid type item

test([1], [1, 2, 3]) # not same size

test([(1), "e", 5], [1, 2, 3]) # invalid type item

test([(1), (1), 5], [1, 2, 3]) # invalid type item

test([(1, 2)], [1, 2, 3]) # invalid type item + size

test([[1], 2, 3], [1, 2, 3]) # invalid item 

test([1, 2, [3]], [1, 2, 3]) # invalid item 

test([[1], 2, 3], [1, 2, 3]) # invalid item 

test([], [1]) # invalid size

test([1], []) # invalid size

test([1], "") # invalid size

test([1], None) # invalid size

test(None, None) # invalid size

test([0], [1]) # can't calculate bmi from height as 0 

print(c, "\nVALID ARGUMENTS\n", nc)

test([], [])

test([1], [0])

test([1], [1])

test([-1, 1], [1, -1])

test([0], [56464646464646464])

test([1], [1])

test([1], [1])

test([1], [1])

test([1], [1])



