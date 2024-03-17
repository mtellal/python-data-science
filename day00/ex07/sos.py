import sys


"""
    This program convert a string argument in morse.

    Args:
        s (str): string to convert

    Returns:
        print the converted string in stdout
"""


def verify_text():
    assert len(sys.argv) == 2, "the arguments are bad"


def convertChar(c: str) -> str:
    NESTED_MORSE = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
    }
    return NESTED_MORSE[c.upper()] + " "


def main():
    try:
        verify_text()
        text = sys.argv[1]
        final = ""
        for x in text:
            if x.isalnum() is False:
                if x.isspace():
                    final += "\\" + " "
                else:
                    raise AssertionError("the arguments are bad")
            else:
                final += convertChar(x)
        print(final[:-1])
    except AssertionError as msg:
        print("AssertionError:", msg)

if __name__ == "__main__":
    main()
