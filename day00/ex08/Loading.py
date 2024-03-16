
"""
    This programm copy the tqdm function
    tqdm is a function that allows you to easily create a progress bar

    Args:
        lst (iterable): the iterable where elements are selected

"""


def ft_tqdm(lst: range) -> None:
    """
        Create a progress bar from a range

        Args:
            lst (range): range to iterate
        Returns:
            None
    """
    nbChars = 50
    len_lst = len(lst)
    white = '█'
    if len_lst == 0:
        noelements = "0it [00:00, ?it/s]"
        print(noelements, end='', flush=True)
    else:
        for x in range(0, len_lst):
            x += 1
            _percent = int(x / (len_lst / 100))
            current_percent = int((x / (len_lst / 100)) * (nbChars / 100))
            whites = current_percent * white
            items = str(x) + "/" + str(len_lst)
            print_str = f"\r{str(_percent) + '%':>4}{'|':1s}{whites:50}{'|':1}"
            print(print_str, items, end='', flush=True)
            yield


def main():
    for x in ft_tqdm(range(74)):
        pass


if __name__ == "__main__":
    main()
