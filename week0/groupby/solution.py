def groupby(func, seq):
    result = {}
    for x in seq:
        if func(x) in result:
            result[func(x)].append(x)
        else:
            result[func(x)] = [x]
    return result
