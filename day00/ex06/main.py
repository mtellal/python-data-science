import ft_filter as ft_filter_module
from ft_filter import ft_filter

print(ft_filter_module.__doc__)


def displayIterable(obj, function_str: str):
    print(function_str, end = '')
    for x in obj:
        print(x, end = ', ')
    print("")


def test_ft_filter(function, array, function_tested: str = ""):
    print("\nft_filter tested with", function_tested)
    print("array:", array)
    displayIterable(ft_filter(function, array), "ft_filer: ")
    displayIterable(filter(function, array), "filter: ")
    

def main():
    iseven = lambda x: (x % 2) == 0
    isodd = lambda x: (x % 2) != 0
    isupper = lambda x: str(x).isupper()
    islower = lambda x: str(x).islower()
    isalpha = lambda x: str(x).isalpha()
    isdigit = lambda x:  str(x).isdigit()
    arrayInt = [1, 2, 3, 4, 5, 6, 7, 8]
    test_ft_filter(isodd, arrayInt, "isodd")
    test_ft_filter(iseven, arrayInt, "iseven")
    test_ft_filter(None, arrayInt, "None")
    print("\nTests with str\n")
    test_ft_filter(isdigit, "my super phrase", "isdigit")
    test_ft_filter(isupper, "My Super Phrase", "isupper")
    test_ft_filter(islower, "My Super Phrase", "islower")
    print("\nTests with set")
    test_ft_filter(isdigit, {1, "wd", 2, (1, 2), 3}, "isdigit")
    test_ft_filter(isdigit, {1, 2, 3}, "isdigit") 
    test_ft_filter(islower, {"wdf", "wd", }, "islower") 

if __name__ == "__main__":
    main()

