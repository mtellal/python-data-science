"""
    Calculate the bmi and apply an limit on it
"""


def isNumber(x) -> bool:
    return type(x) is int or type(x) is float


def verify_lists(height: list, weight: list) -> int:
    assert list(map(isNumber, height)).count(False) == 0, "bad item in list"
    assert list(map(isNumber, weight)).count(False) == 0, "bad item in list"
    assert len(height) == len(weight), "bad length lists"


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
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
        assert type(height) is list and type(weight) is list, "bad type list"
        verify_lists(height, weight)
        print("list valid, going on ...")
        final = [None] * len(height)
        for i in range(0, len(height)):
            final[i] = weight[i] / (height[i] ** 2)
        return final
    except AssertionError as msg:
        print("Error:", msg)


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
        invalid_type = "bmi item not an int or float"
        for x in bmi:
            assert type(x) is int or type(x) is float, invalid_type
            final.append(x > limit)
        return final
    except AssertionError as msg:
        print("Error:", msg)


def main():
    give_bmi(["dw", 1, 2, 12.3], [])
    give_bmi([1, 2, 12.3], None)
    give_bmi([1, 2, 12.3], [1, 2])
    give_bmi(["dw", 1], [1, 2])
    give_bmi([2.3, 1], [1, 2])


if __name__ == "__main__":
    main()
