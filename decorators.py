

def mydecorator(function):

    def wrapper():
        print("I am decorating your function!")
        function()
        print("decorated!")

    return wrapper


@mydecorator
def hello_world():
    print("Hello World")


hello_world()
