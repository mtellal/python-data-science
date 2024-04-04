def callLimit(limit: int):
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
