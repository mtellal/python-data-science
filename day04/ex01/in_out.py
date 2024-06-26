

def square(x: int | float) -> int | float:
    return x ** 2


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    """
    A  function that takes as argument a number
    and a function, it returns an object that when called
    returns the result of the arguments calculation
    """
    count = 0

    def inner() -> float:
        nonlocal count
        value = function(x)
        for i in range(0, count):
            value = function(value)
        count += 1
        return value
    return inner
