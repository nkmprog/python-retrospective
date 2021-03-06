from collections import OrderedDict, defaultdict


def groupby(func, seq):
    result = defaultdict(list)
    for element in seq:
        result[func(element)].append(element)
    return result


def compose(func1, func2):
    return lambda x: func1(func2(x))


def iterate(func):
    current_function = lambda x: x
    while True:
        yield current_function
        current_function = compose(func, current_function)


def zip_with(func, *iterables):
    return (func(*args) for args in zip(*iterables))


def cache(func, cache_size):
    store = OrderedDict()

    if cache_size <= 0:
        return func

    def cached_function(*args):
        if args not in store:
            if len(store) >= cache_size:
                store.popitem(last=False)
            store[args] = func(*args)
        return store[args]
    return cached_function
