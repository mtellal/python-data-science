import math

def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    success = 0
    if (obj_type == type(None)):
        print("Nothing: None", obj_type)
    elif (obj_type == float and math.isnan(object)):
        print("Cheese: nan", obj_type)
    elif (obj_type == int and object == 0):
        print("Zero: 0", obj_type)
    elif (obj_type == str and len(object) == 0):
        print("Empty: ", obj_type)
    elif (obj_type == bool and object == False):
        print("Fake: False", obj_type)
    else: 
        print("Type not found")
        success = 1
    return success



"""
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
test((5,6))
test("Brian")

test(None)
test("")
test(56)
test({})
test(())
test((5,6))
test(float(0.5))
"""
