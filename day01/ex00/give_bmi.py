"""
    Calculate the bmi and apply an limit on it
"""


def isNumber(x):
    return type(x) is int or type(x) is float


def give_bmi(height: list[int | float], weight: list[int | float]) -> list:
    """
        From 2 lists of integer heights and weights,
        calculate the ibm and return the calculated values

        Arguments:
            height (list): list of height
            weight (list): list of weight
        Returns:
            list: list of ibm from heights and weights
    """
    try:
        err_i = "bad item list '"
        err_l = "bad type list"
        assert type(height) is list and type(weight) is list, err_l
        for x in height:
            assert type(x) is int or type(x) is float, err_i + str(x) + "'"
        for x in weight:
            assert type(x) is int or type(x) is float, err_i + str(x) + "'"
        assert len(height) == len(weight), "bad length lists"
        final = [None] * len(height)
        for i in range(0, len(height)):
            assert height[i] != 0, "bad item (0)"
            final[i] = weight[i] / (height[i] ** 2)
        return final
    except AssertionError as msg:
        print("Error:", msg)
    except OverflowError as msg:
        print("Error: invalid value:", msg)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Apply a limit on each bmi in a list,
        return a list of bool

        Arguments:
            bmi (list)
    """
    final = []
    try:
        assert type(bmi) is list, "bmi not a list"
        assert type(limit) is int, "invalid limit '" + str(limit) + "'"
        invalid_type = "bmi item not an int or float '"
        for x in bmi:
            assert type(x) is int, invalid_type + str(x) + "'"
            final.append(x > limit)
        return final
    except AssertionError as msg:
        print("Error:", msg)
