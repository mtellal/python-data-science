import sys


def isPunctuationMark(c: str) -> bool:
    """
    Verify with the param str is a punctuation mark

    Args:
        c (str): string to verify

    Returns:
        bool: if str is a punctuation mark
    """
    return ".?!,;:-–()[]{}'\"".find(c) != -1


def countLetters(s: str) -> dict:
    """
    Count the letters types in a string

    Args:
        s (str): The string
    Returns:
        dict: The dictionary with the numbers and types of letters
    """
    slen = len(s)
    d = {
            "len": slen,
            "upperLetters": 0,
            "lowerLetters": 0,
            "punctuationMarks": 0,
            "spaces": 0,
            "digits": 0,
        }
    for i in range(0, slen):
        if s[i].isupper():
            d["upperLetters"] += 1
        elif s[i].islower():
            d["lowerLetters"] += 1
        elif isPunctuationMark(s[i]):
            d["punctuationMarks"] += 1
        elif len(s) >= 3 and s[i:i+3] == "...":
            i += 3
            d["punctuationMarks"] += 1
        elif s[i].isspace():
            d["spaces"] += 1
        elif s[i].isdigit():
            d["digits"] += 1
    return d


def display(d: dict):
    """
    Dsiplay the types and numbers inside a dictionary

    Args:
        d (dict): The dictionary to display

    """
    print("The text contains %s characters" % d["len"])
    print(d["upperLetters"], "upper letters")
    print(d["lowerLetters"], "lower letters")
    print(d["punctuationMarks"], "punctuation marks")
    print(d["spaces"], "spaces")
    print(d["digits"], "digits")


def main():
    args = sys.argv
    args_len = len(args)
    try:
        if args_len == 1:
            print("wait user stdin")
        else:
            assert args_len == 2, "wrong number of arguments"
            d = countLetters(args[1])
            display(d)
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
