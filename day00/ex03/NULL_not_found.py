import math


def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    success = 0
    if (obj_type is type(None)):
        print("Nothing: None", obj_type)
    elif (obj_type == float and math.isnan(object)):
        print("Cheese: nan", obj_type)
    elif (obj_type == int and object == 0):
        print("Zero: 0", obj_type)
    elif (obj_type == str and len(object) == 0):
        print("Empty: ", obj_type)
    elif (obj_type is bool and object is False):
        print("Fake: False", obj_type)
    else:
        print("Type not found")
        success = 1
    return success
