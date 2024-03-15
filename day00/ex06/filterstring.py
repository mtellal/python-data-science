import sys

def verify_arguments() -> int:
    len_args = len(sys.argv)
    assert len_args == 3, "the arguments are bad"
    try:
        s = str(sys.argv[2])
        sign = 1;
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign *= -1
            s = s[1:]
        if s.isdigit() == False:
            raise Exception("not valid int")
        else:
            return int(s) * sign
    except:
        raise AssertionError("the arguments are bad")

def main():
    try:
        final = []
        word_len  = verify_arguments()
        words = sys.argv[1].split(" ")
        valid_word = lambda x: (len(x) > word_len and len(x) > 0)
        final = [x for x in words if valid_word(x)]
        print(final)
    except AssertionError as msg:
        print("AssertionError:", msg)

if __name__ == "__main__":
    main()
