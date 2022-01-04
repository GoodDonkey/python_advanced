

def mydecorator(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return_value = function(*args, **kwargs)  # 함수가 실행된다.
        print("decorated!")
        return return_value
    return wrapper


@mydecorator
def hello(person):
    print("after...")
    return f"Hello {person}"


print(hello("donkey"))
