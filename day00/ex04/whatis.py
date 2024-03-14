import sys

def isNumber(s: str) -> bool:
    if s[0] == '-' or s[0] == '+':
        s = s[1:]
    for i in range(0, len(s)):
        if (s[i].isdigit() == False):
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

"""
#!/bin/bash

echo "Testing whatis.py"

whatis() {
        echo -e "\npython whatis.py $@"
        python whatis.py $@
}


whatis 14
whatis -5
whatis
whatis 0
whatis Hi!
whatis 13 5
whatis 65465464654654654654653
whatis 65465464654654654654654
whatis -1
whatis whatis.py
whatis +14
whatis ++13
whatis -13
whatis --13
"""
