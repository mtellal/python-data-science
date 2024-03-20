import ft_filter as ft_filter_module
from ft_filter import ft_filter


print(ft_filter_module.__doc__)


def displayIterable(obj, function_str: str):
    print(function_str, end='')
    print(list(obj))


def test(function, array, function_tested: str = ""):
    print("\nft_filter tested with", function_tested)
    print("array:", array)
    displayIterable(ft_filter(function, array), "ft_filer: ")
    displayIterable(filter(function, array), "filter: ")


def main():
    print("Tests with list")
    test(lambda x: (x % 2) != 0, [1, 2, 3, 4], "isodd")
    test(lambda x: (x % 2) == 0, [1, 2, 3, 4], "iseven")
    test(None, [1, 2, 3, 4], "None")
    print("\nTests with str\n")
    test(lambda x: x == "!", "my super phrase", "isdigit")
    test(lambda x: x.isupper(), "My Super Phrase", "isupper")
    test(lambda x: x.islower(), "My Super Phrase", "islower")
    print("\nTests with set")
    test(lambda x: str(x).isdigit(), {1, "wd", 2, (1, 2), 3}, "isdigit")
    test(lambda x: str(x).isdigit(), {1, 2, 3}, "isdigit")
    test(lambda x: str(x).islower(), {"wdf", "wd", }, "islower")


if __name__ == "__main__":
    main()
