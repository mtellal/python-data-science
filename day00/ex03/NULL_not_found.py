import math as m


def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    success = 0
    if (isinstance(object, type(None))):
        print("Nothing: None", obj_type)
    elif (isinstance(object, float) and m.isnan(object)):
        print("Cheese: nan", obj_type)
    elif (obj_type is int and object == 0):
        print("Zero: 0", obj_type)
    elif (isinstance(object, str) and len(object) == 0):
        print("Empty: ", obj_type)
    elif (isinstance(object, bool) and object is False):
        print("Fake: False", obj_type)
    else:
        print("Type not Found")
        success = 1
    return success
