

def ft_tqdm(lst: range) -> None:
    nbChars = 40
    percent = len(lst) / 100
    white = '\033[47m'
    default = '\033[0m'
    previous_percent = 0
    for x in lst:
        _percent = int(x * percent)
        current_percent = int((x * percent) * (nbChars / len(lst)))
        if current_percent != previous_percent:
            spercent = str(_percent) + "%"
            whites = "#" * current_percent
            complete = str(_percent) + "/100"
            print(f'\r{spercent:>4}{"|":1s}{whites:<40}{"|":1s} {complete:7} [00:00<00:00] ', end = '', flush = True)
        previous_percent = current_percent
        yield
    print(default)
