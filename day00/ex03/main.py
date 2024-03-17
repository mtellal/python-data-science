from NULL_not_found import NULL_not_found


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))


def test(object: any):
    print("NULL_not_found(", object, ")")
    print(NULL_not_found(object))


print("\n MORE TESTS \n")

test("wdfw")
test(5)
test([])
test({5})
test(())
test((5, 6))
test("Brian")

test(None)
test("")
test(56)
test({})
test(())
test((5, 6))
test(float(0.5))
