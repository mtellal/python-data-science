import math


def var(_list: list):
    mu = 0
    for x in _list:
        mu += x
    mu /= len(_list)
    total = 0
    for x in _list:
        total += (abs(x - mu) ** 2)
    return (total / len(_list))


def std(_list: list):
    return math.sqrt(var(_list))


def quartile(_list: list):
    _list.sort()
    quart = int(len(_list) / 4)
    return [float(_list[quart]), float(_list[len(_list) - 1 - quart])]


def median(_list: list):
    _list.sort()
    half = int(len(_list) / 2)
    return (_list[half])


def mean(_list: list):
    mean = 0
    for x in _list:
        mean += x
    return mean / len(_list)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    statistics operations on list
    """
    valid_keys = ["mean", "median", "quartile", "std", "var"]
    functions = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "std": std,
            "var": var
            }
    for k, v in kwargs.items():
        try:
            assert valid_keys.index(v) != -1, "invalid key"
            print(f'{v}:', functions[v](list(args)))
        except Exception:
            print("ERROR")
