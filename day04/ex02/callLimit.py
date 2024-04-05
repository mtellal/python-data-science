def callLimit(limit: int):
    """
    A function that takes as argument a call limit
    of another function and blocks
    its execution above a limit
    """
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            nonlocal function
            if count >= limit:
                print("Error:", function, "call too many times")
                return
            function()
            count += 1
        return limit_function
    return callLimiter
