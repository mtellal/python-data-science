import sys
from ft_filter import ft_filter

"""

This program take 2 arguments a string(S) and an integer(N)
and display the number of words with more than N.

if the number is invalid the programm must display an AssertionError

"""


def verify_arguments() -> int:
    """
        Verify if the argument is a valid int

        Returns:
            int: the valid int in argument
        Exception:
            Raise AssertionError with not a valid int
    """
    len_args = len(sys.argv)
    assert len_args == 3, "the arguments are bad"
    assert isinstance(sys.argv[1], str), "arg[1] invalid str"
    try:
        int(sys.argv[2])
    except ValueError:
        raise AssertionError("arg[2] invalid int")
    return int(sys.argv[2])


def main():
    """
        From a text in input (S) and an int (N),
        display a list of words with a length greater than int (N)
        Args:
            S (str): Text to filter
            N (int): Number that words length must respect
        Returns:
            Display a list of words
    """
    try:
        final = []
        word_len = verify_arguments()
        words = sys.argv[1].split(" ")
        it = ft_filter(lambda x: (len(x) > word_len and len(x) > 0), words)
        final = []
        for x in it:
            assert x.isalnum(), "invalid string not alnum"
            final.append(x)
        print(final)
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
