import time


def cach(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cach
def logg_running_function(a, b):
    time.sleep(4)
    return a + b