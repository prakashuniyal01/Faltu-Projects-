# decorator

import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} took {end - start} seconds to execute.')
        return result
    return wrapper

# as a decorator pass krna h isme 
@timing
def example_function(n):
    time.sleep(n)

example_function(2)

# timing(3)