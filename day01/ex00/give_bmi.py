

def isNumber(x) -> bool:
    return type(x) is int or type(x) is float

def verify_lists(height: list, weight: list) -> int:
    assert list(map(isNumber, height)).count(False) == 0, "bad item in list"
    assert list(map(isNumber, weight)).count(False) == 0, "bad item in list"
    assert len(height) == len(weight), "bad length lists"

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
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
    return list(map(lambda x: x > limit, bmi))

def main():
    give_bmi(["dw", 1, 2, 12.3], [])
    give_bmi([1, 2, 12.3], None)
    give_bmi([1, 2, 12.3], [1, 2])
    give_bmi(["dw", 1], [1, 2])
    give_bmi([2.3, 1], [1, 2])

if __name__ == "__main__":
    main()
