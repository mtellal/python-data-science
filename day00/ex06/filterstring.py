import sys
from ft_filter import ft_filter

"""

This program take 2 arguments a string(S) and an integer(N)
and display the number of words with more than N.

if the number is invalid the programm must display an AssertionError

"""


def verify_arguments() -> int:
    len_args = len(sys.argv)
    assert len_args == 3, "the arguments are bad"
    try:
        s = str(sys.argv[2])
        sign = 1
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign *= -1
            s = s[1:]
        if s.isdigit() is False:
            raise Exception("not valid int")
        else:
            return int(s) * sign
    except Exception:
        raise AssertionError("the arguments are bad")


def main():
    try:
        final = []
        word_len = verify_arguments()
        words = sys.argv[1].split(" ")
        it = ft_filter(lambda x: (len(x) > word_len and len(x) > 0), words)
        final = []
        for x in it:
            final.append(x)
        print(final)
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
