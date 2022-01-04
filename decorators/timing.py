# Practical Example #2 - timing

import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname}: time took {after-before} secs to execute!")
        return value
    return wrapper


@timed
def my_func(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


print(my_func(10000))
