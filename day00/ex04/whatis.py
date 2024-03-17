import sys


def isNumber(s: str) -> bool:
    if s[0] == '-' or s[0] == '+':
        s = s[1:]
    for i in range(0, len(s)):
        if (s[i].isdigit() is False):
            return False
    return True


def oddOrEven(num: int):
    if (num % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


nb_args = len(sys.argv)
if nb_args >= 2:
    try:
        arg = sys.argv[1]
        assert nb_args == 2, "more than one argument is provided"
        assert isNumber(arg), "argument is not an integer"
        oddOrEven(int(arg))
    except AssertionError as msg:
        print("AssertionError:", msg)
