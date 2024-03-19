import sys as sys


def oddOrEven(num: int):
    if (num % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


nb_args = len(sys.argv)
if nb_args >= 2:
    try:
        assert nb_args == 2, "more than one argument is provided"
        try:
            my_number = int(sys.argv[1])
            oddOrEven(my_number)
        except ValueError:
            raise AssertionError("argument is not an integer")
    except AssertionError as msg:
        print("AssertionError:", msg)
