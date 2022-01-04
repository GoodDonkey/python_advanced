# Practical Example #1 - Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open("logfile.txt", 'a+') as f:
            fname = function.__name__
            print(f"{fname}: return value is {value}\n")
            f.write(f"{fname}: return value is {value}\n")
        return value
    return wrapper


@logged
def add(x, y):
    return x + y


print(add(1, 22))
